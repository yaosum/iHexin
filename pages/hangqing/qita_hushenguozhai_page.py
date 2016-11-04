#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class QitaHushenguozhai(PageObject):
    """
    行情－> 其他－> 放贷宝
    放贷宝页面的相关元素及操作
    """
    fanhui_btn = page_element(accessibility_id = '返回')
    hushi_btn = page_element(accessibility_id = '沪市（10万起）')
    shenshi_btn = page_element(accessibility_id = '深市（1千起）')
    cell1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]')
    cell1_title = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')
