#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class ZixuanguxinwenPage(PageObject):
	"""
	自选－> 新闻
	新闻及研报页面的相关元素及操作
	"""
	fanhui_btn = page_element(accessibility_id= "返回")
	zixuanguxinwen_staText = page_element(xpath = "//UIAStaticText[@name='自选股新闻']")
	zixuanguyanbao_staText = page_element(xpath="//UIAStaticText[@name='自选股研报']")

	xinwen_btn = page_element(accessibility_id= '新闻')
	yanbao_btn = page_element(accessibility_id='研报')

	xinwen_bankuai1_staText = page_element(xpath="//UIAStaticText[@name= '板块1新闻']")
	xinwen_bankuai2_staText = page_element(xpath="//UIAStaticText[@name= '板块2新闻']")
	xinwen_bankuai3_staText = page_element(xpath="//UIAStaticText[@name= '板块3新闻']")
	xinwen_bankuai4_staText = page_element(xpath="//UIAStaticText[@name= '板块4新闻']")
	xinwen_bankuai5_staText = page_element(xpath="//UIAStaticText[@name= '板块5新闻']")
	xinwen_bankuai6_staText = page_element(xpath="//UIAStaticText[@name= '板块6新闻']")
	xinwen_bankuai7_staText = page_element(xpath="//UIAStaticText[@name= '板块7新闻']")
	xinwen_bankuai8_staText = page_element(xpath="//UIAStaticText[@name= '板块8新闻']")

	yanbao_bankuai1_staText = page_element(xpath="//UIAStaticText[@name= '板块1研报']")
	yanbao_bankuai2_staText = page_element(xpath="//UIAStaticText[@name= '板块2研报']")
	yanbao_bankuai3_staText = page_element(xpath="//UIAStaticText[@name= '板块3研报']")
	yanbao_bankuai4_staText = page_element(xpath="//UIAStaticText[@name= '板块4研报']")
	yanbao_bankuai5_staText = page_element(xpath="//UIAStaticText[@name= '板块5研报']")
	yanbao_bankuai6_staText = page_element(xpath="//UIAStaticText[@name= '板块6研报']")
	yanbao_bankuai7_staText = page_element(xpath="//UIAStaticText[@name= '板块7研报']")
	yanbao_bankuai8_staText = page_element(xpath="//UIAStaticText[@name= '板块8研报']")


	#第一行研报／新闻
	cell01 = page_element(xpath= '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]')
	yanbao_btn = page_element(accessibility_id= "研报")

	def hx_upglide(self):
		"""
		向上滑动
		:return:
		"""
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (85 / 375.0)
		start_y = height * (584 / 667.0)
		end_x = width * (85 / 375.0)
		end_y = height * (112 / 667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

	def hx_downglide(self):
		"""
		向下滑动
		:return:
		"""
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (85 / 375.0)
		start_y = height * (112 / 667.0)
		end_x = width * (85 / 375.0)
		end_y = height * (584 / 667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)