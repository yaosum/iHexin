#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import shutil
from shutil import copy
from hexin_email import HexinEmail
from ..get_project_path import GetProjectPath
from get_excel_data import GetExcelData

class UploadFile(object):
    """
        把最后的结果上传到服务器的documents
    """
    def uploadResult(self, passedList, failedList, rerunList):
        # 读取运行用例id
        getExcelData = GetExcelData()
        run_case_id = getExcelData.getRunCaseId()
        uploadFileFlag = getExcelData.getUploadFileFlag()
        sendEmailFlag = getExcelData.getSendEmailFlag()
        # 如果不需要把结果上传服务器地址,和发邮件通知,return
        if uploadFileFlag == "1":
            # 把结果上传服务器地址
            # -----成功,失败等数据
            self.resultWriteToTxt(run_case_id=run_case_id, passedList=passedList, failedList=failedList,
                                  rerunList=rerunList)
            # -----运行用例的备注信息,也就是运行的模块
            self.readModularCaseTxt(run_case_id=run_case_id)
            # -----手机,程序的相关信息
            self.uploadCaseInfo(run_case_id=run_case_id)
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
        if sendEmailFlag == "1":
            # 发邮件通知
            hexin_email = HexinEmail()
            # 用例统计数据
            rate_list = []
            rerun = getExcelData.getRerun()
            rate_list.append(len(passedList))
            rate_list.append(len(failedList))
            if rerun > 0:
                rate_list.append(len(rerunList) - len(failedList)*rerun)
            else:
                rate_list.append(0)
            # 注意:如果收件人和抄送人邮件拼错,会导致发送全部失败
            to_list = getExcelData.getToList()
            cc_list = getExcelData.getCcList()
            # cc_list = ["huguozhu@myhexin.com","xiaoshaoqing@myhexin.com","liuhaoyu@myhexin.com","yecuiqing@myhexin.com","zhaojunchuan@myhexin.com","tianmaotao@myhexin.com"]
            hexin_email.sendEmail(to_list=to_list, cc_list=cc_list, rate_list=rate_list, run_case_id=run_case_id)

    """
        把统计的成功数,失败数,重跑数数据写入txt文件并上传服务器地址
    """
    def resultWriteToTxt(self, run_case_id, passedList, failedList, rerunList):
        file_path = GetProjectPath.getProjectPath() + '/temFile/statistics.txt'
        getExcelData = GetExcelData()
        rerun  = getExcelData.getRerun()
        file = open(file_path, 'w')
        if not os.path.isfile(file_path):
            file.write("{}\n".format(len(passedList)))
            file.write("{}\n".format(len(failedList)))
            if rerun > 0:
                file.write("{}\n".format(len(rerunList)))
            else:
                file.write("{}\n".format(0))
            file.close()
        else:
            file.truncate()
            file.write("{}\n".format(len(passedList)))
            file.write("{}\n".format(len(failedList)))
            if rerun > 0:
                file.write("{}\n".format(len(rerunList)))
            else:
                file.write("{}\n".format(0))
            file.close()

        targetDir = '/Library/Webserver/Documents/result/{}/report'.format(run_case_id)
        if not os.path.isdir(targetDir):
            os.makedirs(targetDir)
        copy(file_path, targetDir)

    """
    功能:把运行用例模块备注信息上传
    """
    def readModularCaseTxt(self, run_case_id):
        getExcelData = GetExcelData()
        str = getExcelData.readModularCase()
        str.encode('utf-8')
        file_path = GetProjectPath.getProjectPath() + '/temFile/modularCase.txt'
        file = open(file_path, 'w')
        if not os.path.isfile(file_path):
            file.write("{}\n".format(str))
            file.close()
        else:
            file.truncate()
            file.write("{}\n".format(str))
            file.close()

        targetDir = '/Library/Webserver/Documents/result/{}/report'.format(run_case_id)
        if not os.path.isdir(targetDir):
            os.makedirs(targetDir)
        copy(file_path, targetDir)

    """
    功能:把手机和程序相关的信息上传服务器地址
    """
    def uploadCaseInfo(self, run_case_id):
        getExcelData = GetExcelData()
        info_list = getExcelData.getCaseInfo()
        if len(info_list) > 0:
            file_path = GetProjectPath.getProjectPath() + '/temFile/caseInfo.txt'
            file = open(file_path, 'w')
            if not os.path.isfile(file_path):
                for n in info_list:
                    file.write("{}\n".format(n))
                file.close()
            else:
                file.truncate()
                for n in info_list:
                    file.write("{}\n".format(n))
                file.close()
            targetDir = '/Library/Webserver/Documents/result/{}/report'.format(run_case_id)
            if not os.path.isdir(targetDir):
                os.makedirs(targetDir)
            copy(file_path, targetDir)