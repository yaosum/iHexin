#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao@myhexin.com"

from page_object.appium_page_objects import PageObject, page_element

class BankuaiPage(PageObject):
    """
    首页－> 行情－> 板块
    板块页面内相关元素与操作
    """
    group1_btn = page_element(accessibility_id = '行业板块')
    group2_btn = page_element(accessibility_id = '概念板块')

    #板块更多按钮
    hy_gengduo_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]/UIAButton[2]')
    gn_gengduo_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[2]')

    #每个板块下的第一行元素及其对应的股票名称
    cell1_1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')
    cell1_1_title = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[2]')
    cell2_1 = page_element(
        xpath = ' //UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[6]/UIAStaticText[1]')
    cell2_1_title = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[6]/UIAStaticText[2]')