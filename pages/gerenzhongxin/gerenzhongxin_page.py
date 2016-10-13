#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page_object.appium_page_objects import PageObject, page_element

class GerenzhongxinPage(PageObject):
    #denglu_zhuce_btn = page_element(accessibility_id = '登录/注册')
    denglu_zhuce_btn = page_element(xpath = ' //UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[2]')