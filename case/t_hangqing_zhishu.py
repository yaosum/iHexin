# -*- coding: utf-8 -*-
"""
前置条件:未登陆
"""
from time import sleep

from pages.public.debug_page import DebugPage
from pages.public.public_method import PublicMethod
from pages.public.public_page import PublicPage
from pages.hangqing.zhishu_page import ZhishuPage
from pages.zixuangu.kanZhulizijin_page import KanZhulizijinPage
from pages.hangqing.hangqing_page import HangqingPage
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.hangqing.guzhiQihuo_gengduo_page import GuzhiQihuoGengduoPage
from pages.hangqing.hangqing_gengduo_page import HangqingGengduoPage
from pages.public.public_method import PublicMethod

caseName = '20161208'

#进入看主力资金页面，在自选已经运行过这部分脚本，这里只需要看能否正常进入
def test_step3(driver):
    public_page = PublicPage(driver)
    zhishu_page = ZhishuPage(driver)
    kanzhulizijin_page = KanZhulizijinPage(driver)
    hangqing_page = HangqingPage(driver)
    public_method = PublicMethod(driver)
    debug_page = DebugPage(driver)

    # step2
    #debug_page.switch_server("112.17.10.145", "9528")
    #step2
    public_page.hangqing_button.click()
    sleep(1)
    hangqing_page.zhishu_btn.click()
    zhishu_page.kanzijin_btn.click()
    assert kanzhulizijin_page.kanzhulizijin_staticText
    picName = '行情－指数-看资金_2'
    public_method.public_screenshot_as_file(picName=picName)

#进入指数并验证
def test_step1(driver):
    public_page = PublicPage(driver)
    zhishu_page = ZhishuPage(driver)
    hangqing_page = HangqingPage(driver)
    public_method = PublicMethod(driver)
    debug_page = DebugPage(driver)

    # step2
    #debug_page.switch_server("112.17.10.145", "9528")

    #step2
    public_page.hangqing_button.click()
    hangqing_page.zhishu_btn.click()

    assert zhishu_page.zhishu_btn
    assert zhishu_page.guoneiZhishu_btn
    assert zhishu_page.qihuo_btn

    picName = '行情－指数_3'
    public_method.public_screenshot_as_file(picName=picName)

#国内指数
def test_step21(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    zhishu_page = ZhishuPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)
    public_method = PublicMethod(driver)
    debug_page = DebugPage(driver)

    # step2
    #debug_page.switch_server("112.17.10.145", "9528")

    public_page.hangqing_button.click()
    hangqing_page.zhishu_btn.click()
    zhishu_page.down_glide()
    sleep(1)
    picName = '行情-指数_21'
    public_method.public_screenshot_as_file(picName=picName)

    # step22-30
    zhishu_page.gn_operation()

    # step31-40
    zhishu_page.guoneiZhishu_gengduo_btn.click()
    picName = '指数-国内指数－更多_31'
    public_method.public_screenshot_as_file(picName=picName)

    hangqing_gengduo_page.hq_left()
    hangqing_gengduo_page.hq_left()
    hangqing_gengduo_page.hq_right()
    hangqing_gengduo_page.hq_right()

    title = hangqing_gengduo_page.cell01_title.text
    #title = driver.find_element_by_xpath(
        #"//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]").text
    print "指数－国内指数－更多－第一行股票名称：", title
    hangqing_gengduo_page.cell01_click()
    assert fenshikxian_page.title_staText.text == title
    fenshikxian_page.change_gupiao(9)
    fenshikxian_page.fanhui_button.click()
    hangqing_gengduo_page.fanhui_btn.click()

#股指期货
def test_step41(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    zhishu_page = ZhishuPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    guzhiqihuo_gengduo_page = GuzhiQihuoGengduoPage(driver)
    public_method = PublicMethod(driver)
    debug_page = DebugPage(driver)

    # step2
    #debug_page.switch_server("112.17.10.145", "9528")
    public_page.hangqing_button.click()
    sleep(1)
    # step41-49
    hangqing_page.zhishu_btn.click()

    #zhishu_page.qh_operation()

    # step50-57
    zhishu_page.qihuo_gengduo_btn.click()
    picName = '指数-股指期货－更多_50'
    public_method.public_screenshot_as_file(picName=picName)

    # 加上会出错
    #title = guzhiqihuo_gengduo_page.cell1_1_title.text
    guzhiqihuo_gengduo_page.cell1_1_title.click()
    #assert fenshikxian_page.title_staText.text == title
    fenshikxian_page.change_gupiao(9)
    fenshikxian_page.fanhui_button.click()
    public_method.public_tap_element(guzhiqihuo_gengduo_page.hushen300_btn)
    picName = '指数-股指期货－更多-隐藏沪深300_51'
    public_method.public_screenshot_as_file(picName=picName)
    sleep(1)

    # step5
    title = guzhiqihuo_gengduo_page.cell1_1_title.text
    guzhiqihuo_gengduo_page.cell1_1.click()
    assert fenshikxian_page.title_staText.text == title
    fenshikxian_page.change_gupiao(9)
    fenshikxian_page.fanhui_button.click()
    public_method.public_tap_element(guzhiqihuo_gengduo_page.shangzheng50_btn)
    picName = '指数-股指期货－更多-隐藏上证50_52'
    public_method.public_screenshot_as_file(picName=picName)
    sleep(1)

    # step65-70
    title = guzhiqihuo_gengduo_page.cell1_1_title.text
    guzhiqihuo_gengduo_page.cell1_1.click()
    assert fenshikxian_page.title_staText.text == title
    fenshikxian_page.change_gupiao(9)
    fenshikxian_page.fanhui_button.click()
    public_method.public_tap_element(guzhiqihuo_gengduo_page.zhongzheng500_btn)
    picName = '指数-股指期货－更多-隐藏中证500_53'
    public_method.public_screenshot_as_file(picName=picName)

    # step71-75
    public_method.public_tap_element(guzhiqihuo_gengduo_page.zhongzheng500_btn)
    public_method.public_tap_element(guzhiqihuo_gengduo_page.shangzheng50_btn)
    public_method.public_tap_element(guzhiqihuo_gengduo_page.hushen300_btn)
    guzhiqihuo_gengduo_page.hushen300_btn.click()
    guzhiqihuo_gengduo_page.fanhui_btn.click()

#富时A50指数
def test_step76(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    zhishu_page = ZhishuPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    debug_page = DebugPage(driver)

    # step2
    #debug_page.switch_server("112.17.10.145", "9528")

    public_page.hangqing_button.click()
    sleep(1)
    hangqing_page.zhishu_btn.click()

    # step84-92，上滑动至其他指数可见
    zhishu_page.up_glide()

    # step76-83
    zhishu_page.fs_operation()

#其他指数
def test_step93(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    zhishu_page = ZhishuPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)
    public_method = PublicMethod(driver)
    debug_page = DebugPage(driver)

    # step2
    #debug_page.switch_server("112.17.10.145", "9528")

    public_page.hangqing_button.click()
    hangqing_page.zhishu_btn.click()

    # 上滑动至其他指数可见
    zhishu_page.up_glide()

    # step93-102
    zhishu_page.qt_operation()

    zhishu_page.qita_gengduo_btn.click()
    picName = '指数-其它指数-更多_93'
    public_method.public_screenshot_as_file(picName=picName)

    hangqing_gengduo_page.hq_left()
    hangqing_gengduo_page.hq_left()
    hangqing_gengduo_page.hq_right()
    hangqing_gengduo_page.hq_right()

    title = hangqing_gengduo_page.cell01_title.text
    hangqing_gengduo_page.cell01_title.click()
    assert fenshikxian_page.title_staText.text == title
    fenshikxian_page.change_gupiao(9)
    fenshikxian_page.fanhui_button.click()
    hangqing_gengduo_page.fanhui_btn.click()
