#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class GengduoPage7(PageObject):
    fanhui_btn = page_element(accessibility_id = '返回')
    zuixin_btn = page_element(accessibility_id = '最新')
    zhangfu_btn = page_element(accessibility_id = '涨幅')
    zhangdie_btn = page_element(accessibility_id = '涨跌')
    liangbi_btn = page_element(accessibility_id = '量比')
    zhenfu_btn = page_element(accessibility_id = '振幅')
    jine_btn = page_element(accessibility_id = '金额')
    zongshou_btn = page_element(accessibility_id = '总手')

    cell01 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]')

    def gd_right(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (240 / 375.0)
        start_y = height * (350 / 667.0)
        end_x = width * (340 / 375.0)
        end_y = height * (350 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def gd_left(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (350 / 375.0)
        start_y = height * (350 / 667.0)
        end_x = width * (240 / 375.0)
        end_y = height * (350 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)