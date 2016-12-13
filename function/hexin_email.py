#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib

from email.message import Message
from time import sleep
import email.utils
from email.mime.text import MIMEText
from email.header import Header
import socket

class HexinEmail(object):
    """
    功能:自动发送邮件
    参数说明:
        to_list:收件人邮箱,可以是多个
        cc_list:抄送人邮箱,可以是多个
        rate_list:用例结果统计数据,具体是rate_list[0]---成功率,rate_list[1]---失败率,rate_list[2]重跑率
    """
    def sendEmail(self, to_list, cc_list, rate_list, run_case_id):
        smtpserver = 'mail.myhexin.com'
        username = 'tianmaotao@myhexin.com'
        password = 'tmthd19940404'
        from_addr = 'tianmaotao@myhexin.com'
        to_addr = ''
        cc_addr = ''
        if len(to_list) > 0:
            for add_to in to_list:
                to_addr = to_addr + add_to + ';'
        if len(cc_list) > 0:
            for add_cc in cc_list:
                cc_addr = cc_addr + add_cc + ';'
        content = "你好:\n"
        content = content + "  " + "运行用例ID:" + run_case_id + '\n'
        #用例统计内容拼接
        num = 0
        for n in rate_list:
            num = num + n
        content = content+ "  " +'总用例数:{}'.format(num) + '\n'
        tem_list = ['通过用例数:', '失败用例数:', '重跑用例数:']
        if len(rate_list) > 0:
            i = 0
            for rate in rate_list:
                content = content + "  " + tem_list[i] + "{}".format(rate) + "\n"
                i = i + 1

        #获取本地的ip地址
        localIP = socket.gethostbyname(socket.gethostname())
        content = content + '\n' + "详情请访问:" + "http://" + localIP + "/"

        #签名
        autograph = '-------------------------------------\n' \
                    '该邮件由自动化脚本跑完后自动发送!\n' \
                    '请勿回复!\n' \
                    '有问题请找：田茂涛\n' \
                    '部门：移动互联网事业部iOS组\n' \
                    '电话：13685759479\n' \
                    '邮箱：tianmaotao@myhexin.com\n'

        msg = MIMEText(content + '\n \n'+autograph, 'plain', 'utf-8')
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Cc'] = cc_addr
        msg['Subject'] = Header(u'[自动化测试]测试用例结果邮件', 'utf-8').encode()

        sm = smtplib.SMTP(smtpserver, port=25, timeout=20)
        sm.ehlo()
        sm.starttls()
        sm.ehlo()
        sm.login(username, password)
        try:
            if len(to_list) > 0:
                for add_to in to_list:
                    sm.sendmail(from_addr,add_to, msg.as_string())

            if len(cc_list) > 0:
                for add_cc in cc_list:
                    sm.sendmail(from_addr, add_cc, msg.as_string())

        finally:
            sm.quit()