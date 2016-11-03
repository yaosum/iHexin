#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page_object.appium_page_objects import PageObject, page_element

class FenshikxianLungutangPage(PageObject):
    """
        分时k线页面---论股堂页面的一些操作及元素查找
    """

    fanhui_button = page_element(accessibility_id = '返回')
    xuantie_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]')

    zuixintiezi_btn = page_element(accessibility_id = '最新帖子')
    zuiretiezi_btn = page_element(accessibility_id = '最热帖子')