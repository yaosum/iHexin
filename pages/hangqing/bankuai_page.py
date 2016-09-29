#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class BankuaiPage(PageObject):
    group1_btn = page_element(accessibility_id = '行业版块')
    group2_btn = page_element(accessibility_id = '概念版块')

    hy_gengduo_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]/UIAButton[2]')
    gn_gengduo_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[2]')

    cell1_1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')
    cell2_1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[6]/UIAStaticText[1]')