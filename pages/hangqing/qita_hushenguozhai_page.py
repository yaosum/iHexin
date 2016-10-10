#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class QitaHushenguozhai(PageObject):
    fanhui_btn = page_element(accessibility_id = '返回')
    hushi_btn = page_element(accessibility_id = '')
    shenshi_btn = page_element(accessibility_id = '')
    cell1 = page_element(xpath = '')
