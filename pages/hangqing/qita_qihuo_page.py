#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class QitaQihuoPage(PageObject):
    """
    行情－> 其他－> 期货
    期货页面的相关元素及操作
    """
    fanhui_button = page_element(accessibility_id='返回')

    zhangfu_statictext = page_element(accessibility_id = '涨幅')
    zhangdie_statictext = page_element(accessibility_id='涨跌')

    cell01_title = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')

   #国内期货和外汇，涨跌涨幅按钮点击
    zhangdiefu_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]")


