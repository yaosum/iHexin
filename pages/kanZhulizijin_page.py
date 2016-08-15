#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..appium_page_objects import PageObject, page_element


class KanZhulizijinPage(PageObject):
	fanhui_btn = page_element(xpath= '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]')
	kanzhulizijin_staticText = page_element(xpath= '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]')
	gengduo_button = page_element(accessibility_id= '更多')
	#closeTip_button = page_element()

	denglu_btn = page_element(accessibility_id='登录')

	zixuan_btn = page_element(xpath= '//UIAApplication[1]/UIAWindow[1]/UIAButton[3]')
	hushen_btn = page_element(accessibility_id='沪深')
	hangye_btn = page_element(accessibility_id='行业')
	gainian_btn = page_element(accessibility_id='概念')

	zuixin_staText = page_element(accessibility_id='最新')
	dadanjingliang_staText = page_element(accessibility_id='大单净量')
	zhangfu_staText = page_element(accessibility_id='涨幅')
	zhuliliuru_staText = page_element(accessibility_id='主力流入')
	zhuliliuchu_staText = page_element(accessibility_id='主力流出')
	zhulijingliuru_staText = page_element(accessibility_id='主力净流入')
	jingliuru_staText = page_element(accessibility_id='净流入')
	zhulijingezhanbi_staText = page_element(accessibility_id='主力净额占比')
	rijingliang5_staText = page_element(accessibility_id='5日净量')
	rijingliang10_staText = page_element(accessibility_id='10日净量')
	rizhangfu5_staText = page_element(accessibility_id='5日涨幅')
	rizhangfu10_staText = page_element(accessibility_id='10日涨幅')
	liangbi_staText = page_element(accessibility_id='量比')
	huanshou_staText = page_element(accessibility_id='换手')
	shiyingdong_staText = page_element(accessibility_id='市盈(动)')
	shijinglv_staText = page_element(accessibility_id='市净率')
	liutongshizhi_staText = page_element(accessibility_id='流通市值')
	zongshizhi_staText = page_element(accessibility_id='总市值')

	rizhangfu20_staText = page_element(accessibility_id='20日涨幅')
	zongshou_staText = page_element(accessibility_id='总手')
	jine_staText = page_element(accessibility_id='金额')

	desc_img = page_element(accessibility_id='DescImg')
	asc_img = page_element(accessibility_id='AscImg')

	def hx_ergodic_hushen_zhibiao(self):
		self.zuixin_staText.click()
		assert self.desc_img
		self.zuixin_staText.click()
		assert self.asc_img
		self.dadanjingliang_staText.click()
		self.dadanjingliang_staText.click()
		self.zhangfu_staText.click()
		self.zhangfu_staText.click()
		self.zhuliliuru_staText.click()
		self.zhuliliuru_staText.click()
		self.zhuliliuchu_staText.click()
		self.zhuliliuchu_staText.click()
		self.zhulijingliuru_staText.click()
		self.zhulijingliuru_staText.click()
		self.jingliuru_staText.click()
		self.jingliuru_staText.click()
		self.zhulijingezhanbi_staText.click()
		self.zhulijingezhanbi_staText.click()
		self.rijingliang5_staText.click()
		self.rijingliang5_staText.click()
		self.rijingliang10_staText.click()
		self.rijingliang10_staText.click()
		self.rizhangfu5_staText.click()
		assert self.desc_img
		self.rizhangfu5_staText.click()
		assert self.asc_img
		self.rizhangfu10_staText.click()
		self.rizhangfu10_staText.click()
		self.liangbi_staText.click()
		self.liangbi_staText.click()
		self.huanshou_staText.click()
		self.huanshou_staText.click()
		self.shiyingdong_staText.click()
		self.shiyingdong_staText.click()
		self.shijinglv_staText.click()
		self.shijinglv_staText.click()
		self.liutongshizhi_staText.click()
		self.liutongshizhi_staText.click()
		self.zongshizhi_staText.click()
		assert self.desc_img
		self.zongshizhi_staText.click()
		assert self.asc_img

	def hx_ergodic_zhibiao(self):
		self.dadanjingliang_staText.click()
		assert self.asc_img
		self.dadanjingliang_staText.click()
		assert self.desc_img
		self.zhangfu_staText.click()
		self.zhangfu_staText.click()
		self.huanshou_staText.click()
		self.huanshou_staText.click()
		self.rizhangfu5_staText.click()
		self.rizhangfu5_staText.click()
		self.rizhangfu10_staText.click()
		self.rizhangfu10_staText.click()
		self.rizhangfu20_staText.click()
		self.zongshou_staText.click()
		self.zongshou_staText.click()
		self.jine_staText.click()
		assert self.desc_img
		self.jine_staText.click()
		assert self.asc_img