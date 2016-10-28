#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "yaosumei@myhexin.com"

from page_object.appium_page_objects import PageObject, page_element

class GanggutongPage(PageObject):
    """
    行情－ 港美股－ 港股－ 港股通
    港股通页面内相关元素及其操作
    """
    ganggutong_title = page_element(accessibility_id = "港股通")
    fanhui_btn = page_element(accessibility_id = "返回")

    def cell01_click(self):
        """
        点击港股通列表第一行元素
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (48 / 375.0)
        tap_y = height * (175 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
