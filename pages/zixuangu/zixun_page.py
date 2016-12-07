#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class ZixunPage(PageObject):
    """
    某条研报/新闻/公告详情页
    研报具体页面的相关元素
    """
    fanhui_btn = page_element(accessibility_id = '返回')
    jkxq_fanhui_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]")
    jkxq_title_text = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]")

    webView = page_element(accessibility_id = "WebView")

    zixun_title = page_element(accessibility_id = "//UIAStaticText[@name='资讯']")
    shezhi_btn = page_element(accessibility_id = "设置")
    gonggao_title = page_element(xpath = "//UIAStaticText[@name='公司公告']")

    chakanyuanwen_staText = page_element(accessibility_id= "查看原文")

    shoucang_btn = page_element(accessibility_id = "收藏")
    fenxiang_btn = page_element(accessibility_id = "分享")

    xiangqing_title = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[1]")



