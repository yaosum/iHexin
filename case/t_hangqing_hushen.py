# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException, WebDriverException

from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.hangqing.ahbijiagu_page import AHBijiaguPage
from pages.hangqing.hangqing_gengduo_page import HangqingGengduoPage
from pages.hangqing.hushen_page import HushenPage
from pages.hangqing.zhangtinfenxi_page import ZhangtinfenxiPage
from pages.public.public_method import PublicMethod
from pages.public.public_page import PublicPage
from pages.hangqing.hangqing_page import HangqingPage
from pages.shouye.home_page import HomePage
from time import sleep

def test_step1(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    hushen_page = HushenPage(driver)

    public_page.hangqing_button.click()
    assert hangqing_page.hushen_btn
    hangqing_page.hushen_btn.click()
    assert hushen_page.hushen_title

#第一行单元格
def test_step4(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    hushen_page = HushenPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)

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

    public_page.hangqing_button.click()
    hangqing_page.hushen_btn.click()

    hushen_page.ahbijia_btn.click()
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

    public_page.hangqing_button.click()
    hangqing_page.hushen_btn.click()

    hushen_page.zhangtinfenxi_btn.click()
    assert zhangtinfenxi_page.zhangtinfenxi_title
    assert zhangtinfenxi_page.sousuo_btn
    driver.get_screenshot_as_base64()
    zhangtinfenxi_page.fanhui_btn.click()

def test_step29(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    hushen_page = HushenPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)
    public_method = PublicMethod(driver)

    public_page.hangqing_button.click()
    hangqing_page.hushen_btn.click()
    hushen_page.zfb_shousuo_btn.click()
    hushenname = ["zfb", "dfb", "kszf", "hslb", "lbb", "cjeb"]

    for name in hushenname:
        eval('hushen_page.{0}_shousuo_btn.click()'.format(name))
        sleep(1)
        title = hushen_page.hs_cell1_title.text
        hushen_page.cell1_btn.click()
        assert fenshikxian_page.title_staText.text == title
        fenshikxian_page.change_gupiao(10)
        fenshikxian_page.fanhui_button.click()

        eval('hushen_page.{0}_gengduo_btn.click()'.format(name))
        for i in range(8):
            hangqing_gengduo_page.hq_left()
        hangqing_gengduo_page.hq_up()
        hangqing_gengduo_page.hq_down()
        hangqing_gengduo_page.hq_down()
        #hangqing_gengduo_page.hs_clickOperation()

        el1 = driver.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (42 / 375.0)
        tap_y = height * (124 / 667.0)
        #title = hangqing_gengduo_page.cell01_title.text
        driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
        #assert fenshikxian_page.title_staText.text == title
        fenshikxian_page.change_gupiao(10)
        fenshikxian_page.fanhui_button.click()

        hangqing_gengduo_page.fanhui_btn.click()
        eval('hushen_page.{0}_shousuo_btn.click()'.format(name))

    for name in hushenname[:: -1]:
        eval('public_method.hx_tap_element(hushen_page.{0}_shousuo_btn)'.format(name))



