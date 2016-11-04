#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class Kefuzhongxin(PageObject):
    """
    客服中心页面的相关元素及方法
    """
    fanhui_btn = page_element(accessibility_id= '返回')