#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pages.fenshikxian.fenshikxian_wubaidang_page import QuanjingwubaidangPage
from time import sleep

from pages.hangqing.hangqing_gengduo_page import HangqingGengduoPage
from pages.public.denglu_page import DengluPage
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.shouye.home_page import HomePage
from pages.fenshikxian.fenshikxian_yujing_page import FenshikxianYujingPage
from pages.fenshikxian.fenshikxian_lungutang_page import FenshikxianLungutangPage
from pages.fenshikxian.fenshikxian_zhibiao_page import FenshikxianZhibiaoPage
from pages.fenshikxian.fenshikxian_hengping_page import FenshikxianHengpingPage
from pages.public.public_method import PublicMethod
from pages.zixuangu.zixun_page import ZixunPage
import random

case_name = 'test_fenshikxian_hengping'
args = ('600000', )

# 分时 横屏
def test_step64_69(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    fenshikxian_hengping_page = FenshikxianHengpingPage(driver)
    wubaidang_page = QuanjingwubaidangPage(driver)
    public_method = PublicMethod(driver)

    for arg in args:
        fenshikxian_page.searchtofenshi(arg)
        pic_name = '搜索-{}-分时_2'.format(arg)
        public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

        # 分时
        fenshikxian_page.fenshi_qiehengping_btn.click()
        pic_name = '搜索-分时-横屏_64'
        public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

        fenshikxian_hengping_page.hangqingshuju_btn.click()
        pic_name = '搜索-分时-横屏－报价头_65'
        public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
        fenshikxian_hengping_page.guanbi_btn.click()

        if fenshikxian_hengping_page.mingxi_btn:
            fenshikxian_hengping_page.mingxi_btn.click()
            pic_name = '搜索-分时-横屏-明细tab_67'
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

        if fenshikxian_hengping_page.chengjiao_btn:
            fenshikxian_hengping_page.chengjiao_btn.click()
            pic_name = '搜索-分时-横屏－成交tab_68'
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

        if fenshikxian_hengping_page.wudang_btn:
            fenshikxian_hengping_page.wudang_btn.click()
            pic_name = '搜索-分时-横屏－5档tab_69'
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
        else:
            fenshikxian_hengping_page.shidang_btn.click()
            pic_name = '搜索-分时-横屏-10档tab_69'
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
            if fenshikxian_hengping_page.wubaidang_btn:
                fenshikxian_hengping_page.wubaidang_btn.click()
                sleep(1)
                pic_name = '搜索-分时-横屏－500档_69'
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                assert wubaidang_page.wubaidang_title
                wubaidang_page.fanhui_btn.click()
        if fenshikxian_hengping_page.x_btn:
            fenshikxian_hengping_page.x_btn.click()
            sleep(1)

# k线横屏,日／周／月／分钟周期
def test_step69_70(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    fenshikxian_hengping_page = FenshikxianHengpingPage(driver)
    public_method = PublicMethod(driver)
    fenshikxian_zhibiao_page = FenshikxianZhibiaoPage(driver)

    fenshikxian_page.searchtofenshi(args[0])
    fenshikxian_page.hx_left()

    fenshikxian_page.shezhi_btn.click()
    pic_name = '搜索-分时-k线-设置_35'
    public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

    fenshikxian_zhibiao_page.tianjiazhibiao_btn.click()
    if fenshikxian_zhibiao_page.title.text == u'添加指标':
        # 添加指标
        cells = driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell')
        for cell in cells:
            cell.click()
        fenshikxian_zhibiao_page.fanhui_button.click()

    lenth = public_method.public_getlength()
    fenshikxian_zhibiao_page.guanbi_btn.click()

    fenshikxian_page.kLine_qiehengping_btn.click()
    sleep(1)
    pic_name = '搜索-分时-k线－横屏_70'
    public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

    # k线
    fenshikxian_hengping_page.hangqingshuju_btn.click()
    fenshikxian_hengping_page.guanbi_btn.click()
    fenshikxian_hengping_page.zhibiao_btn.click()

    fenshikxian_hengping_page.riK_btn.click()
    print "k线周期：日",
    for m in range(lenth):
        print "第 {} 个指标：".format(m)
        fenshikxian_hengping_page.kxian_action_operation()

    # 周 月 随机一个
    time_list = ['zhouK_btn', 'yueK_btn']
    cycle_1 = random.choice(time_list)
    eval('fenshikxian_hengping_page.{}.click()'.format(cycle_1))
    print "k线周期：", cycle_1
    for m in range(lenth):
        print "第 {} 个指标：".format(m)
        fenshikxian_hengping_page.kxian_action_operation()

    el1 = driver.get_window_size()
    width = el1.get('width')
    height = el1.get('height')

    # 分钟周期，横屏里边点击更多弹出来的几个时间appium找不到元素,所以通过坐标的形式点击，横屏下设备的长宽是相反的
    gengduo_list = [[width * 538 / 667.0, height * 320 / 375.0, 'oneminute'],
                    [width * 538 / 667.0, height * 288 / 375.0, 'fiveminute'],
                    [width * 538 / 667.0, height * 258 / 375.0, 'fifteenminute'],
                    [width * 538 / 667.0, height * 226 / 375.0, 'thirtyminute'],
                    [0, 0, 'sixtyminute']]
    cycle_2 = random.choice(gengduo_list)
    print "k线周期：{}".format(cycle_2[2])
    if cycle_2[2] == u'sixtyminute':
        fenshikxian_hengping_page.sixty_btn.click()
    else:
        fenshikxian_hengping_page.gengduo_btn.click()
        tap_x = cycle_2[0]
        tap_y = cycle_2[1]
        driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
    sleep(1)
    for m in range(lenth):
        print "第 {} 个指标：".format(m)
        fenshikxian_hengping_page.kxian_action_operation()

    fenshikxian_hengping_page.x_btn.click()
