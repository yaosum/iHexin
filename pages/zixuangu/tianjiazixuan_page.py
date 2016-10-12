#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element


class TianjiazixuanPage(PageObject):
	fanhui_button = page_element(accessibility_id = '返回')
	tianjiazixuan_staticText = page_element(xpath= "//UIAStaticText[@name='添加自选']")

	qingchuwenben_button = page_element(accessibility_id = '清除文本')

	zixuanadd_button = page_element(accessibility_id='zixuan add')

	addPFYH_btn = page_element(accessibility_id = '添加浦发银行')
	addPAYH_btn = page_element(accessibility_id = '添加平安银行')
	addYSBG_btn = page_element(accessibility_id='添加云赛Ｂ股')
	addSWYB_btn = page_element(accessibility_id='添加深物业B')
	add21GZ_btn = page_element(accessibility_id='添加21国债⑺')
	addGZ0213_btn = page_element(accessibility_id='添加国债0213')
	addJJYF_btn = page_element(accessibility_id='添加基金银丰')
	addRHXK_btn = page_element(accessibility_id='添加瑞和小康')
	addCB5_btn = page_element(accessibility_id='添加长  白 5')
	addSZCZ_btn = page_element(accessibility_id='添加深证成指')
	addDQS_btn = page_element(accessibility_id='添加道琼斯工业平均指数')
	addBD_btn = page_element(accessibility_id='添加百度')
	add50ETF_btn = page_element(accessibility_id='添加50ETF')
	addY15_btn = page_element(accessibility_id='添加银15Kg')
	addHJ9999_btn = page_element(accessibility_id='添加黄金9999')

	addCH_btn = page_element(accessibility_id='添加长和')
	addHSZS_btn = page_element(accessibility_id='添加恒生指数')



