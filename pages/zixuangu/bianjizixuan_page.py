#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "wangminghai@myhexin.com"

from appium.webdriver.common.touch_action import TouchAction

from page_object.appium_page_objects import PageObject, page_element

class BianjizixuanPage(PageObject):
    """
    首页－> 自选－> 编辑自选
    编辑自选页面相关元素和操作
    """
    fanhui_button = page_element(accessibility_id = "返回")
    bianjizixuan_StaticText = page_element(xpath="//UIAStaticText[@name='编辑自选']")
    tianjiagupiao_button = page_element(accessibility_id = "添加股票")

    shanchu_button = page_element(accessibility_id = "删除自选")

    THS_staText = page_element(xpath="//UIATableCell[@name='同花顺']")
    PFYH_staText = page_element(xpath="//UIATableCell[@name='浦发银行']")

    cell001 = page_element(xpath="//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]")
    cell002 = page_element(xpath="//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]")
    cell003 = page_element(xpath="//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]")

    cell001_btn = page_element(xpath="//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]")
    cell002_btn = page_element(xpath="//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAButton[1]")
    cell003_btn = page_element(xpath="//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[1]")

    #某行元素的股票名称
    cell001_stock_staText = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]")
    cell002_stock_staText = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[1]")
    cell003_stock_staText = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAStaticText[1]")
    cell018_stock_staText = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[18]/UIAStaticText[1]")

    #置顶按钮
    cell018_zhiding_btn = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[18]/UIAButton[2]')
    cell019_zhiding_btn = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[19]/UIAButton[2]')
    cell010_zhiding_btn = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[10]/UIAButton[2]')
    #拖动按钮
    cell001_tuodong_btn = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[4]')
    cell002_tuodong_btn = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAButton[4]')
    cell003_tuodong_btn = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[4]')

    def hx_upglide(self):
        """
        在编辑自选界面进行上滑操作
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (285 / 375.0)
        start_y = height * (550 / 667.0)
        end_x = width * (285 / 375.0)
        end_y = height * (108 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hx_glide(self):
        """
        在编辑自选界面进行下滑操作
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (285 / 375.0)
        start_y = height * (108 / 667.0)
        end_x = width * (285 / 375.0)
        end_y = height * (550 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hx_drag_and_drop(self, origin_el, destination_el):
        """
        在编辑自选界面进行拖拽操作
        :return:
        """
        action1 = TouchAction(self)
        action1.press(origin_el).wait(100).move_to(destination_el).wait(100).release()
        action1.perform()






