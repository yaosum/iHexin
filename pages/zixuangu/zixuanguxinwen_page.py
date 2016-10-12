#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class ZixuanguxinwenPage(PageObject):
	fanhui_btn = page_element(accessibility_id= "返回")
	zixuanguxinwen_staText = page_element(xpath = "//UIAStaticText[@name='自选股新闻']")

	cell01 = page_element(xpath= '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]')
	yanbao_btn = page_element(accessibility_id= "研报")

	def hx_upglide(self):
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (85 / 375.0)
		start_y = height * (584 / 667.0)
		end_x = width * (85 / 375.0)
		end_y = height * (112 / 667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

	def hx_downglide(self):
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (85 / 375.0)
		start_y = height * (112 / 667.0)
		end_x = width * (85 / 375.0)
		end_y = height * (584 / 667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)