#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class DengluPage(PageObject):
	guanbi_btn = page_element(accessibility_id = '关闭')
