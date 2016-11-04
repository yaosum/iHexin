#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep

from appium import webdriver

from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.public.public_page import PublicPage
from pages.public.searchStock_page import SearchStockPage
from pages.shouye.home_page import HomePage
from pages.zixuangu.bianjizixuan_page import BianjizixuanPage
from pages.zixuangu.optional_page import OptionalPage
from pages.zixuangu.tianjiazixuan_page import TianjiazixuanPage

def test_search(driver):
	optional_page = OptionalPage(driver)
	fenshikxian_page = FenshiKxianPage(driver)
	searchStock_page = SearchStockPage(driver)
	bianjizixuan_page = BianjizixuanPage(driver)
	public_page = PublicPage(driver)
	home_page = HomePage(driver)
	tianjiazixuan_page = TianjiazixuanPage(driver)

	public_page.zixuan_button.click()
	optional_page.bianji_button.click()
	bianjizixuan_page.tianjiagupiao_button.click()
	sleep(1)
	stockCodes = [('600000', 'addPFYH_btn'), ('000001','addPAYH_btn')]
	#stockNames = ['','addPAYH_btn']
	for stockCode, stockName in stockCodes:
		searchStock_page.hx_send_keys(stockCode)
		try:
			eval('tianjiazixuan_page.{}.click()'.format(stockName))
		except:
			print '该股票已添加过'
		tianjiazixuan_page.qingchuwenben_button.click()

if __name__ == '__main__':
	# equals to setUp
	desired_caps = {}
	# basic settings
	desired_caps['platformName'] = 'iOS'
	desired_caps['platformVersion'] = '9.3'

	# real device
	desired_caps['deviceName'] = 'iPhone 6'
	desired_caps['udid'] = '57e95712fdd52a1fce030ed46808f1a98e9b2f5e'
	desired_caps['bundleId'] = 'cn.com.10jqka.iHexinFee'
	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	test_search(driver)

