#!/usr/bin/env python
# -*- coding: utf-8 -*-


from appium import webdriver
import pytest

import sys
import logging
import os
import time
from get_project_path import GetProjectPath
import shutil
from shutil import copy
from function.hexin_email import HexinEmail

ROOT_PATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(ROOT_PATH)

PY3 = sys.version_info[0] == 3
framework_dir = os.path.join(os.path.abspath(__file__), "..")

logging.basicConfig(level = logging.INFO,
                    filename = os.path.join(framework_dir, "test.log"),
                    filemode = "w",
                    stream = sys.stdout,
                    format = "%(asctime)s - [%(name)s] %(levelname)s: %(message)s")
framework_logger = logging.getLogger("pytest")
passedList = []
failedList = []
rerunList = []

@pytest.mark.trylast
def pytest_runtest_setup(item):
    framework_logger.info("==Begin to run test case %s==" % item.name)


@pytest.fixture(scope = 'function')
def logger(request):
    # set function name as tag automatically
    test_logger = logging.getLogger(request.function.func_name)

    return test_logger


def pytest_addoption(parser):
    parser.addoption("--platform_name", help = "platform name of device", required = True)
    parser.addoption("--platform_version", help="platform version of device", required=True)
    parser.addoption("--device_name", help = "name of device", required = True)
    parser.addoption("--device_udid", help = "udid of device")
    parser.addoption("--bundle_id", help = "bundleId of application")
    parser.addoption("--app_path", help="path of app file")


@pytest.fixture(scope = 'session')
def platform_name(request):
    return request.config.getoption('platform_name')

@pytest.fixture(scope= 'session')
def platform_version(request):
    return request.config.getoption('platform_version')

@pytest.fixture(scope = 'session')
def device_name(request):
    return request.config.getoption('device_name')

@pytest.fixture(scope = 'session')
def device_udid(request):
    return request.config.getoption('device_udid')

@pytest.fixture(scope = 'session')
def bundle_id(request):
    return request.config.getoption('bundle_id')

@pytest.fixture(scope = 'session')
def app_path(request):
    return request.config.getoption('app_path')


@pytest.fixture(scope = 'function')
def driver(request, platform_name, platform_version, device_name, device_udid, bundle_id, app_path):
    # equals to setUp
    desired_caps = {}
    # basic settings
    desired_caps['platformName'] = platform_name
    desired_caps['platformVersion'] = platform_version
    # real device
    desired_caps['deviceName'] = device_name
    desired_caps['udid'] = device_udid
    desired_caps['bundleId'] = bundle_id
    # instruments for app
    desired_caps['app'] = app_path


    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    request.node._driver = driver
    # equals to tearDown
    request.addfinalizer(driver.quit)
    return driver

@pytest.fixture(scope = 'function')
def pytest_unconfigure(config):
    """uploadResult()"""
    uploadResult()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    summary = []
    extra = getattr(report, 'extra', [])
    driver = getattr(item, '_driver', None)
    failure = report.failed


    # add log
    if report.when == "setup":
        framework_logger.info("==Finish running setup of test case %s" % item.name)
        framework_logger.info("**Test result of setup: %s" % report.outcome)
    if report.when == "call":
        # only log result of test case itself. Skip setup and teardown
        framework_logger.info("==Finish running test case %s" % item.name)
        framework_logger.info("**Test result of test case: %s**" % report.outcome)
        statistics(report,item)
    if report.when == "teardown":
        framework_logger.info("==Finish running teardown of %s" % item.name)
        framework_logger.info("**Test result of teardown: %s" % report.outcome)

    if not report.passed:
        framework_logger.info("%s infos: %s" % (report.outcome.capitalize(), str(report.longrepr.reprcrash)))
        framework_logger.error("%s traceback: %s" % (report.outcome.capitalize(), str(report.longrepr.reprtraceback)))



    if driver is not None:
        if failure:
            _gather_screenshot(item, report, driver, summary, extra)
            _gather_page_source(item, report, driver, summary, extra)

    if summary:
        report.sections.append(('pytest-appium', '\n'.join(summary)))
    report.extra = extra


################################  以下是自定义方法  #######################################
def _gather_screenshot(item, report, driver, summary, extra):
    try:
        screenshot = driver.get_screenshot_as_base64()
    except Exception as e:
        summary.append('WARNING: Failed to gather screenshot: {0}'.format(e))
        return
    pytest_html = item.config.pluginmanager.getplugin('html')
    if pytest_html is not None:
        # add screenshot to the html report
        extra.append(pytest_html.extras.image(screenshot, 'Screenshot'))


def _gather_page_source(item, report, driver, summary, extra):
    try:
        html = driver.page_source
        if not PY3:
            html = html.encode('utf-8')
    except Exception as e:
        summary.append('WARNING: Failed to gather Page Source: {0}'.format(e))
        return
    pytest_html = item.config.pluginmanager.getplugin('html')
    if pytest_html is not None:
        # add page source to the html report
        extra.append(pytest_html.extras.text(html, 'HTML'))


"""
    把最后的结果上传到服务器的documents
"""
def uploadResult():
    #读取运行用例id
    sign = "0"
    run_case_id = "9999999"
    file_path = GetProjectPath.getProjectPath() + '/runConf.txt'
    if not os.path.isfile(file_path):
        file = open(file_path, 'w')
        file.write('9999999\n0')
        file.close()
    else:
        file = open(file_path, 'r')
        i = 0
        for line in file.readlines():
            if i == 0:
                line = line.strip('\n') #去掉换行符
                msg = line
            elif i == 1:
                line = line.strip('\n') #去掉换行符
                sign = line
                break
            i = i + 1
        file.close()
        run_case_id = msg
    resultWriteToTxt(run_case_id)

    #如果不需要把结果上传服务器地址,和发邮件通知,return
    if sign != "1":
        return

    #把结果上传服务器地址
    #-----截图
    screen_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    sourceDir = GetProjectPath.getProjectPath() + '/result/' + screen_date + '/' + run_case_id
    targetDir = '/Library/Webserver/Documents/result/{}/screenshot/'.format(run_case_id)
    print(sourceDir)
    print(targetDir)
    if not os.path.isdir(targetDir):
        os.makedirs(targetDir)
    for root, dirs, files in os.walk(sourceDir):
        for i in xrange(0, files.__len__()):
            sf = os.path.join(root, files[i])
            copy(sf, targetDir)

    # ------report报告
    htmlSourceDir = GetProjectPath.getProjectPath()+"/report.html"
    htmlTargetDir = '/Library/Webserver/Documents/result/{}/report'.format(run_case_id)
    if not os.path.isdir(htmlTargetDir):
        os.makedirs(htmlTargetDir)
    copy(htmlSourceDir,htmlTargetDir)

    #------pytest生成的,与report相关的文件(如:网页的格式,错误截图)
    assertTargetDir = htmlTargetDir + "/assets"
    if not os.path.isdir(assertTargetDir):
        os.makedirs(assertTargetDir)
    assetsSourceDir = GetProjectPath.getProjectPath()+"/assets"
    filelist = []
    filelist = os.listdir(assetsSourceDir)
    for f in filelist:
        filepath = os.path.join(assetsSourceDir, f)
        if os.path.isfile(filepath):
            copy(filepath,assertTargetDir)
            os.remove(filepath)
        elif os.path.isdir(filepath):
            copy(filepath, assertTargetDir)
            shutil.rmtree(filepath, True)


    #发邮件通知
    hexin_email = HexinEmail()
    #用例统计数据
    rate_list = []
    rate_list.append(len(passedList))
    rate_list.append(len(failedList))
    rate_list.append(len(rerunList))
    to_list = ['tianmaotao@myhexin.com']
    cc_list = ['tianmaotao@myhexin.com']
    hexin_email.sendEmail(to_list=to_list, cc_list=cc_list, rate_list=rate_list, run_case_id=run_case_id)

"""
    统计成功数,失败数,重跑数
"""
def statistics(report,item):
    if report.outcome == "passed":
        passedList.append(item.name)
    if report.outcome == "failed":
        n = len(failedList)
        if n >= 1:
            if failedList[n - 1] != item.name:
                failedList.append(item.name)
            else:
                m = len(rerunList)
                if m >= 1:
                    if rerunList[m - 1] != item.name:
                        rerunList.append(item.name)
                else:
                    rerunList.append(item.name)
        else:
            failedList.append(item.name)

"""
    把统计的成功数,失败数,重跑数数据写入txt文件并上传服务器地址
"""
def resultWriteToTxt(case_id):
    file_path = GetProjectPath.getProjectPath() + '/statistics.txt'
    file = open(file_path, 'w')
    if os.path.isfile(file_path):
        file.write("{}\n".format(len(passedList)))
        file.write("{}\n".format(len(failedList)))
        file.write("{}\n".format(len(rerunList)))
        file.close()
    else:
        i=0
        for line in file.readlines():
            if i==0:
                str = line
                s = line.replace(str, "{}".format(len(passedList)))
                file.writelines(s)
            if i==1:
                str = line
                s = line.replace(str, "{}".format(len(failedList)))
                file.writelines(s)
            if i==2:
                str = line
                s = line.replace(str, "{}".format(len(rerunList)))
                file.writelines(s)
            i = i + 1
        file.close()

    targetDir = '/Library/Webserver/Documents/result/{}/report'.format(case_id)
    if not os.path.isdir(targetDir):
        os.makedirs(targetDir)
    copy(file_path, targetDir)
    os.remove(file_path)