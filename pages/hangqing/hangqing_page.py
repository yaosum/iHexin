#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao@myhexin.com"

from page_object.appium_page_objects import PageObject, page_element

class HangqingPage(PageObject):
    """
    行情页面的相关元素及操作
    """
    guzhi_btn = page_element(accessibility_id = '股指')
    hushen_btn = page_element(accessibility_id = '沪深')
    bankuai_btn = page_element(accessibility_id = '板块')
    gangmeigu_btn = page_element(accessibility_id = '港美股')
    qita_btn = page_element(accessibility_id = '其他')