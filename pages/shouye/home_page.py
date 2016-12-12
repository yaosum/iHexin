#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class HomePage(PageObject):
	"""
	首页
	"""
	button_337705299 = page_element(accessibility_id = "337705299")
	yonghu_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]")
	feivip_button = page_element(accessibility_id = "非vip")
	qiehuanyejianmoshi_button = page_element(accessibility_id = "切换到夜间模式")
	sousuo_button = page_element(accessibility_id = "搜索")
	gerenzhongxin_btn = page_element(accessibility_id = '个人中心')
	# 非审核状态下
	xiaoxizhongxin_btn_feishen = page_element(accessibility_id = "message center")
	# 审核状态下
	xiaoxizhongxin_btn_shen = page_element(accessibility_id = "message_center_entrance.png")





