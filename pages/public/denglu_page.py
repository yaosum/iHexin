#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class DengluPage(PageObject):
    guanbi_btn = page_element(accessibility_id = '关闭')

    username_text = page_element(accessibility_id = "登录账号")
    password_text = page_element(accessibility_id = "密码")
    denglu_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAButton[4]")

