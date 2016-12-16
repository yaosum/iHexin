#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import types

class GetConfigureData(object):
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
        if row <= nrows and col <= ncols:
            # 获取指定行列数据
            cell_A1 = sh.cell(row, col).value
            return cell_A1
        else:
            return ""

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