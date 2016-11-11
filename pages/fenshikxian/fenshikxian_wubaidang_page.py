#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element
import types
from time import sleep
from pages.public.public_method import PublicMethod

class QuanjingwubaidangPage(PageObject):
    wubaidang_title = page_element(accessibility_id = '全景500档')
    fanhui_btn = page_element(accessibility_id = '返回')
    sousuo_btn = page_element(accessibility_id = '搜索')