#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page_object.appium_page_objects import PageObject, page_element

class FenshikxianYujingPage(PageObject):
    """
    	分时k线页面---预警页面的一些操作及元素查找
    """
    fanhui_button = page_element(accessibility_id='返回')
    wodeyujing_btn = page_element(accessibility_id = '我的预警')
    tianjiayujing_btn = page_element(accessibility_id = '添加预警')

    #没有预警信息时 弹出的提示信息
    queding_btn = page_element(accessibility_id = '确定')
    info_staticText = page_element(accessibility_id = '您未设置股价预警信息')

    #提示框返回
    tishi_fanhui_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[1]/UIAButton[1]')
    tishi_window = page_element(xpath = "//UIAAlert[@name='提示']")
