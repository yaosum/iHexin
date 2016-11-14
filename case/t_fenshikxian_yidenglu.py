#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pages.fenshikxian.fenshikxian_wubaidang_page import QuanjingwubaidangPage
from pages.public.public_page import PublicPage
from pages.public.searchStock_page import SearchStockPage
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.shouye.home_page import HomePage
from pages.fenshikxian.fenshikxian_yujing_page import FenshikxianYujingPage
from pages.fenshikxian.fenshikxian_lungutang_page import FenshikxianLungutangPage
from pages.fenshikxian.fenshikxian_zhibiao_page import FenshikxianZhibiaoPage
from pages.public.public_method import PublicMethod
from pages.fenshikxian.fenshikxian_hengping_page import FenshikxianHengpingPage
from time import sleep
import random

from pages.zixuangu.optional_page import OptionalPage
"""
#分时页面
def test_step1_7(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    searchstock_page = SearchStockPage(driver)
    home_page = HomePage(driver)
    wubaidang_page = QuanjingwubaidangPage(driver)

    home_page.sousuo_button.click()
    sleep(1)
    args = ['300033']
    searchstock_page.hx_send_keys(args[0])
    # [截图]

    #弹出行情数据窗口
    el1 = driver.get_window_size()
    width = el1.get('width')
    height = el1.get('height')
    driver.tap([(width * 50 / 375.0, height * 100 / 667.0)])
    # [截图]
    fenshikxian_page.guanbi_btn.click()

    fenshikxian_page.mingxi_btn.click()
    fenshikxian_page.chengjiao_btn.click()
    if fenshikxian_page.wudang_btn:
        fenshikxian_page.wudang_btn.click()
    else:
        fenshikxian_page.shidang_btn.click()
        fenshikxian_page.quanjingwubaidang_btn.click()
        sleep(1)
        # [截图]
        assert wubaidang_page.wubaidang_title
        wubaidang_page.fanhui_btn.click()

    fenshikxian_page.fanhui_button.click()
"""
#预警 下单 论股堂
def test_step25_33(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    searchstock_page = SearchStockPage(driver)
    home_page = HomePage(driver)
    fenshikxian_yujing_page = FenshikxianYujingPage(driver)
    fenshikxian_lungutang_page = FenshikxianLungutangPage(driver)

    home_page.sousuo_button.click()
    sleep(1)
    args = ['881112']
    searchstock_page.hx_send_keys(args[0])
    sleep(1)

    #大盘(appium找不到其元素)

    #预警[截图]
    try:
        fenshikxian_page.yujing_btn.click()
        sleep(1)
        # [截图]
        fenshikxian_yujing_page.wodeyujing_btn.click()
        # [截图]
        if fenshikxian_yujing_page.info_staticText != None:
            fenshikxian_yujing_page.queding_btn.click()
        fenshikxian_yujing_page.tianjiayujing_btn.click()
        fenshikxian_yujing_page.fanhui_button.click()
    except:
        print "这只股票没有预警"

    #下单
    try:
       fenshikxian_page.xiadan_btn.click()
       el1 = driver.get_window_size()
       width = el1.get('width')
       height = el1.get('height')
       tap_x = width * (100 / 375.0)
       tap_y = height * (100 / 667.0)
       # driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
       fenshikxian_page.quxiaojiaoyi_btn.click()
    except:
        print "这只股票没有闪电下单"

    #论股堂
    try:
        fenshikxian_page.lungu_btn.click()
        # [截图]
        fenshikxian_lungutang_page.xuantie_btn.click()
        fenshikxian_lungutang_page.zuiretiezi_btn.click()
        # [截图]
        fenshikxian_lungutang_page.xuantie_btn.click()
        fenshikxian_lungutang_page.zuixintiezi_btn.click()
        fenshikxian_lungutang_page.fanhui_button.click()
    except:
        print "这只股票没有论股堂"

    #港股的刷新按钮
    try:
        fenshikxian_page.shuaxin_btn.click()
    except:
        print "这只股票没有刷新按钮"

"""
#k线指标切换
def test_step34_47(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    searchstock_page = SearchStockPage(driver)
    home_page = HomePage(driver)
    fenshikxian_zhibiao_page = FenshikxianZhibiaoPage(driver)
    public_method = PublicMethod(driver)

    home_page.sousuo_button.click()
    sleep(1)
    args = ['300033']
    searchstock_page.hx_send_keys(args[0])
    sleep(1)

    #k线页面
    fenshikxian_page.hx_left()
    sleep(1)
    fenshikxian_page.shezhi_btn.click()
    fenshikxian_zhibiao_page.tianjiazhibiao_btn.click()
    if fenshikxian_zhibiao_page.title.text == u'添加指标':
        # 添加指标
        cells = driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell')
        for cell in cells:
            cell.click()
        fenshikxian_zhibiao_page.fanhui_button.click()

    lenth = len(driver.find_elements_by_xpath("//UIATableCell[@name]"))
    print "指标个数 ＝", lenth
    fenshikxian_zhibiao_page.guanbi_btn.click()

    time_list = ['ri_btn', 'zhou_btn', 'yue_btn']
    fenzhong_list = ['oneMinute_btn', 'five_btn', 'fifteen_btn', 'thirty_btn', 'sixty_btn']
    el1 = driver.get_window_size()
    width = el1.get('width')
    height = el1.get('height')
    #k线放大缩小移动操作
    #日／周／月
    for time in time_list:
        print "k线周期 ＝ ", time
        eval('fenshikxian_page.{}.click()'.format(time))
        for n in range(2):
            print "第 " + str(n) + " 个指标"
            # [截图]
            fenshikxian_page.kxian_action_operation()

    fenshikxian_page.fenzhong_btn.click()
    #1分钟／5分钟／15分钟30分钟／60分钟／
    for fenzhon in fenzhong_list:
        print "k线周期 ＝", fenzhon
        eval('fenshikxian_page.{}.click()'.format(fenzhon))
        fenshikxian_page.fenzhong_btn.click()
        for n in range(2):
            print "第 " + str(n) + " 个指标"
            # [截图]
            fenshikxian_page.kxian_action_operation()
        eval('fenshikxian_page.{}.click()'.format(fenzhon))

#k线设置
def test_step48_63(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    searchstock_page = SearchStockPage(driver)
    home_page = HomePage(driver)
    fenshikxian_zhibiao_page = FenshikxianZhibiaoPage(driver)
    public_method = PublicMethod(driver)
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)

    home_page.sousuo_button.click()
    sleep(1)
    args = ['300033']
    searchstock_page.hx_send_keys(args[0])
    sleep(1)
    #进入k线页面
    fenshikxian_page.hx_left()
    sleep(1)
    fenshikxian_page.shezhi_btn.click()

    fenshikxian_zhibiao_page.kjunxian_shezhi_image.click()
    sleep(1)
    fenshikxian_zhibiao_page.fanhui_button.click()
    fenshikxian_zhibiao_page.quekou_xinxi_image.click()
    sleep(1)
    fenshikxian_zhibiao_page.fanhui_button.click()
    #除复权设置并放大缩小k线操作
    fenshikxian_zhibiao_page.chuquan_btn.click()
    fenshikxian_zhibiao_page.guanbi_btn.click()
    fenshikxian_page.kxian_action_operation()

    #选择前复权 关闭k线均线
    fenshikxian_page.shezhi_btn.click()
    fenshikxian_zhibiao_page.qianfuquan_btn.click()
    fenshikxian_zhibiao_page.kjunxian_switch.click()
    fenshikxian_zhibiao_page.guanbi_btn.click()
    fenshikxian_page.kxian_action_operation()

    #关闭k线均线设置 打开缺口
    fenshikxian_page.shezhi_btn.click()
    fenshikxian_zhibiao_page.kjunxian_switch.click()
    fenshikxian_zhibiao_page.quekou_switch.click()
    fenshikxian_zhibiao_page.guanbi_btn.click()
    fenshikxian_page.kxian_action_operation()

    #关闭缺口
    fenshikxian_page.shezhi_btn.click()
    fenshikxian_zhibiao_page.quekou_switch.click()
    fenshikxian_page.hx_left()

#分时 横屏
def test_step64_69(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    searchstock_page = SearchStockPage(driver)
    home_page = HomePage(driver)
    fenshikxian_hengping_page = FenshikxianHengpingPage(driver)
    wubaidang_page = QuanjingwubaidangPage(driver)

    home_page.sousuo_button.click()
    sleep(1)
    args = ['300033']
    searchstock_page.hx_send_keys(args[0])
    sleep(1)

    #分时
    fenshikxian_page.fenshi_qiehengping_btn.click()
    sleep(1)
    fenshikxian_hengping_page.hangqingshuju_btn.click()
    sleep(1)
    fenshikxian_hengping_page.guanbi_btn.click()
    sleep(1)
    fenshikxian_hengping_page.mingxi_btn.click()
    fenshikxian_hengping_page.chengjiao_btn.click()
    if fenshikxian_page.wudang_btn:
        fenshikxian_page.wudang_btn.click()
        fenshikxian_hengping_page.x_btn.click()
    else:
        fenshikxian_page.shidang_btn.click()
        fenshikxian_page.quanjingwubaidang_btn.click()
        sleep(1)
        # [截图]
        assert wubaidang_page.wubaidang_title
        wubaidang_page.fanhui_btn.click()
    fenshikxian_page.fanhui_button.click()

# k线 横屏
def test_step70(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    searchstock_page = SearchStockPage(driver)
    home_page = HomePage(driver)
    fenshikxian_hengping_page = FenshikxianHengpingPage(driver)

    home_page.sousuo_button.click()
    sleep(1)
    args = ['300033']
    searchstock_page.hx_send_keys(args[0])
    sleep(1)

    fenshikxian_page.hx_left()
    sleep(1)
    fenshikxian_page.kLine_qiehengping_btn.click()
    sleep(1)
    #k线
    fenshikxian_hengping_page.riK_btn.click()
    fenshikxian_hengping_page.hangqingshuju_btn.click()
    sleep(1)
    fenshikxian_hengping_page.guanbi_btn.click()
    sleep(1)

    fenshikxian_hengping_page.zhibiao_btn.click()
    zhibiao_length = len(driver.find_elements_by_xpath("//UIATableCell[@name]"))

    time_list = ['riK_btn', 'zhouK_btn', 'yueK_btn', 'sixty_btn']
    el1 = driver.get_window_size()
    width = el1.get('width')
    height = el1.get('height')

    #横屏里边点击更多弹出来的几个时间appium找不到元素,所以通过坐标的形式点击。横屏下，设备的长宽是相反的
    gengduo_list = [(width * 538/667.0, height * 320/375.0, "gengduo"),
                    (width * 538/667.0, height * 288/375.0, "oneminute"),
                    (width * 538/667.0, height * 258/375.0, "fiveminute"),
                    (width * 538/667.0, height * 226/375.0, "fifteenminute")]

    #日k／周k／月k／60分
    for time in time_list:
        print "横屏k线周期 ＝ ",time
        eval('fenshikxian_hengping_page.{}.click()'.format(time))
        for m in range(2):
            # [截图]
            print "第 " + str(m) + " 个指标"
            fenshikxian_hengping_page.kxian_action_operation()

    #1分钟／5分钟15分钟／30分钟／
    for x, y, btnname in gengduo_list:
        print "横屏k线周期 ＝ ",btnname
        eval("fenshikxian_hengping_page.{0}_btn.click()".format(btnname))
        driver.tap([(x, y)])
        for m in range(2):
            # [截图]
            print "第 " + str(m) + " 个指标"
            fenshikxian_hengping_page.kxian_action_operation()

    fenshikxian_hengping_page.x_btn.click()
    fenshikxian_page.fanhui_button.click()
    """