#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class ZixuanDapanPage(PageObject):
    """
    自选－> 大盘
    大盘的相关操作
    """
    hu_btn = page_element(accessibility_id = "btn hu")
    shen_btn = page_element(accessibility_id = "btn shen")
    chuang_btn = page_element(accessibility_id = "btn chuang")

    fenshitu_scr = page_element(xpath= "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]")

    def hx_left(self):
        """
        向左滑动至k线
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (210 / 375.0)
        start_y = height * (239 / 667.0)
        end_x = width * (45 / 375.0)
        end_y = height * (239 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hx_right(self):
        """
        向右滑动至分时
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (39 / 375.0)
        start_y = height * (239 / 667.0)
        end_x = width * (236 / 375.0)
        end_y = height * (239 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hx_tapblank(self):
        """
        点击大盘外的下方空白处
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (188 / 375.0)
        tap_y = height * (480 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})

