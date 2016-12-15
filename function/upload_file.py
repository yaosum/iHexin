#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import shutil
from shutil import copy
from hexin_email import HexinEmail
from ..get_project_path import GetProjectPath

class UploadFile(object):
    """
        把最后的结果上传到服务器的documents
    """
    def uploadResult(self, passedList, failedList, rerunList):
        # 读取运行用例id
        sign = "0"
        run_case_id = "9999999"
        file_path =GetProjectPath.getProjectPath() + '/runConf.txt'
        if not os.path.isfile(file_path):
            file = open(file_path, 'w')
            file.write('9999999\n0')
            file.close()
        else:
            file = open(file_path, 'r')
            i = 0
            for line in file.readlines():
                if i == 0:
                    line = line.strip('\n')  # 去掉换行符
                    msg = line
                elif i == 1:
                    line = line.strip('\n')  # 去掉换行符
                    sign = line
                    break
                i = i + 1
            file.close()
            run_case_id = msg

        # 如果不需要把结果上传服务器地址,和发邮件通知,return
        if sign != "1":
            return

        # 把结果上传服务器地址
        # -----成功,失败等数据
        self.resultWriteToTxt(run_case_id=run_case_id, passedList=passedList, failedList=failedList, rerunList=rerunList)
        # -----截图
        screen_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        sourceDir = GetProjectPath.getProjectPath() + '/result/' + screen_date + '/' + run_case_id
        targetDir = '/Library/Webserver/Documents/result/{}/screenshot/'.format(run_case_id)
        if not os.path.isdir(targetDir):
            os.makedirs(targetDir)
        for root, dirs, files in os.walk(sourceDir):
            for i in xrange(0, files.__len__()):
                sf = os.path.join(root, files[i])
                copy(sf, targetDir)

        # ------report报告
        htmlSourceDir = GetProjectPath.getProjectPath() + "/report.html"
        htmlTargetDir = '/Library/Webserver/Documents/result/{}/report'.format(run_case_id)
        if not os.path.isdir(htmlTargetDir):
            os.makedirs(htmlTargetDir)
        copy(htmlSourceDir, htmlTargetDir)

        # ------pytest生成的,与report相关的文件(如:网页的格式,错误截图)
        assertTargetDir = htmlTargetDir + "/assets"
        if not os.path.isdir(assertTargetDir):
            os.makedirs(assertTargetDir)
        assetsSourceDir = GetProjectPath.getProjectPath() + "/assets"
        filelist = []
        filelist = os.listdir(assetsSourceDir)
        for f in filelist:
            filepath = os.path.join(assetsSourceDir, f)
            if os.path.isfile(filepath):
                copy(filepath, assertTargetDir)
                os.remove(filepath)
            elif os.path.isdir(filepath):
                copy(filepath, assertTargetDir)
                shutil.rmtree(filepath, True)

        # 发邮件通知
        hexin_email = HexinEmail()
        # 用例统计数据
        rate_list = []
        rate_list.append(len(passedList))
        rate_list.append(len(failedList))
        rate_list.append(len(rerunList))
        # 注意:如果收件人和抄送人邮件拼错,会导致发送全部失败
        to_list = ["tianmaotao@myhexin.com"]
        cc_list = ["huguozhu@myhexin.com","xiaoshaoqing@myhexin.com","liuhaoyu@myhexin.com","yecuiqing@myhexin.com","zhaojunchuan@myhexin.com","tianmaotao@myhexin.com"]
        hexin_email.sendEmail(to_list=to_list, cc_list=cc_list, rate_list=rate_list, run_case_id=run_case_id)

    """
        把统计的成功数,失败数,重跑数数据写入txt文件并上传服务器地址
    """
    def resultWriteToTxt(self, run_case_id, passedList, failedList, rerunList):
        file_path = GetProjectPath.getProjectPath() + '/statistics.txt'
        file = open(file_path, 'w')
        if os.path.isfile(file_path):
            file.write("{}\n".format(len(passedList)))
            file.write("{}\n".format(len(failedList)))
            file.write("{}\n".format(len(rerunList) - len(failedList)))
            file.close()
        else:
            i = 0
            for line in file.readlines():
                if i == 0:
                    str = line
                    s = line.replace(str, "{}".format(len(passedList)))
                    file.writelines(s)
                if i == 1:
                    str = line
                    s = line.replace(str, "{}".format(len(failedList)))
                    file.writelines(s)
                if i == 2:
                    str = line
                    s = line.replace(str, "{}".format(len(rerunList)))
                    file.writelines(s)
                i = i + 1
            file.close()

        targetDir = '/Library/Webserver/Documents/result/{}/report'.format(run_case_id)
        if not os.path.isdir(targetDir):
            os.makedirs(targetDir)
        copy(file_path, targetDir)
        os.remove(file_path)