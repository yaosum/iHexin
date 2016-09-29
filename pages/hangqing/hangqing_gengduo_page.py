#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

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
    desc_img = page_element(accessibility_id='DescImg')
    asc_img = page_element(accessibility_id='AscImg')

    cell01 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]')

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