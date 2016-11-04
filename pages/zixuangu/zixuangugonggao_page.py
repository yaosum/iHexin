#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class ZixuangugonggaoPage(PageObject):
    """
    自选－> 自选股公告
    自选股公告页面的相关元素及操作
    """
    fanhui_btn = page_element(accessibility_id = '返回')
    zixuangugonggao_staText = page_element(xpath = "//UIAStaticText[@name= '自选股公告']")

    gonggao_bankuai1_staText = page_element(xpath = "//UIAStaticText[@name= '板块1公告']")
    gonggao_bankuai2_staText = page_element(xpath = "//UIAStaticText[@name= '板块2公告']")
    gonggao_bankuai3_staText = page_element(xpath = "//UIAStaticText[@name= '板块3公告']")
    gonggao_bankuai4_staText = page_element(xpath = "//UIAStaticText[@name= '板块4公告']")
    gonggao_bankuai5_staText = page_element(xpath = "//UIAStaticText[@name= '板块5公告']")
    gonggao_bankuai6_staText = page_element(xpath = "//UIAStaticText[@name= '板块6公告']")
    gonggao_bankuai7_staText = page_element(xpath = "//UIAStaticText[@name= '板块7公告']")
    gonggao_bankuai8_staText = page_element(xpath = "//UIAStaticText[@name= '板块8公告']")

    cell01 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]')

    def hx_upglide(self):
        """
        向上滑动
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (85 / 375.0)
        start_y = height * (584 / 667.0)
        end_x = width * (85 / 375.0)
        end_y = height * (112 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hx_downglide(self):
        """
        向下滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (85 / 375.0)
        start_y = height * (112 / 667.0)
        end_x = width * (85 / 375.0)
        end_y = height * (584 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

