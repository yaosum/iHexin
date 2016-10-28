#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class GuzhiQihuoGengduoPage(PageObject):
    """
    行情－> 股指－> 股指期货更多
    股指期货更多页面相关元素及操作
    """
    fanhui_btn = page_element(accessibility_id = '返回')

    hushen300_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableGroup[1]/UIAButton[1]')
    shangzheng50_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableGroup[2]/UIAButton[1]')
    zhongzheng500_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableGroup[3]/UIAButton[1]')

    #当表示图点击隐藏按钮后,这个单元格查找到的元素未可见的第一个单元格
    cell1_1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableCell[1]')
    cell1_1_title = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')
    cell2_1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableCell[10]')
    cell3_1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableCell[19]')
