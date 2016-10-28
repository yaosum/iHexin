#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "yaosumei@myhexin.com"

from page_object.appium_page_objects import PageObject, page_element

class AHBijiaguPage(PageObject):
    """
    行情－> 沪深－> AH比价
    ah比价股页面的相关元素与操作
    """
    ahbijia_title = page_element(accessibility_id = "AH股比价")
    shuaxin_btn = page_element(accessibility_id = "刷新")
    sousuo_btn = page_element(accessibility_id = "搜索")
    fanhui_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]")

    #列表头
    zuixin_btn = page_element(accessibility_id = "   最新")
    zhangfu_btn = page_element(accessibility_id = "   涨幅")
    yijialv_btn = page_element(accessibility_id = "溢价率")

    xiaochuwenben_btn = page_element(accessibility_id = "AH tips close")
    wenben_text = page_element(accessibility_id="AH股溢价率是指同时有A股和H股的上市公司，两地股价经汇率换算后的价格差值比率。")

    #第一行元素及其股票名称
    cell01_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]")
    cell01_title = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[1]')

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