#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.header import Header
import socket
import urllib2
import urllib
import json

class HexinEmail(object):
    """
    功能:自动发送邮件
    参数说明:
        to_list:收件人邮箱,可以是多个
        cc_list:抄送人邮箱,可以是多个
        rate_list:用例结果统计数据,具体是rate_list[0]---成功率,rate_list[1]---失败率,rate_list[2]重跑率
        sm.sendmail(from_addr, add_cc, msg.as_string())
    """
    def sendEmail(self, to_list, cc_list, rate_list, run_case_id):
        content = "&nbsp;&nbsp;&nbsp;" + "run_case_ID:&nbsp;" + run_case_id + '<br />'
        #用例统计内容拼接
        num = rate_list[0] + rate_list[1]
        content = content+ "&nbsp;&nbsp;&nbsp;" +'total:&nbsp;{}'.format(num) + '<br />'
        tem_list = ['passed:&nbsp;', 'failed:&nbsp;', 'rerun:&nbsp;']
        if len(rate_list) > 0:
            i = 0
            for rate in rate_list:
                content = content + "&nbsp;&nbsp;&nbsp;" + tem_list[i] + "{}".format(rate) + "&nbsp;&nbsp;&nbsp;"
                i = i + 1

        #获取本地的ip地址
        localIP = socket.gethostbyname(socket.gethostname())
        content = content + '<br /><br />' + "URL:&nbsp&nbsp" + "http://" + localIP + "/"

        #签名
        autograph = '<br />-------------------------------------<br />/*<br />' \
                    '*If you have any problems, please ask for tianmaotao. <br />' \
                    '*tel: 13685759479<br />' \
                    '*email: tianmaotao@myhexin.com<br />' \
                    '*This email is automatically sent by the script.<br />' \
                    '*Do not reply!<br />*/' \

        # 定义一个要提交的数据数组(字典)
        data = {}
        data['recv'] = json.dumps(to_list)
        data['cc'] = json.dumps(cc_list)
        data['content'] = unicode(content + '\n \n'+autograph, 'utf-8')
        data['fromname'] = 'automation@myhexin.com'
        data['isall'] = 1
        data['subject'] = Header(u'[自动化测试]测试用例结果邮件', 'utf-8').encode()
        # 定义post的地址
        url = 'http://183.131.12.178/sendmail/send.php'
        post_data = urllib.urlencode(data)
        # 提交，发送数据
        req = urllib2.urlopen(url, post_data)
        # 获取提交后返回的信息
        content = req.read()