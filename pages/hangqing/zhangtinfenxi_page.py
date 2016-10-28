#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "yaosumei@myhexin.com"

from page_object.appium_page_objects import PageObject, page_element

class ZhangtinfenxiPage(PageObject):
    """
    行情－> 沪深－> 涨停分析
    涨停分析页面的相关元素及操作
    """
    fanhui_btn = page_element(accessibility_id = "返回")
    zhangtinfenxi_title = page_element(accessibility_id = "涨停分析")
    sousuo_btn = page_element(accessibility_id = "搜索")

    def hq_up(self):
        """
        向上滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (200 / 375.0)
        start_y = height * (500 / 667.0)
        end_x = width * (200 / 375.0)
        end_y = height * (200 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hq_down(self):
        """
        向下滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (200 / 375.0)
        start_y = height * (200 / 667.0)
        end_x = width * (200 / 375.0)
        end_y = height * (500 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)