#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class GengduoPage3(PageObject):
    zuixin_btn = page_element(accessibility_id = '最新')
    zhangfu_btn = page_element(accessibility_id = '涨幅')
    zhangdie_btn = page_element(accessibility_id = '涨跌')

    cell01 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]')