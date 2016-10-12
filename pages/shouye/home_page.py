#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class HomePage(PageObject):
	# navigation bar
	gerenzhongxin_button = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]")
	feivip_button = page_element(accessibility_id = "非vip")
	qiehuanyejianmoshi_button = page_element(accessibility_id = "切换到夜间模式")
	sousuo_button = page_element(accessibility_id = "搜索")

	xiaoxizhongxin_button = page_element(accessibility_id = "message center")




