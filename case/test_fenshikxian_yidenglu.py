#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pages.public.searchStock_page import SearchStockPage
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.shouye.home_page import HomePage
from pages.fenshikxian.fenshikxian_yujing_page import FenshikxianYujingPage
from pages.fenshikxian.fenshikxian_lungutang_page import FenshikxianLungutangPage
from pages.fenshikxian.fenshikxian_zhibiao_page import FenshikxianZhibiaoPage
from pages.public.public_method import PublicMethod
from pages.fenshikxian.fenshikxian_hengping_page import FenshikxianHengpingPage


#分时页面
def tst_step1_7(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    searchstock_page = SearchStockPage(driver)
    home_page = HomePage(driver)

    home_page.sousuo_button.click()
    args = ['300033']
    searchstock_page.hx_send_keys(args)

    #进入行情数据
    el1 = driver.get_window_size()
    width = el1.get('width')
    height = el1.get('height')
    driver.tap([(width * 50 / 375.0, height * 100 / 667.0)])
    fenshikxian_page.guanbi_btn.click()

    fenshikxian_page.mingxi_btn.click()
    fenshikxian_page.chengjiao_btn.click()
    fenshikxian_page.wudang_btn.click()

#预警 下单 论股堂
def tst_step25_33(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    searchstock_page = SearchStockPage(driver)
    home_page = HomePage(driver)
    fenshikxian_yujing_page = FenshikxianYujingPage(driver)
    fenshikxian_lungutang_page = FenshikxianLungutangPage(driver)

    home_page.sousuo_button.click()
    args = ['300033']
    searchstock_page.hx_send_keys(args)

    #大盘(appium找不到其元素)

    #预警
    fenshikxian_page.yujing_btn.click()
    fenshikxian_yujing_page.wodeyujing_btn.click()
    if fenshikxian_yujing_page.info_staticText != None:
        fenshikxian_yujing_page.queding_btn.click()
    fenshikxian_yujing_page.tianjiayujing_btn.click()
    fenshikxian_yujing_page.fanhui_button.click()

    #下单
    fenshikxian_page.xiadan_btn.click()
    el1 = driver.get_window_size()
    width = el1.get('width')
    height = el1.get('height')
    tap_x = width * (100 / 375.0)
    tap_y = height * (100 / 667.0)
    driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})

    #论股堂
    fenshikxian_page.lungu_btn.click()
    fenshikxian_lungutang_page.xuantie_btn.click()
    fenshikxian_lungutang_page.zuiretiezi_btn.click()
    fenshikxian_lungutang_page.fanhui_button.click()

#k线指标切换
def test_step34_47(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    searchstock_page = SearchStockPage(driver)
    home_page = HomePage(driver)
    fenshikxian_zhibiao_page = FenshikxianZhibiaoPage(driver)
    public_method = PublicMethod(driver)

    home_page.sousuo_button.click()
    args = ['300033']
    searchstock_page.hx_send_keys(args)
    fenshikxian_page.hx_left()
    fenshikxian_page.shezhi_btn.click()
    fenshikxian_zhibiao_page.tianjiazhibiao_btn.click()
    if fenshikxian_zhibiao_page.title.text == u'添加指标':
        # 添加指标
        cells = driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell')
        for cell in cells:
            cell.click()
        fenshikxian_zhibiao_page.fanhui_button.click()

    lenth = len(driver.find_elements_by_xpath("//UIATableCell[@name]"))
    fenshikxian_zhibiao_page.guanbi_btn.click()

    time_list = ['ri_btn', 'zhou_btn', 'yue_btn', 'fenzhong_btn']
    fenzhong_list = ['oneMinu1irty_btn', 'sixty_btn']
    el1 = driver.get_window_size()
    width = el1.get('width')
    height = el1.get('height')
    #k线放大缩小移动操作
    for time in time_list:
        if time == u'fenzhong_btn':
            #分钟
            for fenzhong in fenzhong_list:
                fenshikxian_page.fenzhong_btn.click()
                eval('fenshikxian_page.{}.click()'.format(fenzhong))
                driver.tap([(width * 190 / 375.0, height * 300 / 667.0,)])
                for n in range(lenth):
                    fenshikxian_page.kxian_action_operation()
        else:
            #日 周 月
            eval('fenshikxian_page.{}.click()'.format(time))
            for n in range(lenth):
                fenshikxian_page.kxian_action_operation()

#k线设置
def tst_step48_63(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    searchstock_page = SearchStockPage(driver)
    home_page = HomePage(driver)
    fenshikxian_zhibiao_page = FenshikxianZhibiaoPage(driver)
    public_method = PublicMethod(driver)

    home_page.sousuo_button.click()
    args = ['300033']
    searchstock_page.hx_send_keys(args)
    fenshikxian_page.hx_left()
    fenshikxian_page.shezhi_btn.click()

    fenshikxian_zhibiao_page.kjunxian_shezhi_image.click()
    fenshikxian_zhibiao_page.fanhui_button.click()
    fenshikxian_zhibiao_page.quekou_xinxi_image.click()
    fenshikxian_zhibiao_page.fanhui_button.click()
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
def tst_step64_69(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    searchstock_page = SearchStockPage(driver)
    home_page = HomePage(driver)
    fenshikxian_hengping_page = FenshikxianHengpingPage(driver)

    home_page.sousuo_button.click()
    args = ['300033']
    searchstock_page.hx_send_keys(args)

    #分时
    el1 = driver.get_window_size()
    width = el1.get('width')
    height = el1.get('height')
    driver.tap([(width * 253/375.0,height * 486/667.0)])
    fenshikxian_hengping_page.hangqingshuju_btn.click()
    fenshikxian_hengping_page.guanbi_btn.click()
    fenshikxian_hengping_page.mingxi_btn.click()
    fenshikxian_hengping_page.chengjiao_btn.click()
    fenshikxian_hengping_page.wudang_btn.click()

    #k线
    fenshikxian_hengping_page.riK_btn.click()
    fenshikxian_hengping_page.hangqingshuju_btn.click()
    fenshikxian_hengping_page.guanbi_btn.click()
    fenshikxian_hengping_page.zhibiao_btn.click()
    zhibiao_lenth = len(driver.find_elements_by_xpath("//UIATableCell[@name]"))
    fenshikxian_hengping_page.zhibiao_cell01.click()

    time_list = ['riK_btn', 'zhouK_btn', 'yueK_btn', 'sixty_btn', 'gengduo_btn']

    #横屏里边点击更多弹出来的几个时间appium找不到元素,所以通过坐标的形式点击
    gengduo_list = [(width * 538/375.0, height * 320/667.0), (width * 538/375.0, height * 288/667.0), (width * 538/375.0, height * 258/667.0), (width * 538/375.0, height * 226/667.0)]
    for time in time_list:
        if time != u'gengduo_btn':
            eval('fenshikxian_hengping_page.{}.click()'.format(time))
            fenshikxian_hengping_page.zhibiao_cell01.click()
            for m in range(zhibiao_lenth):
                fenshikxian_hengping_page.kxian_action_operation()
        else:
            for x, y in gengduo_list:
                fenshikxian_hengping_page.gengduo_btn.click()
                driver.tap([(x, y)])
                if fenshikxian_hengping_page.gengduo_btn.text == u'更多':
                    print('分时k线横屏里边更多时间选择有问题。')
                fenshikxian_hengping_page.zhibiao_cell01.click()
                for m in range(zhibiao_lenth):
                    fenshikxian_hengping_page.kxian_action_operation()
    fenshikxian_hengping_page.x_btn.click()
    fenshikxian_page.kLine_qiehengping_btn.click()
    fenshikxian_hengping_page.fenshi_btn.click()
    fenshikxian_hengping_page.x_btn.click()
    fenshikxian_page.fanhui_button.click()