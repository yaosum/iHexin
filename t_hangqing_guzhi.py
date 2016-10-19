# -*- coding: utf-8 -*-
"""
前置条件:未登陆
"""
from time import sleep
from pages.public.public_page import PublicPage
from pages.hangqing.guzhi_page import GuzhiPage
from pages.zixuangu.kanZhulizijin_page import KanZhulizijinPage
from pages.public.denglu_page import DengluPage
from pages.hangqing.hangqing_page import HangqingPage
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.hangqing.guzhiQihuo_gengduo_page import GuzhiQihuoGengduoPage
from pages.hangqing.hangqing_gengduo_page import HangqingGengduoPage
"""
def test_step1(driver):
    public_page = PublicPage(driver)
    guzhi_page = GuzhiPage(driver)
    hangqing_page = HangqingPage(driver)

    #step2
    public_page.hangqing_button.click()
    hangqing_page.guzhi_btn.click()

    assert guzhi_page.guzhi_btn
    assert guzhi_page.guoneiZhishu_btn
    assert guzhi_page.qihuo_btn

def test_step3(driver):
    public_page = PublicPage(driver)
    guzhi_page = GuzhiPage(driver)
    kanzhulizijin_page = KanZhulizijinPage(driver)
    denglu_page = DengluPage(driver)
    hangqing_page = HangqingPage(driver)

    public_page.hangqing_button.click()
    hangqing_page.guzhi_btn.click()
    guzhi_page.kanzijin_btn.click()
    assert kanzhulizijin_page.kanzhulizijin_staticText

    #step4-5
    #kanzhulizijin_page.gengduo_button.click()

    #step6-7
    kanzhulizijin_page.zixuan_btn.click()
    kanzhulizijin_page.denglu_btn.click()
    denglu_page.guanbi_btn.click()
    #step9-20
    kanzhulizijin_page.hushen_btn.click()
    kanzhulizijin_page.hx_ergodic_hushen_zhibiao()
    kanzhulizijin_page.hangye_btn.click()
    kanzhulizijin_page.hx_ergodic_zhibiao()
    kanzhulizijin_page.gainian_btn.click()
    kanzhulizijin_page.hx_ergodic_zhibiao()


"""
def test_step21(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    guzhi_page = GuzhiPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)
    guzhiqihuo_gengduo_page = GuzhiQihuoGengduoPage(driver)

    public_page.hangqing_button.click()

    hangqing_page.guzhi_btn.click()

    #step22-30
    guzhi_page.gn_operation()
    fenshikxian_page.hx_left()
    fenshikxian_page.change_gupiao(6)
    fenshikxian_page.fanhui_button.click()

    #step31-40
    guzhi_page.guoneiZhishu_gengduo_btn.click()

    hangqing_gengduo_page.hq_left()
    hangqing_gengduo_page.hq_left()
    hangqing_gengduo_page.hq_right()
    hangqing_gengduo_page.hq_right()

    title = hangqing_gengduo_page.cell01_title.text
    hangqing_gengduo_page.cell01.click()
    assert fenshikxian_page.title_staText.text == title
    fenshikxian_page.change_gupiao(9)
    fenshikxian_page.fanhui_button.click()
    hangqing_gengduo_page.fanhui_btn.click()

    #step41-49
    hangqing_page.guzhi_btn.click()

    guzhi_page.qh_operation()
    fenshikxian_page.change_gupiao(9)
    fenshikxian_page.fanhui_button.click()

    #step50-57

    guzhi_page.qihuo_gengduo_btn.click()

    #加上会出错
    title = guzhiqihuo_gengduo_page.cell1_1_title.text
    guzhiqihuo_gengduo_page.cell1_1.click()
    assert fenshikxian_page.title_staText.text == title
    #fenshikxian_page.change_gupiao(9)
    fenshikxian_page.fanhui_button.click()
    guzhiqihuo_gengduo_page.hushen300_btn.click()
    #sleep(1)

    #step58-64
    title = guzhiqihuo_gengduo_page.cell1_1_title.text
    guzhiqihuo_gengduo_page.cell1_1.click()
    assert fenshikxian_page.title_staText.text == title
    #fenshikxian_page.change_gupiao(9)
    fenshikxian_page.fanhui_button.click()
    guzhiqihuo_gengduo_page.shangzheng50.click()
    sleep(1)

    #step65-70
    title = guzhiqihuo_gengduo_page.cell1_1_title.text
    guzhiqihuo_gengduo_page.cell1_1.click()
    assert fenshikxian_page.title_staText.text == title
    #fenshikxian_page.change_gupiao(9)
    fenshikxian_page.fanhui_button.click()

    #step71-75
    print(guzhiqihuo_gengduo_page.zhongzheng500)
    guzhiqihuo_gengduo_page.zhongzheng500.click()
    sleep(1)
    guzhiqihuo_gengduo_page.zhongzheng500.click()
    sleep(1)
    guzhiqihuo_gengduo_page.shangzheng50.click()
    sleep(1)
    guzhiqihuo_gengduo_page.hushen300_btn.click()
    sleep(1)
    guzhiqihuo_gengduo_page.fanhui_btn.click()

    #step76-83
    guzhi_page.fs_operation()
    #fenshikxian_page.change_gupiao(6)
    fenshikxian_page.fanhui_button.click()

    #step84-92，上滑动至其他指数可见
    el1 = driver.get_window_size()
    width = el1.get('width')
    height = el1.get('height')
    start_x = width * (344 / 375.0)
    start_y = height * (500 / 667.0)
    end_x = width * (344 / 375.0)
    end_y = height * (10 / 667.0)
    driver.swipe(start_x, start_y, end_x, end_y, duration=500)
    guzhi_page.qt_operation()
    fenshikxian_page.change_gupiao(9)
    fenshikxian_page.fanhui_button.click()

    #step93-102
    guzhi_page.qita_gengduo_btn.click()

    hangqing_gengduo_page.hq_left()
    hangqing_gengduo_page.hq_left()
    hangqing_gengduo_page.hq_right()
    hangqing_gengduo_page.hq_right()

    title = hangqing_gengduo_page.cell01_title.text
    hangqing_gengduo_page.cell01.click()
    assert fenshikxian_page.title_staText.text == title
    fenshikxian_page.change_gupiao(8)
    fenshikxian_page.fanhui_button.click()
    hangqing_gengduo_page.fanhui_btn.click()
    