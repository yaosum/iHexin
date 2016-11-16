# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException, WebDriverException

from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.hangqing.ahbijiagu_page import AHBijiaguPage
from pages.hangqing.hangqing_gengduo_page import HangqingGengduoPage
from pages.hangqing.hushen_page import HushenPage
from pages.hangqing.zhangtinfenxi_page import ZhangtinfenxiPage
from pages.public.debug_page import DebugPage
from pages.public.public_method import PublicMethod
from pages.public.public_page import PublicPage
from pages.hangqing.hangqing_page import HangqingPage
from pages.shouye.home_page import HomePage
from pages.public.public_method import PublicMethod
from time import sleep

caseName = 'test_hangqing_hushen'
def test_step1(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    hushen_page = HushenPage(driver)
    public_method = PublicMethod(driver)
    debug_page = DebugPage(driver)

    debug_page.switch_server("112.17.10.145", "9528")

    public_page.hangqing_button.click()
    assert hangqing_page.hushen_btn
    hangqing_page.hushen_btn.click()
    picName = '行情-沪深_3'
    public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
    assert hushen_page.hushen_title

#第一行单元格
def test_step4(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    hushen_page = HushenPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    debug_page = DebugPage(driver)

    debug_page.switch_server("112.17.10.145", "9528")

    public_page.hangqing_button.click()
    hangqing_page.hushen_btn.click()

    zhishuname = ["szzs", "szcz"]
    for name in zhishuname:
        eval('hushen_page.{0}_btn.click()'.format(name))
        assert fenshikxian_page.sousuo_btn
        fenshikxian_page.hx_left()
        assert fenshikxian_page.shezhi_btn
        fenshikxian_page.hx_right()
        fenshikxian_page.fanhui_button.click()

#ah比价股
def test_step12(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    hushen_page = HushenPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    ahbijiagu_page = AHBijiaguPage(driver)
    public_method = PublicMethod(driver)
    debug_page = DebugPage(driver)

    debug_page.switch_server("112.17.10.145", "9528")

    public_page.hangqing_button.click()
    hangqing_page.hushen_btn.click()

    hushen_page.ahbijia_btn.click()
    picName = '沪深-AH股比价_12'
    public_method.public_screenshot_as_file(caseName=caseName, picName=picName)

    assert ahbijiagu_page.ahbijia_title
    assert ahbijiagu_page.shuaxin_btn
    assert ahbijiagu_page.sousuo_btn
    #assert ahbijiagu_page.wenben_text

    #ahbijiagu_page.xiaochuwenben_btn.click()

    ahbijiagu_page.hq_up()
    ahbijiagu_page.hq_down()

    ahbijiagu_page.zuixin_btn.click()
    ahbijiagu_page.zuixin_btn.click()
    ahbijiagu_page.zhangfu_btn.click()
    ahbijiagu_page.zhangfu_btn.click()
    ahbijiagu_page.yijialv_btn.click()
    ahbijiagu_page.yijialv_btn.click()

    length = int(len(driver.find_elements_by_xpath("//UIATableView[1]/UIATableCell[@name]")))
    title = ahbijiagu_page.cell01_title.text
    ahbijiagu_page.cell01_btn.click()
    assert fenshikxian_page.title_staText.text == title
    fenshikxian_page.change_gupiao(length - 1)
    fenshikxian_page.fanhui_button.click()
    ahbijiagu_page.fanhui_btn.click()
    assert hushen_page.hushen_title

#涨停分析
def test_step26(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    hushen_page = HushenPage(driver)
    zhangtinfenxi_page = ZhangtinfenxiPage(driver)
    public_method = PublicMethod(driver)
    debug_page = DebugPage(driver)

    debug_page.switch_server("112.17.10.145", "9528")

    public_page.hangqing_button.click()
    hangqing_page.hushen_btn.click()

    hushen_page.zhangtinfenxi_btn.click()
    picName = '沪深-涨停分析_26'
    public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
    assert zhangtinfenxi_page.zhangtinfenxi_title
    assert zhangtinfenxi_page.sousuo_btn
    zhangtinfenxi_page.fanhui_btn.click()

def test_step29(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    hushen_page = HushenPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)
    public_method = PublicMethod(driver)
    debug_page = DebugPage(driver)

    debug_page.switch_server("112.17.10.145", "9528")

    public_page.hangqing_button.click()
    hangqing_page.hushen_btn.click()
    hushen_page.zfb_shousuo_btn.click()
    hushenname = [("zfb", '涨幅榜更多'), ("dfb", '跌幅榜更多'), ("kszf", '5分钟涨幅更多'), ("hslb" ,'换手率榜更多'),
                  ("lbb", '量比榜更多'), ("cjeb", '成交额榜更多')]

    for name, gengduo in hushenname:
        eval('public_method.public_tap_element(hushen_page.{0}_shousuo_btn)'.format(name))
        sleep(1)
        title = hushen_page.hs_cell1_title.text
        hushen_page.cell1_btn.click()
        assert fenshikxian_page.title_staText.text == title
        fenshikxian_page.change_gupiao(10)
        fenshikxian_page.fanhui_button.click()

        eval('hushen_page.{0}_gengduo_btn.click()'.format(name))
        picName = '行情-{}_'.format(gengduo)
        public_method.public_screenshot_as_file(caseName=caseName, picName=picName)

        hangqing_gengduo_page.hq_left()
        hangqing_gengduo_page.hq_right()
        hangqing_gengduo_page.hq_up()
        hangqing_gengduo_page.hq_down()
        hangqing_gengduo_page.hq_down()
        #hangqing_gengduo_page.hs_clickOperation()

        #title = hangqing_gengduo_page.cell01_title.text
        hangqing_gengduo_page.cell01_click()
        #assert fenshikxian_page.title_staText.text == title
        fenshikxian_page.change_gupiao(10)
        fenshikxian_page.fanhui_button.click()

        hangqing_gengduo_page.fanhui_btn.click()
        eval('public_method.public_tap_element(hushen_page.{0}_shousuo_btn)'.format(name))

    for name, b in hushenname[:: -1]:
        eval('public_method.public_tap_element(hushen_page.{0}_shousuo_btn)'.format(name))
