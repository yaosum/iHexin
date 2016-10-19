#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from time import sleep

__author__ = "Hemin Won"

class OptionalPage(PageObject):
	# navigation bar
	#bianji_button = page_element(accessibility_id = "编辑")
	bianji_button = page_element(xpath="//UIAApplication[1]/UIAWindow[1]/UIAButton[21]")
	zixuan_staticText = page_element(xpath = "//UIAStaticText[@name='自选']")
	sousuo_button = page_element(accessibility_id = "搜索")

	zixuanIndexItemName_staText = page_element(accessibility_id = 'ZixuanIndexItemName')
	zijin_btn = page_element(accessibility_id = '资金')
	xinwen_btn = page_element(accessibility_id = '新闻')
	gonggao_btn = page_element(accessibility_id='公告')
	zichan_btn = page_element(accessibility_id='资产')

	zuixin_staText = page_element(accessibility_id ="最新")
	zhangfu_staText = page_element(accessibility_id="涨幅")
	zhangdie_staText = page_element(accessibility_id="涨跌")
	zhangsu_staText = page_element(accessibility_id="涨速")
	zongshou_staText = page_element(accessibility_id="总手")
	huanshou_staText = page_element(accessibility_id="换手")
	liangbi_staText = page_element(accessibility_id='量比')
	shiyingdong_staText = page_element(accessibility_id='市盈(动)')
	shijinglv_staText = page_element(accessibility_id='市净率')
	xianshou_staText = page_element(accessibility_id='现手')
	kaipan_staText = page_element(accessibility_id='开盘')
	zuoshou_staText = page_element(accessibility_id='昨收')
	zuigao_staText = page_element(accessibility_id='最高')
	zuidi_staText = page_element(accessibility_id='最低')
	weibi_staText = page_element(accessibility_id='委比')
	zhenfu_staText = page_element(accessibility_id='振幅')

	tongbuzixuangu_btn = page_element(accessibility_id='同步自选股')
	duoshoujiPCtongbu_staText = page_element(accessibility_id='多手机，pc同步自选股')


	quxiaopaixu_btn = page_element(accessibility_id="取消排序")

	shanchu_btn = page_element(accessibility_id="删除")
	zhiding_btn = page_element(accessibility_id="置顶")
	zhidi_btn = page_element(accessibility_id="置底")

	THS_stock_staText = page_element(xpath="//UIAStaticText[@name='同花顺']")
	SZZS_stock_staText = page_element(xpath="//UIAStaticText[@name='上证指数']")
	CYBZ_stock_staText = page_element(xpath="//UIAStaticText[@name='创业扳指']")
	PFYH_stock_staText = page_element(xpath="//UIAStaticText[@name='浦发银行']")
	PAYH_stock_staText = page_element(xpath="//UIAStaticText[@name='平安银行']")
	YSBG_stock_staText = page_element(xpath="//UIAStaticText[@name='云赛Ｂ股']")
	SWYB_stock_staText = page_element(xpath="//UIAStaticText[@name='深物业B']")
	GZ217_stock_staText = page_element(xpath="//UIAStaticText[@name='21国债⑺']")
	GZ0213_stock_staText = page_element(xpath="//UIAStaticText[@name='国债0213']")
	JJYF_stock_staText = page_element(xpath="//UIAStaticText[@name='基金银丰']")
	RHXK_stock_staText = page_element(xpath="//UIAStaticText[@name='瑞和小康']")
	CB5_stock_staText = page_element(xpath="//UIAStaticText[@name='长白5']")
	SZCZ_stock_staText = page_element(xpath="//UIAStaticText[@name='深证成指']")
	DQS_stock_staText = page_element(xpath="//UIAStaticText[@name='道琼斯']")
	BD_stock_staText = page_element(xpath="//UIAStaticText[@name='百度']")
	ETF50_stock_staText = page_element(xpath="//UIAStaticText[@name='50ETF']")
	XHBY_stock_staText = page_element(xpath="//UIAStaticText[@name='现货白银']")

	THS_cell = page_element(xpath="//UIATableView[1]/UIATableCell[@name='同花顺']")

	fenzu_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]")
	cell001 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]')
	cell001_title = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')
	cell002 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]')
	cell002_title = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[1]')
	cell003 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]')
	cell017 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[17]')
	cell05 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[5]')

	cell001_stock_staText = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')
	cell002_stock_staText = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[1]')
	cell003_stock_staText = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAStaticText[1]')

	def hx_upglide(self):
		# 基于iPhone6 375/667
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (256/375.0)
		start_y = height * (598/667.0)
		end_x = width * (256/375.0)
		end_y = height * (183/667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

	def hx_glide(self):
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (256 / 375.0)
		start_y = height * (183 / 667.0)
		end_x = width * (256 / 375.0)
		end_y = height * (598/667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

	def hx_right(self):
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (359 / 375.0)
		start_y = height * (214 / 667.0)
		end_x = width * (164 / 375.0)
		end_y = height * (214 / 667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

	def hx_left(self):
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (164 / 375.0)
		start_y = height * (214 / 667.0)
		end_x = width * (359 / 375.0)
		end_y = height * (214 / 667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

	def hx_longPress(self, element):

		location = element.location
		el_size = element.size

		x = el_size['width'] / 2.0 + location['x']
		y = el_size['height'] / 2.0 + location['y']

		return self.w.tap([(x, y)], duration=0.5)

	# 从自选股页面滑动到分组页面
	def zx_left(self):
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (365 / 375.0)
		start_y = height * (466 / 667.0)
		end_x = width * (200 / 375.0)
		end_y = height * (466 / 667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)
	#从分组页面滑到自选股页面
	def zx_right(self):
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (10 / 375.0)
		start_y = height * (466 / 667.0)
		end_x = width * (200 / 375.0)
		end_y = height * (466 / 667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

	def pageGotoFenshikxian(self):
		fenshikxian_page = FenshiKxianPage(self.w)
		title1 = self.cell001_title.text
		self.cell001.click()
		assert fenshikxian_page.title_staText.text == title1
		# step73-76
		fenshikxian_page.change_gupiao(1)
		# step 77
		fenshikxian_page.fanhui_button.click()
		sleep(1)
		length = int(len(self.w.find_elements_by_xpath("//UIATableView[1]/UIATableCell[@name]")))
		if length >= 2:
			title2 = self.cell002_title.text
			self.cell002.click()
			assert fenshikxian_page.title_staText.text == title2
			fenshikxian_page.change_gupiao(1)
			fenshikxian_page.fanhui_button.click()