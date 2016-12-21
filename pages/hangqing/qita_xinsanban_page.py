#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class QitaXinsanbanPage(PageObject):
    """
    首页－> 行情－> 新三板
    新三板内相关元素与操作
    """
    fanhui_btn = page_element(accessibility_id = '返回')
    sanbanzuoshi_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAButton[1]')
    sanbanchengzhi_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAButton[2]')

    chengfengu_btn = page_element(accessibility_id = '成分股')

    chuangxin_btn = page_element(accessibility_id = '创新')
    jichu_btn = page_element(accessibility_id = '基础')
    zuoshi_btn = page_element(accessibility_id = '做市')
    xieyi_btn = page_element(accessibility_id = '协议')
    youxiangu_btn = page_element(accessibility_id = '优先股')

    group1 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]/UIAButton[1]')
    group2 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[1]')
    group3 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[3]/UIAButton[1]')

    gengduo1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]/UIAButton[2]')
    gengduo2 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[2]')
    gengduo3 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[3]/UIAButton[2]')

    #第一行元素
    cell1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[3]')
    # 更多列表中第一行元素的标题
    cell1_title = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[3]')
    # 成分股－三板成指／三板做市
    sanbanzuoshi_tab = page_element(accessibility_id = "三板做市")
    sanbanchengzhi_tab = page_element(accessibility_id = "三板成指")

    # 成分股列表中第一行元素的标题
    cell01_title_chengfengu = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]")
    cell01_chengfengu_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]")

    def cell01_chengfengu_click(self):
        """
        列表中的元素过多，按照路径不能点击第一行元素，因此使用坐标点击
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (47 / 375.0)
        tap_y = height * (158 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
