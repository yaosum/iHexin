#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page_object.appium_page_objects import PageObject, page_element

class GerenzhongxinPage(PageObject):
    """
    未登录时的个人中心页面
    """
    # denglu_zhuce_btn = page_element(accessibility_id = '登录/注册')
    denglu_zhuce_btn = page_element(
        xpath = ' //UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[2]')
    # tuichudenglu_btn = page_element(accessibility_id = "退出账号")
    tuichudenglu_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[18]")
    # 提示框
    tishi_allert = page_element(xpath = "//UIAAlert[@name='提示']")
    quedin_btn = page_element(xpath = "//UIAButton[@name='确定']")
    quxiao_btn = page_element(xpath="//UIAButton[@name='取消']")


