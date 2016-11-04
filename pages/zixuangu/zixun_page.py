#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class ZixunPage(PageObject):
	"""
	自选－> 新闻－> 研报－> 某条研报详情页
	研报具体页面的相关元素
	"""
	fanhui_btn = page_element(accessibility_id = '返回')

	webView = page_element(accessibility_id = "WebView")

	chakanyuanwen_staText = page_element(accessibility_id= "查看原文")



