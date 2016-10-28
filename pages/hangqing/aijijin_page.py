#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "yaosumei@myhexin.com"

from page_object.appium_page_objects import PageObject, page_element

class LovejijinPage(PageObject):
    """
    首页－> 行情－> 其他－> 同花顺爱基金
    同花顺爱基金SDK内相关元素
    """
    fanhui_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]')

    shouyipaihang_text = page_element(accessibility_id = '收益排行')

    aijijin_text = page_element(accessibility_id = '爱基金')