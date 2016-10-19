#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

"""
行情页面,所有进入更多页面,需要查找的元素和操作放在此类(除了一些特殊的)。
"""
from page_object.appium_page_objects import PageObject, page_element

class HangqingGengduoPage(PageObject):
    fanhui_btn = page_element(accessibility_id = '返回')
    zuixin_btn = page_element(accessibility_id = '最新')
    zhangfu_btn = page_element(accessibility_id = '涨幅')
    zhangdie_btn = page_element(accessibility_id = '涨跌')
    xingji_btn = page_element(accessibility_id = '星级')
    zhangfu5_btn = page_element(accessibility_id = '5日涨幅')
    huanshou_btn = page_element(accessibility_id = '换手')
    liangbi_btn = page_element(accessibility_id = '量比')
    zhenfu_btn = page_element(accessibility_id = '振幅')
    zhangsu_btn = page_element(accessibility_id = '涨速')
    shiying_btn = page_element(accessibility_id = '市盈(动)')
    shijinglv_btn = page_element(accessibility_id = '市净率')
    liutong_btn = page_element(accessibility_id = '流通市值')
    jine_btn = page_element(accessibility_id = '金额')
    zongshizhi_btn = page_element(accessibility_id = '总市值')
    zongshou_btn = page_element(accessibility_id = '总手')
    xianshou_btn = page_element(accessibility_id = '现手')

    chengjiaoliang_btn = page_element(accessibility_id = '成交量')
    chengjiaoe_btn = page_element(accessibility_id = '成交额')
    desc_img = page_element(accessibility_id='DescImg')
    asc_img = page_element(accessibility_id='AscImg')

    qita_50ETF_btn = page_element(accessibility_id= '50ETF')
    kaipan_btn = page_element(accessibility_id= '开盘')
    zuoshou_btn = page_element(accessibility_id= '昨收')
    zuigao_btn = page_element(accessibility_id= '最高')
    zuidi_btn = page_element(accessibility_id= '最低')
    weibi_btn = page_element(accessibility_id= '委比')
    zuojiesuan_btn = page_element(accessibility_id= '昨结算')
    chicangliang_btn = page_element(accessibility_id= '持仓量')

    #新三板的
    sanbanzuoshi_btn = page_element(accessibility_id= '三板做市')
    sanbanchengzhi_btn =  page_element(accessibility_id= '三板成指')

    cell01 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]')
    cell01_title = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')

    #行情里边每个分组进入页面后的操作不一样
    def bk_clickOperation(self):
        self.zongshou_btn.click()
        assert self.desc_img
        self.zongshou_btn.click()
        assert self.asc_img
        self.jine_btn.click()
        assert self.desc_img
        self.jine_btn.click()
        assert self.asc_img
        self.zuixin_btn.click()
        assert self.desc_img
        self.zuixin_btn.click()
        assert self.asc_img
        self.huanshou_btn.click()
        assert self.desc_img
        self.huanshou_btn.click()
        assert self.asc_img
        self.zhangfu5_btn.click()
        assert self.desc_img
        self.zhangfu5_btn.click()
        assert self.asc_img
        self.zhangfu_btn.click()
        assert self.desc_img
        self.zhangfu_btn.click()
        assert self.asc_img

    #港媒股里边行业板块点击单元格后,再点击查看更多数据页面操作
    def hybk_clickOperation(self):
        self.hq_left()
        self.chengjiaoe_btn.click()
        self.chengjiaoe_btn.click()
        self.chengjiaoliang_btn.click()
        self.chengjiaoliang_btn.click()
        self.zhangdie_btn.click()
        self.zhangdie_btn.click()
        self.zhangfu_btn.click()
        self.zhangfu_btn.click()
        self.zuixin_btn.click()
        self.zuixin_btn.click()
        self.hq_up()
        self.hq_down()

    #其他
    #股票期权
    def qita_gpqq_clickOperation(self):
        self.zhenfu_btn.click()
        self.zhenfu_btn.click()
        self.weibi_btn.click()
        self.weibi_btn.click()
        self.zuidi_btn.click()
        self.zuidi_btn.click()
        self.zuigao_btn.click()
        self.zuigao_btn.click()
        self.zuoshou_btn.click()
        self.zuoshou_btn.click()
        #self.kaipan_btn.click()
        #self.kaipan_btn.clicK()
        self.xianshou_btn.click()
        self.xianshou_btn.click()
        self.shijinglv_btn.click()
        self.shijinglv_btn.click()
        self.shiying_btn.click()
        self.shiying_btn.click()
        self.liangbi_btn.click()
        self.liangbi_btn.click()
        self.huanshou_btn.click()
        self.huanshou_btn.click()
        self.zongshou_btn.click()
        self.zongshou_btn.click()
        self.zhangsu_btn.click()
        self.zhangsu_btn.click()
        self.zhangdie_btn.click()
        self.zhangdie_btn.click()
        self.zhangfu_btn.click()
        self.zhangfu_btn.click()
        self.zuixin_btn.click()
        self.zuixin_btn.click()
    #上海黄金
    def shhj_clickOperation(self):
        self.zuojiesuan_btn.click()
        self.zuojiesuan_btn.click()
        self.chicangliang_btn.click()
        self.chicangliang_btn.click()
        self.zongshou_btn.click()
        self.zongshou_btn.click()
        self.zhangdie_btn.click()
        self.zhangdie_btn.click()
        self.zhangfu_btn.click()
        self.zhangfu_btn.click()
        self.zuixin_btn.click()
        self.zuixin_btn.click()
    #基金(包括沪深封闭基金),以及个股里的除了新三板的其它股
    def jijin_clickOperation(self):
        self.xianshou_btn.click()
        self.xianshou_btn.click()
        self.zongshou_btn.click()
        self.zongshou_btn.click()
        self.jine_btn.click()
        self.jine_btn.click()
        self.zongshizhi_btn.click()
        self.zongshizhi_btn.click()
        self.liutong_btn.click()
        self.liutong_btn.click()
        self.shijinglv_btn.click()
        self.shijinglv_btn.click()
        self.shiying_btn.click()
        self.shiying_btn.click()
        self.zhangsu_btn.click()
        self.zhangsu_btn.click()
        self.zhenfu_btn.click()
        self.zhenfu_btn.click()
        self.liangbi_btn.click()
        self.liangbi_btn.click()
        self.huanshou_btn.click()
        self.huanshou_btn.click()
        self.xingji_btn.click()
        self.xingji_btn.click()
        self.zhangdie_btn.click()
        self.zhangdie_btn.click()
        self.zhangfu_btn.click()
        self.zhangfu_btn.click()
        self.zuixin_btn.click()
        self.zuixin_btn.click()

    #沪深
    def hs_clickOperation(self):
        self.xianshou_btn.click()
        assert self.desc_img
        self.xianshou_btn.click()
        assert self.asc_img
        self.zongshou_btn.click()
        assert self.desc_img
        self.zongshou_btn.click()
        assert self.asc_img
        #self.jine_btn.clcik()
        #assert self.desc_img
        #self.jine_btn.clcik()
        #assert self.asc_img
        self.zongshizhi_btn.click()
        assert self.desc_img
        self.zongshizhi_btn.click()
        assert self.asc_img
        self.liutong_btn.click()
        assert self.desc_img
        self.liutong_btn.click()
        assert self.asc_img
        self.shijinglv_btn.click()
        assert self.desc_img
        self.shijinglv_btn.click()
        assert self.asc_img
        self.shiying_btn.click()
        assert self.desc_img
        self.shiying_btn.click()
        assert self.asc_img
        self.zhangsu_btn.click()
        assert self.desc_img
        self.zhangsu_btn.click()
        assert self.asc_img
        self.zhenfu_btn.click()
        assert self.desc_img
        self.zhenfu_btn.click()
        assert self.asc_img
        self.liangbi_btn.click()
        assert self.desc_img
        self.liangbi_btn.click()
        assert self.asc_img
        self.huanshou_btn.click()
        assert self.desc_img
        self.huanshou_btn.click()
        assert self.asc_img
        self.xingji_btn.click()
        assert self.desc_img
        self.xingji_btn.click()
        assert self.asc_img
        self.zhangdie_btn.click()
        assert self.desc_img
        self.zhangdie_btn.click()
        assert self.asc_img
        self.zhangfu_btn.click()
        assert self.desc_img
        self.zhangfu_btn.click()
        assert self.asc_img
        self.zuixin_btn.click()
        assert self.desc_img
        self.zuixin_btn.click()
        assert self.asc_img
    #港股通
    def ganggutong_clickOperation(self):
        self.zuixin_btn.click()
        self.zuixin_btn.click()
        self.zhangfu_btn.click()
        self.zhangfu_btn.click()
        self.zhangdie_btn.click()
        self.zhangdie_btn.click()

    def hq_right(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (240 / 375.0)
        start_y = height * (350 / 667.0)
        end_x = width * (340 / 375.0)
        end_y = height * (350 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hq_left(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (350 / 375.0)
        start_y = height * (350 / 667.0)
        end_x = width * (240 / 375.0)
        end_y = height * (350 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hq_up(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (200 / 375.0)
        start_y = height * (500 / 667.0)
        end_x = width * (200 / 375.0)
        end_y = height * (200 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hq_down(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (200 / 375.0)
        start_y = height * (200 / 667.0)
        end_x = width * (200 / 375.0)
        end_y = height * (500 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)