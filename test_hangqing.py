# -*- coding: utf-8 -*-
"""
前置条件:未登陆
"""
from pages.public.public_page import PublicPage
from pages.hangqing.guzhi_page import GuzhiPage
from pages.zixuangu.kanZhulizijin_page import KanZhulizijinPage
from pages.public.denglu_page import DengluPage
from pages.hangqing.hangqing_page import HangqingPage
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.hangqing.gengduo_page_3 import GengduoPage3
from pages.hangqing.gengduo_page_7 import GengduoPage7
from pages.hangqing.guzhiQihuo_gengduo_page import GuzhiQihuoGengduoPage
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
    assert guzhi_page.fushiA50Qihuo_btn
    assert guzhi_page.qita_btn
"""
def test_step3(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    guzhi_page = GuzhiPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    kanzhulizijin_page = KanZhulizijinPage(driver)
    denglu_page = DengluPage(driver)
    gengduo_page_3 = GengduoPage3(driver)
    gengduo_page_7 = GengduoPage7(driver)
    guzhiqihuo_gengduo_page = GuzhiQihuoGengduoPage(driver)

    public_page.hangqing_button.click()
    """
    guzhi_page.kanzijin_btn.click()

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

    kanzhulizijin_page.fanhui_btn.click()
    """
    #step21
    hangqing_page.guzhi_btn.click()

    #step22-30
    guzhi_page.gn_operation()
    fenshikxian_page.hx_left()
    fenshikxian_page.change_gupiao(6)
    fenshikxian_page.fanhui_button.click()

    #step31-40
    guzhi_page.guoneiZhishu_gengduo_btn.click()
    gengduo_page_7.gd_left()
    gengduo_page_7.gd_left()
    gengduo_page_7.gd_right()
    gengduo_page_7.gd_right()
    gengduo_page_7.cell01.click()
    fenshikxian_page.change_gupiao(9)
    fenshikxian_page.hx_right()
    fenshikxian_page.fanhui_button.click()
    gengduo_page_7.fanhui_btn.click()

    #step41-49
    guzhi_page.qh_operation()
    fenshikxian_page.hx_left(9)
    fenshikxian_page.hx_left()
    fenshikxian_page.change_gupiao(9)
    fenshikxian_page.fanhui_button.click()

    #step50-57
    guzhi_page.qihuo_gengduo_btn.click()
    guzhiqihuo_gengduo_page.cell1_1.click()
    fenshikxian_page.change_gupiao(9)
    fenshikxian_page.hx_right()
    fenshikxian_page.fanhui_button.click()
    guzhiqihuo_gengduo_page.hushen300_btn.click()

    #step58-64
    guzhiqihuo_gengduo_page.cell2_1.click()
    fenshikxian_page.change_gupiao(9)
    fenshikxian_page.hx_right()
    fenshikxian_page.fanhui_button.click()
    guzhiqihuo_gengduo_page.shangzheng50.click()

    #step65-70
    guzhiqihuo_gengduo_page.cell3_1.click()
    fenshikxian_page.change_gupiao(9)
    fenshikxian_page.hx_right()
    fenshikxian_page.fanhui_button.click()

    #step71-75
    guzhiqihuo_gengduo_page.zhongzheng500.click()
    guzhiqihuo_gengduo_page.zhongzheng500.click()
    guzhiqihuo_gengduo_page.shangzheng50.click()
    guzhiqihuo_gengduo_page.hushen300_btn.click()
    guzhiqihuo_gengduo_page.fanhui_btn.click()

    #step76-83
    guzhi_page.fs_operation()
    fenshikxian_page.change_gupiao(6)
    fenshikxian_page.fanhui_button.click()

    #step84-92
    guzhi_page.qt_operation()
    fenshikxian_page.hx_left(9)
    fenshikxian_page.hx_left()
    fenshikxian_page.change_gupiao(9)
    fenshikxian_page.fanhui_button.click()

    #step93-102
    guzhi_page.qita_gengduo_btn.click()
    gengduo_page_7.gd_left()
    gengduo_page_7.gd_left()
    gengduo_page_7.gd_right()
    gengduo_page_7.gd_right()
    gengduo_page_7.cell01.click()
    fenshikxian_page.change_gupiao(8)
    fenshikxian_page.hx_right()
    fenshikxian_page.fanhui_button.click()
    gengduo_page_7.fanhui_btn.click()






