#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class GuzhiQihuoGengduoPage(PageObject):
    fanhui_btn = page_element(accessibility_id = '返回')
    hushen300_btn = page_element(accessibility_id = '沪深300')
    shangzheng50 = page_element(accessibility_id = '上证50')
    zhongzheng500 = page_element(accessibility_id = '中证500')

    cell1_1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableCell[1]/UIAElement[1]')
    cell2_1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableCell[10]/UIAElement[1]')
    cell3_1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableCell[19]/UIAElement[1]')
