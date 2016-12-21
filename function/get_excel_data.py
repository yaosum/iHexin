#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import types

class GetExcelData(object):
    """
    功能:读取xls文件的内容
    参数:
        row:需要读取的数据的行位置
        col:需要读取的数据的列位置
    """
    def readXls(self, row, col):
        name = "configure.xls"
        xls = xlrd.open_workbook(name)
        shxrange = range(xls.nsheets)
        sh = ""
        try:
            sh = xls.sheet_by_name("test")
        except:
            print "no sheet in %s named Sheet1" % name
        # 获取行数
        nrows = sh.nrows
        # 获取列数
        ncols = sh.ncols
        try:
            if row <= nrows and col <= ncols:
                # 获取指定行列数据
                cell_A1 = sh.cell(row, col).value
                return cell_A1
            else:
                return ''
        except:
            return ''

    """
    功能:获取运行用例的ID
    """
    def getRunCaseId(self):
        #取出来的是float转换字符串
        f = self.readXls(row=1, col=1)
        if type(f) is types.FloatType:
            s = '{}'.format(f)
        else:
            s = f
        l = s.split('.')
        return l[0]

    """
    功能:获取是否把结果上传服务器地址的标识
    """
    def getUploadFileFlag(self):
        f = self.readXls(row=2, col=1)
        if type(f) is types.FloatType:
            s = '{}'.format(f)
        else:
            s = f
        l = s.split('.')
        return l[0]

    """
    功能:获取是否自动发送email的标识
    """
    def getSendEmailFlag(self):
        f = self.readXls(row=3, col=1)
        if type(f) is types.FloatType:
            s = '{}'.format(f)
        else:
            s = f
        l = s.split('.')
        return l[0]

    """
    功能:获取收件人
    """
    def getToList(self):
        s = self.readXls(row=4, col=1)
        l = s.split(',')
        list = self.listString(l)
        return list

    """
    功能:获取抄送人
    """

    def getCcList(self):
        s = self.readXls(row=5, col=1)
        l = s.split(',')
        list = self.listString(l)
        return list

    """
    功能:因为从excel上面拿到的邮箱,字符串前面都带一个u,也就是python2.x 里unicode字符串需要在字符串前加u来表示,所以转换一下
    """
    def listString(self, list):
        result = []
        for tep in list:
            str = "{}".format(tep)
            result.append(str)
        return result

    """
    功能:获取重跑数
    """
    def getRerun(self):
        if self.readXls(row=11, col=1) != '':
            rerun =self.readXls(row=11, col=1)
            return rerun

    """
    功能:获取pytest相关的配置信息。如:bundleid,手机型号,手机系统。。。。
    return:pytest启动的命令字符串
    """
    def pytestConfigure(self):
        # 取出来的是float转换字符串
        f = self.readXls(row=6, col=1)
        if type(f) is types.FloatType:
            s = '{}'.format(f)
        else:
            s = f
        if s != "":
            platform_version = ' --platform_version=\'' + s + '\''
        else:
            platform_version = ''
        if self.readXls(row=7, col=1) != "":
            device_name = ' --device_name=\'' + self.readXls(row=7, col=1) + '\''
        else:
            device_name = ''
        if self.readXls(row=8, col=1) != "":
            device_udid = ' --device_udid=\'' + self.readXls(row=8, col=1) + '\''
        else:
            device_udid = ''
        if self.readXls(row=9, col=1) != "":
            bundle_id = ' --bundle_id=\'' + self.readXls(row=9, col=1) + '\''
        else:
            bundle_id = ''
        if self.readXls(row=10, col=1) != "":
            repeat = ' --count=' + "{}".format(int(self.readXls(row=10, col=1)))
        else:
            repeat = ''
        if self.readXls(row=11, col=1) != '':
            rerun =' --rerun=' + "{}".format(int(self.readXls(row=11, col=1)))
        else:
            rerun = ''
        #pytest启动的命令字符串
        run_str = 'py.test --platform_name=\'iOS\' --html=report.html --junitxml=report.xml'+ platform_version + device_udid + device_name + bundle_id + rerun + repeat
        print(run_str)
        return run_str

    """
    功能:获取运行用例模块备注信息
    """
    def readModularCase(self):
        str = self.readXls(row=12, col=1)
        if str != "":
            return str
        else:
            return "没有填写"
    """
    功能:获取手机和包相关的信息
    return:一个list
    """
    def getCaseInfo(self):
        result_list = []

        # 手机的型号
        if self.readXls(row=7, col=1) != "":
            iPhone_name = "手机型号:"+str(self.readXls(row=7, col=1))
            result_list.append(iPhone_name)

        # 系统版本
        f = self.readXls(row=6, col=1)
        if type(f) is types.FloatType:
            s = '{}'.format(f)
        else:
            s = f
        if s != "":
            iPhone_version = "系统版本:"+s
            result_list.append(iPhone_version)

        #rerun
        if self.readXls(row=11, col=1) != '':
            rerun = "重跑次数:" + "{}".format(self.readXls(row=11, col=1))
            result_list.append(rerun)

        #repeat
        if self.readXls(row=10, col=1) != "":
            repeat = "运行次数:" + "{}".format(self.readXls(row=10, col=1))
            result_list.append(repeat)

        # bundle id
        if self.readXls(row=9, col=1) != "":
            bundle_id = "bundleid: " + self.readXls(row=9, col=1)
            result_list.append(bundle_id)

        # device_udid
        if self.readXls(row=8, col=1) != "":
            device_udid = "udid: " + self.readXls(row=8, col=1)
            result_list.append(device_udid)

        return result_list