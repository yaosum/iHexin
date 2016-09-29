#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.public.denglu_page import DengluPage
from pages.public.public_page import PublicPage
from pages.public.searchStock_page import SearchStockPage
from pages.shouye.home_page import HomePage
from pages.zixuangu.bianjizixuan_page import BianjizixuanPage
from pages.zixuangu.kanZhulizijin_page import KanZhulizijinPage
from pages.zixuangu.optional_page import OptionalPage
from pages.zixuangu.tianjiazixuan_page import TianjiazixuanPage
from pages.zixuangu.wodezichan_page import WodezichanPage
from pages.zixuangu.zixuanDapan_page import ZixuanDapanPage
from pages.zixuangu.zixuangugonggao_page import ZixuangugonggaoPage
from pages.zixuangu.zixuanguxinwen_page import ZixuanguxinwenPage
from pages.zixuangu.zixun_page import ZixunPage


def test_step001(driver):
	home_page = HomePage(driver)
	optional_page = OptionalPage(driver)
	bianjizixuan_page = BianjizixuanPage(driver)
	tianjiazixuan_page = TianjiazixuanPage(driver)
	public_page = PublicPage(driver)
	# step1
	assert home_page.gerenzhongxin_button
	assert home_page.feivip_button
	assert home_page.qiehuanyejianmoshi_button
	# step2
	public_page.zixuan_button.click()
	assert optional_page.zixuan_staticText
	assert optional_page.tongbuzixuangu_btn
	assert optional_page.duoshoujiPCtongbu_staText
	# step3
	optional_page.bianji_button.click()
	assert bianjizixuan_page.bianjizixuan_StaticText
	# step4
	bianjizixuan_page.tianjiagupiao_button.click()
	assert tianjiazixuan_page.tianjiazixuan_staticText
"""
def test_step005(driver):
	public_page = PublicPage(driver)
	optional_page = OptionalPage(driver)
	tianjiazixuan_page = TianjiazixuanPage(driver)
	bianjizixuan_page = BianjizixuanPage(driver)
	searchStock_page = SearchStockPage(driver)
	fenshikxian_page = FenshiKxianPage(driver)

	# step5-10
	public_page.zixuan_button.click()
	assert optional_page.cell001_stock_staText.text == u'上证指数'
	assert optional_page.cell002_stock_staText.text == u'创业板指'
	assert optional_page.cell003_stock_staText.text == u'同花顺'
	optional_page.bianji_button.click()
	bianjizixuan_page.tianjiagupiao_button.click()
	sleep(1)
	# 添加股票
	stocks = [('600000','addPFYH_btn'), ('000001','addPAYH_btn'), ('900901','addYSBG_btn'), ('200011','addSWYB_btn'), ('010107','add21GZ_btn'),
	              ('100213','addGZ0213_btn'), ('500058','addJJYF_btn'), ('150008','addRHXK_btn'), ('400002','addCB5_btn'), ('399001','addSZCZ_btn'),
	              ('dji','addDQS_btn'), ('BIDU','addBD_btn'), ('510050','add50ETF_btn'), ('TJAG00','addXHBY_btn'), ('00001','addCH_btn'),
	              ('hsi','addHSZS_btn')]
	for stockCode,stockName in stocks:
		print stockCode,stockName
		searchStock_page.hx_send_keys(stockCode)
		try:
			eval('tianjiazixuan_page.{}.click()'.format(stockName))
		except:
			print '该股票已添加过'
		tianjiazixuan_page.qingchuwenben_button.click()
	# step11
	tianjiazixuan_page.fanhui_button.click()
	bianjizixuan_page.fanhui_button.click()
	optional_page.bianji_button.click()
	bianjizixuan_page.hx_upglide()
	assert bianjizixuan_page.cell001_stock_staText.text == u'现货白银'
	bianjizixuan_page.hx_upglide()
	assert bianjizixuan_page.cell017_stock_staText.text == u'同花顺'
	assert bianjizixuan_page.PFYH_staText
	# step12
	bianjizixuan_page.fanhui_button.click()
	sleep(1)
	assert optional_page.cell001_stock_staText.text == u'现货白银'
	optional_page.hx_upglide()
	sleep(1)
	assert optional_page.THS_stock_staText
	# step13
	public_page.shouye_button.click()
	# step14
	public_page.zixuan_button.click()
	# step15
	optional_page.bianji_button.click()
	bianjizixuan_page.hx_upglide()
	sleep(1)
	#置顶三次操作
	for n in range(3):
		print n
		bianjizixuan_page.cell017_zhiding_btn.click()
		sleep(1)
	# 第一条为上证指数
	bianjizixuan_page.hx_glide()
	sleep(1)
	assert bianjizixuan_page.cell001_stock_staText.text == u'上证指数'
	bianjizixuan_page.fanhui_button.click()
	optional_page.hx_glide()
	sleep(1)
	assert optional_page.cell001_stock_staText.text == u'上证指数'
	# step18
	optional_page.bianji_button.click()
	action1 = TouchAction(driver)
	action1.press(bianjizixuan_page.cell002_tuodong_btn).wait(100).move_to(bianjizixuan_page.cell001_tuodong_btn).wait(100).release()
	action1.perform()
	action2 = TouchAction(driver)
	action2.press(bianjizixuan_page.cell003_tuodong_btn).wait(100).move_to(bianjizixuan_page.cell001_tuodong_btn).wait(100).release()
	action2.perform()
	print optional_page.cell001_stock_staText.text
	assert optional_page.cell001_stock_staText.text == u'同花顺'
	# step18
	bianjizixuan_page.fanhui_button.click()
	optional_page.bianji_button.click()
	# 删除前三支股票
	bianjizixuan_page.cell001_btn.click()
	bianjizixuan_page.cell002_btn.click()
	bianjizixuan_page.cell003_btn.click()
	bianjizixuan_page.shanchu_button.click()
	# step19
	bianjizixuan_page.fanhui_button.click()
	# step20
	optional_page.sousuo_button.click()
	sleep(1)
	searchStock_page.hx_send_keys('1A0001')
	searchStock_page.zixuanadd_button.click()
	searchStock_page.qingchuwenben_button.click()
	searchStock_page.hx_send_keys('399006')
	sleep(1)
	fenshikxian_page.jiazixuan_staText.click()
	fenshikxian_page.fanhui_button.click()
	optional_page.sousuo_button.click()
	sleep(1)
	searchStock_page.hx_send_keys('300033')
	sleep(1)
	fenshikxian_page.jiazixuan_staText.click()
	fenshikxian_page.fanhui_button.click()

	# step90
	# 上下滑
	for n in range(2):
		optional_page.hx_upglide()
	for n in range(2):
		optional_page.hx_glide()
	# step91
	# 左右滑
	for n in range(12):
		optional_page.hx_right()
	for n in range(13):
		optional_page.hx_left()
	# step93
	optional_page.zuixin_staText.click()
	optional_page.zuixin_staText.click()
	optional_page.quxiaopaixu_btn.click()

	for n in range(12):
		optional_page.hx_right()

	optional_page.zhenfu_staText.click()
	optional_page.zhenfu_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.weibi_staText.click()
	optional_page.weibi_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.zuidi_staText.click()
	optional_page.zuidi_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.zuigao_staText.click()
	optional_page.zuigao_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.zuoshou_staText.click()
	optional_page.zuoshou_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.kaipan_staText.click()
	optional_page.kaipan_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.xianshou_staText.click()
	optional_page.xianshou_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.shijinglv_staText.click()
	optional_page.shijinglv_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.shiyingdong_staText.click()
	optional_page.shiyingdong_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.liangbi_staText.click()
	optional_page.liangbi_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.huanshou_staText.click()
	optional_page.huanshou_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.zongshou_staText.click()
	optional_page.zongshou_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.zhangsu_staText.click()
	optional_page.zhangsu_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.zhangdie_staText.click()
	optional_page.zhangdie_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.zhangfu_staText.click()
	optional_page.zhangfu_staText.click()
	optional_page.quxiaopaixu_btn.click()

	optional_page.zuixin_staText.click()
	optional_page.zuixin_staText.click()
	optional_page.quxiaopaixu_btn.click()

	# step99
	optional_page.hx_glide()
	sleep(1)
	#assert optional_page.cell001_stock_staText.text == u'同花顺'
	#optional_page.cell001.click()
	optional_page.THS_stock_staText.click()
	sleep(1)
	# step100
	for n in range(17):
		fenshikxian_page.xiayigegupiao_button.click

	for n in range(17):
		fenshikxian_page.shangyigegupiao_button.click()

	fenshikxian_page.hx_left()
	sleep(1)
	assert fenshikxian_page.klineTabButton
	assert fenshikxian_page.shezhi_btn

	for n in range(17):
		fenshikxian_page.xiayigegupiao_button.click

	for n in range(17):
		fenshikxian_page.shangyigegupiao_button.click()
	# step103
	fenshikxian_page.fanhui_button.click()

	optional_page.zuixin_staText.click()
	optional_page.hx_longPress(optional_page.cell001)
	optional_page.zhidi_btn.click()
	# 待扩展
	optional_page.quxiaopaixu_btn.click()
	optional_page.zuixin_staText.click()
	optional_page.hx_upglide()
	optional_page.hx_longPress(optional_page.cell017)
	optional_page.zhiding_btn.click()
	optional_page.quxiaopaixu_btn.click()
	optional_page.hx_glide()
	optional_page.hx_longPress(optional_page.cell001)
	optional_page.shanchu_btn.click()
	optional_page.hx_longPress(optional_page.cell001)
	optional_page.shanchu_btn.click()
"""

def test_step031(driver):
	public_page = PublicPage(driver)
	optional_page = OptionalPage(driver)
	searchStock_page = SearchStockPage(driver)
	zixuanDapan_page = ZixuanDapanPage(driver)
	fenshikxian_page = FenshiKxianPage(driver)

	public_page.zixuan_button.click()
	optional_page.zixuanIndexItemName_staText.click()
	zixuanDapan_page.shen_btn.click()
	zixuanDapan_page.chuang_btn.click()
	driver.swipe(start_x=300, start_y=239, end_x=39, end_y=239, duration=500)
	zixuanDapan_page.shen_btn.click()
	zixuanDapan_page.hu_btn.click()

	driver.swipe(start_x=39, start_y=239, end_x=300, end_y=239, duration=500)
	driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 188, "y": 480})
	optional_page.zixuanIndexItemName_staText.click()
	zixuanDapan_page.shen_btn.click()
	driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 188, "y": 480})
	optional_page.zixuanIndexItemName_staText.click()
	zixuanDapan_page.chuang_btn.click()
	driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 188, "y": 480})
	optional_page.zixuanIndexItemName_staText.click()
	zixuanDapan_page.fenshitu_scr.click()
	fenshikxian_page.xiayigegupiao_button.click()
	fenshikxian_page.xiayigegupiao_button.click()
	fenshikxian_page.xiayigegupiao_button.click()
	driver.swipe(start_x=331, start_y=296, end_x=59, end_y=296, duration=500)
	fenshikxian_page.xiayigegupiao_button.click()
	fenshikxian_page.xiayigegupiao_button.click()
	fenshikxian_page.xiayigegupiao_button.click()
	driver.swipe(start_x=59, start_y=296, end_x=331, end_y=296, duration=500)
	fenshikxian_page.fanhui_button.click()

def test_step051(driver):
	public_page = PublicPage(driver)
	optional_page = OptionalPage(driver)
	kanzhulizijin_page = KanZhulizijinPage(driver)
	denglu_page = DengluPage(driver)

	public_page.zixuan_button.click()
	optional_page.zijin_btn.click()
	kanzhulizijin_page.denglu_btn.click()
	denglu_page.guanbi_btn.click()
	kanzhulizijin_page.hushen_btn.click()
	# 上下滑
	driver.swipe(start_x=304, start_y=598, end_x=304, end_y=154, duration=500)
	driver.swipe(start_x=304, start_y=154, end_x=304, end_y=598, duration=500)

	# 左右滑
	driver.swipe(start_x=358, start_y=466, end_x=142, end_y=466, duration=500)
	driver.swipe(start_x=358, start_y=466, end_x=142, end_y=466, duration=500)
	driver.swipe(start_x=358, start_y=466, end_x=142, end_y=466, duration=500)
	driver.swipe(start_x=358, start_y=466, end_x=142, end_y=466, duration=500)

	driver.swipe(start_x=142, start_y=466, end_x=358, end_y=466, duration=500)
	driver.swipe(start_x=142, start_y=466, end_x=358, end_y=466, duration=500)
	driver.swipe(start_x=142, start_y=466, end_x=358, end_y=466, duration=500)

	kanzhulizijin_page.hx_ergodic_hushen_zhibiao()

	kanzhulizijin_page.hangye_btn.click()
	kanzhulizijin_page.hx_ergodic_zhibiao()

	kanzhulizijin_page.gainian_btn.click()
	kanzhulizijin_page.hx_ergodic_zhibiao()

	kanzhulizijin_page.fanhui_btn.click()

def test_step69(driver):
	public_page = PublicPage(driver)
	optional_page = OptionalPage(driver)
	zixuanguxinwen_page = ZixuanguxinwenPage(driver)
	zixun_page = ZixunPage(driver)

	public_page.zixuan_button.click()
	optional_page.xinwen_btn.click()
	assert zixuanguxinwen_page.zixuanguxinwen_staText
	driver.swipe(start_x=85, start_y=584, end_x=85, end_y=112, duration=500)
	driver.swipe(start_x=85, start_y=112, end_x=85, end_y=584, duration=500)
	driver.swipe(start_x=85, start_y=112, end_x=85, end_y=584, duration=500)
	zixuanguxinwen_page.cell01.click()
	zixun_page.fanhui_btn.click()
	zixuanguxinwen_page.yanbao_btn.click()
	driver.swipe(start_x=85, start_y=584, end_x=85, end_y=112, duration=500)
	driver.swipe(start_x=85, start_y=112, end_x=85, end_y=584, duration=500)
	driver.swipe(start_x=85, start_y=112, end_x=85, end_y=584, duration=500)
	zixuanguxinwen_page.cell01.click()
	zixun_page.fanhui_btn.click()
	zixuanguxinwen_page.fanhui_btn.click()

def test_step80(driver):
	public_page = PublicPage(driver)
	optional_page = OptionalPage(driver)
	zixuangugonggao_page=ZixuangugonggaoPage(driver)
	zixun_page = ZixunPage(driver)

	public_page.zixuan_button.click()
	optional_page.gonggao_btn.click()
	assert zixuangugonggao_page.zixuangugonggao_staText.text == u'自选股公告'
	driver.swipe(start_x=86, start_y=584, end_x=86, end_y=112, duration=500)
	driver.swipe(start_x=85, start_y=112, end_x=85, end_y=584, duration=500)
	driver.swipe(start_x=85, start_y=112, end_x=85, end_y=584, duration=500)
	zixuangugonggao_page.cell01.click()

	zixun_page.fanhui_btn.click()
	zixuangugonggao_page.fanhui_btn.click()

def test_step88(driver):
	public_page = PublicPage(driver)
	optional_page = OptionalPage(driver)
	wodezichan_page = WodezichanPage(driver)

	public_page.zixuan_button.click()
	optional_page.zichan_btn.click()
	wodezichan_page.fanhui_btn.click()