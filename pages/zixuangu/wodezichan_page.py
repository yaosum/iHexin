#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class WodezichanPage(PageObject):
	"""
	自选－> 我的资产
	"""
	fanhui_btn = page_element(accessibility_id = '返回')
	wodezichan_staText = page_element(xpath = "//UIAStaticText[@name='我的资产']")