#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from page_object.appium_page_objects import PageObject, page_element
import types
from time import sleep
from pages.public.public_method import PublicMethod
from pages.public.searchStock_page import SearchStockPage
from pages.shouye.home_page import HomePage
from pages.zixuangu.zixun_page import ZixunPage


class FenshiKxianPage(PageObject):
    """
    分时k线页面的相关元素及操作
    """
    fanhui_button = page_element(accessibility_id = '返回')
    xiayigegupiao_button = page_element(accessibility_id = '下一个股票')
    # 股票名称
    title_staText = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAScrollView[1]/UIAStaticText[1]')
    shangyigegupiao_button = page_element(accessibility_id = '上一个股票')
    sousuo_btn = page_element(accessibility_id="搜索")

    # k线
    klineTabButton = page_element(accessibility_id='KlineTabButtonBackground')
    zhankai_btn = page_element(accessibility_id='展开菜单')
    shouqi_btn = page_element(accessibility_id='收起菜单')
    fangda_btn = page_element(accessibility_id='k线放大')
    suoxiao_btn = page_element(accessibility_id='k线缩小')
    zuoyi_btn = page_element(accessibility_id='k线左移')
    youyi_btn = page_element(accessibility_id='k线右移')
    kLine_qiehengping_btn = page_element(accessibility_id='切换横屏')
    # k线周期
    ri_btn = page_element(accessibility_id='日')
    zhou_btn = page_element(accessibility_id='周')
    yue_btn = page_element(accessibility_id='月')

    fenzhon_btn = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[14]')
    one_btn = page_element(accessibility_id='1分')
    five_btn = page_element(accessibility_id='5分')
    fifteen_btn = page_element(accessibility_id='15分')
    thirty_btn = page_element(accessibility_id='30分')
    sixty_btn = page_element(accessibility_id='60分')

    zhibiao_name_btn = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[9]')
    shezhi_btn = page_element(accessibility_id='设置')

    # 分时
    wudang_btn = page_element(accessibility_id='五档')
    mingxi_btn = page_element(accessibility_id='明细')
    chengjiao_btn = page_element(accessibility_id='成交')
    #十档按钮
    shidang_btn = page_element(xpath = "//UIAButton[@name='十档']")
    quanjingwubaidang_btn = page_element(accessibility_id = '全景500档')
    #分时切换横屏按钮
    fenshi_qiehengping_btn = page_element(xpath = "//UIAButton[@name='toLandscape']")

    yujing_btn = page_element(accessibility_id='预警')
    xiadan_btn = page_element(accessibility_id='下单')
    lungu_btn = page_element(accessibility_id='论股')
    shuaxin_btn = page_element(accessibility_id = '刷新')
    kaihu_btn = page_element(accessibility_id = '开户')
    pinzhonggaishu_btn = page_element(accessibility_id = '品种概述')

    jiazixuan_staText = page_element(accessibility_id='加自选')

    # 闪电下单
    quickbuy_btn = page_element(accessibility_id = 'xiadan QuickBuy')
    quicksell_btn = page_element(accessibility_id = 'xiadan QuickSell')
    chedan_btn = page_element(accessibility_id = 'xiadan CheDanChaXun')
    qujiaoyi_btn = page_element(accessibility_id = '去交易下单')
    quxiaojiaoyi_btn = page_element(accessibility_id = '取 消')

    # 行情数据
    hangqingshuju_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAButton[2]')
    guanbi_btn = page_element(accessibility_id = '关闭')

    #分时tab
    maimaiduilie_tab_btn = page_element(xpath="//UIAButton[@name='买卖队列']")
    xinwen_tab_btn = page_element(xpath = "//UIAButton[@name='新闻']")
    pankou_tab_btn = page_element(xpath="//UIAButton[@name='盘口']")
    gonggao_tab_btn = page_element(xpath="//UIAButton[@name='公告']")
    jiankuang_tab_btn = page_element(xpath="//UIAButton[@name='简况(F10)']")
    zhengu_tab_btn = page_element(xpath="//UIAButton[@name='诊股']")
    caiwu_tab_btn = page_element(xpath="//UIAButton[@name='财务']")
    yanbao_tab_btn = page_element(xpath="//UIAButton[@name='研报']")
    zhangfubang_tab_btn = page_element(xpath="//UIAButton[@name='涨幅榜']")
    diefubang_tab_btn = page_element(xpath="//UIAButton[@name='跌幅榜']")
    gainianjiexi_tab_btn = page_element(xpath="//UIAButton[@name='概念解析']")
    # 新闻／研报tab下的第一条资讯(港美股特殊处理)
    zixun_cell01 = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIATableView[1]"
                "/UIATableCell[1]")
    zixun_cell01_title = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIATableView[1]"
              "/UIATableCell[1]/UIAStaticText[1]")
    hkus_zixun_cell01 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIATableView[1]"
              "/UIATableCell[1]")
    hkus_zixun_cell01_title = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIATableView[1]"
              "/UIATableCell[1]/UIAStaticText[1]")
    # 公告下的第一条查看公告(港美股特殊处理)
    chakangonggao_cell01 = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAWebView[1]/UIALink[1]")
    hkus_gonggao_cell01 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIAWebView[1]/UIALink[1]")
    hkus_gonggao_cell01_title = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIAWebView[1]/UIALink[1]/UIAStaticText[1]")
    # 公告列表下的第一条公告
    gonggao_cell01 = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAWebView[1]/UIALink[4]")
    gonggao_cell01_title = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAWebView[1]UIALink[4]/UIAStaticText[1]")

    longhubang_btn = page_element(
        xpath = "//UIAWebView[1]/UIAStaticText[8]")
    dazongjiaoyi_btn = page_element(
        xpath = "//UIAWebView[1]/UIAStaticText[9]")
    rongzirongquan_btn = page_element(
        xpath = "//UIAWebView[1]/UIAStaticText[10]")
    iwendongmi_btn = page_element(
        xpath = "//UIAWebView[1]/UIAStaticText[11]")

    # 港美股下的广告运营位
    hkus_yunyingwei = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]")

    # 财务/简况下的更多(港美股特殊处理)
    caiwu_cell01 = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]"
                "/UIAWebView[1]/UIALink[1]/UIALink[1]/UIALink[1]")
    caiwu_cell02 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]"
              "/UIAWebView[1]/UIALink[2]/UIALink[1]/UIALink[1]")
    caiwu_cell03 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]"
              "/UIAWebView[1]/UIALink[3]/UIALink[1]/UIALink[1]")
    caiwu_cell04 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]"
              "/UIAWebView[1]/UIALink[4]/UIALink[1]/UIALink[1]")
    caiwu_cell05 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]"
              "/UIAWebView[1]/UIALink[5]/UIALink[1]/UIALink[1]")
    caiwu_cell06 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]"
              "/UIAWebView[1]/UIALink[7]/UIALink[1]/UIALink[1]")
    caiwu_cell07 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]"
              "/UIAWebView[1]/UIALink[8]/UIALink[1]/UIALink[1]")
    caiwu_cell08 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]"
              "/UIAWebView[1]/UIALink[9]/UIALink[1]/UIALink[1]")
    caiwu_cell09 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]"
              "/UIAWebView[1]/UIALink[10]/UIALink[1]/UIALink[1]")
    caiwu_cell10 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]"
              "/UIAWebView[1]/UIALink[16]/UIALink[1]/UIALink[1]")
    # 港美股下简况列表
    hkus_jiankuang_cell01 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]"
              "/UIAWebView[1]/UIALink[1]/UIALink[1]/UIALink[1]")
    hkus_jiankuang_cell02 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]"
              "/UIAWebView[1]UIALink[2]/UIALink[1]/UIALink[1]")
    hkus_jiankuang_cell03 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]"
              "/UIAWebView[1]UIALink[3]/UIALink[1]/UIALink[1]")
    hkus_jiankuang_cell04 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]"
              "/UIAWebView[1]UIALink[4]/UIALink[1]/UIALink[1]")
    hkus_jiankuang_cell05 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]"
              "/UIAWebView[1]UIALink[5]/UIALink[1]/UIALink[1]")
    hkus_jiankuang_cell06 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]"
              "/UIAWebView[1]UIALink[6]/UIALink[1]/UIALink[1]")
    hkus_jiankuang_cell07 = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]"
              "/UIAWebView[1]/UIALink[7]/UIALink[1]/UIALink[1]")

    # 港美股下财务列表
    hkus_caiwu_cell01 = page_element(
        xpath="//UIAWebView[1]/UIALink[1]/UIALink[1]/UIALink[1]/UIALink[1]")
    hkus_caiwu_cell02 = page_element(
        xpath="//UIAWebView[1]/UIALink[2]/UIALink[1]/UIALink[1]/UIALink[1]")
    hkus_caiwu_cell03 = page_element(
        xpath="//UIAWebView[1]/UIALink[3]/UIALink[1]/UIALink[1]/UIALink[1]")
    hkus_caiwu_cell04 = page_element(
        xpath="//UIAWebView[1]/UIALink[4]/UIALink[1]/UIALink[1]/UIALink[1]")

    # 盘口下的第一个板块按钮
    pankou_bankuai_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIATableView[1]"
                "/UIATableCell[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]")

    # 涨幅榜/跌幅榜下第一个元素
    gupaio_cell001_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIATableView[1]"
                "/UIATableCell[1]")
    gengduogupiao_btn = page_element(accessibility_id = "点击查看更多股票")


    def hx_right(self):
        """
        向右滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (67 / 375.0)
        start_y = height * (134 / 667.0)
        end_x = width * (344 / 375.0)
        end_y = height * (134 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hx_left(self):
        """
        向左滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (344 / 375.0)
        start_y = height * (134 / 667.0)
        end_x = width * (67 / 375.0)
        end_y = height * (134 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hx_up(self):
        """
        向上滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (188 / 375.0)
        start_y = height * (500 / 667.0)
        end_x = width * (188 / 375.0)
        end_y = height * (140 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    # 切换股票,切换分时和k线
    def change_gupiao(self, count):
        """
        上一只股票／下一只股票的切换操作：先切换下一只股票count次，滑动至k线页面切换上一只股票count次，滑动至分时页面
        :param count: 切换股票的次数
        :return:
        """
        if type(count) is types.IntType:
            for n in range(count):
                self.xiayigegupiao_button.click()
            self.hx_left()
            sleep(1)
            for m in range(count):
                self.shangyigegupiao_button.click()
            self.hx_right()
        else:
            print('分时k线切换股票次数输入参数错误')

    def kxian_action_operation(self):
        """
        k线放大 缩小 左移 右移操作
        :return:
        """
        public_method = PublicMethod(self.w)
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        if self.zhankai_btn:
            self.zhankai_btn.click()
        public_method.public_longPress(self.fangda_btn, 1)
        public_method.public_longPress(self.suoxiao_btn, 1)
        public_method.public_longPress(self.zuoyi_btn, 1)
        public_method.public_longPress(self.youyi_btn, 1)
        self.w.tap([(width * 190 / 375.0, height * 572 / 667.0,)])

    def shuping_hqsj_click(self):
        """
        竖屏下点击行情数据
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        self.w.tap([(width * 50 / 375.0, height * 90 / 667.0)])

    def searchtofenshi(self, arg):
        """
        在有搜索按钮的页面，点击搜索，输入股票代码并进入相应股票分时页面
        :param arg: 股票代码
        :return:
        """
        searchstock_page = SearchStockPage(self.w)
        fenshikxian_page = FenshiKxianPage(self.w)
        home_page = HomePage(self.w)
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (193 / 375.0)
        tap_y = height * (84 / 667.0)

        home_page.sousuo_button.click()
        sleep(1)
        searchstock_page.hx_send_keys(arg)
        sleep(1)
        if not fenshikxian_page.sousuo_btn:
            self.w.execute_script("mobile: tap",
                                  {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
            sleep(1)
        if not fenshikxian_page.sousuo_btn:
            tap_x = width * (193 / 375.0)
            tap_y = height * (130 / 667.0)
            self.w.execute_script("mobile: tap",
                                  {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
            sleep(1)

    def qiehuanmingxi(self):
        """
        切换买卖档、明细、成交
        :return:
        """
        public_method = PublicMethod(self.w)
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (311 / 375.0)
        tap_y = height * (308 / 667.0)
        if self.mingxi_btn:
            for i in range(3):
                self.w.tap([(tap_x, tap_y)])
                pic_name = '搜索-分时-明细/成交/五档_8/9/10'
                public_method.public_screenshot_as_file(caseName="test_fenshikxian_yidenglu", picName=pic_name)

    def zhibiaoqiehuan_up_click(self):
        """
        向上切换分时指标
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (65 / 375.0)
        tap_y = height * (428 / 667.0)
        self.w.tap([(tap_x, tap_y)])

    def zhibiaoqiehuan_down_click(self):
        """
        向下切换分时指标
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (65 / 375.0)
        tap_y = height * (480 / 667.0)
        self.w.tap([(tap_x, tap_y)])

    def chengjiaoeliang_click(self):
        """
             切换成交额和成交量
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (176 / 375.0)
        tap_y = height * (456 / 667.0)
        self.w.tap([(tap_x, tap_y)])

    def zixun_celln_click(self):
        """
        资讯列表随机一行对象
        :return:
        """
        zixun_page = ZixunPage(self.w)
        public_method = PublicMethod(self.w)

        for i in range(7):
            self.hx_up()
        lenth = len(self.w.find_elements_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/"
                                                  "UIATableView[1]/UIATableCell[2]/UIATableView[1]/UIATableCell[@name]"))
        if lenth > 3:
            num = random.randint(2, lenth-1)
            print "普通股票新闻/研报列表随机数：{}, 普通股票新闻/研报列表长度：{}".format(num, lenth)
            celln = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIATableView[1]"
                "/UIATableCell[{}]".format(num))
            celln_title = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIATableView[1]"
                "/UIATableCell[{}]/UIAStaticText[1]".format(num))
            celln_title.click()
            sleep(1)
            pic_name = '搜索-分时-新闻/研报-资讯详情{}_9'.format(num)
            public_method.public_screenshot_as_file(caseName="test_fenshikxian_yidenglu", picName=pic_name)
            assert zixun_page.shoucang_btn
            assert zixun_page.fenxiang_btn
            assert zixun_page.shezhi_btn
            assert zixun_page.xiangqing_title.text == celln_title.text

    def zixun_celllast_click(self):
        """
        返回资讯列表最后一行对象
        :return:
        """
        zixun_page = ZixunPage(self.w)
        public_method = PublicMethod(self.w)

        length = len(self.w.find_elements_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]"
                                                   "/UIATableCell[2]/UIATableView[1]/UIATableCell[@name]"))
        print "普通股票新闻/研报列表长度：{}".format(length)
        if length > 1:
            celllast = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIATableView[1]"
                "/UIATableCell[{}]".format(length))

            celllast_title = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIATableView[1]"
                "/UIATableCell[{}]/UIAStaticText[1]".format(length))
            celllast.click()
            sleep(1)
            pic_name = '搜索-分时-新闻/研报-资讯详情{}_9'.format(length)
            public_method.public_screenshot_as_file(caseName="test_fenshikxian_yidenglu", picName=pic_name)
            assert zixun_page.shoucang_btn
            assert zixun_page.fenxiang_btn
            assert zixun_page.shezhi_btn
            assert zixun_page.xiangqing_title.text == celllast_title.text

    def hkus_zixun_celln_click(self):
        """
        点击资讯列表随机一行对象
        :return:
        """
        zixun_page = ZixunPage(self.w)
        public_method = PublicMethod(self.w)

        for i in range(7):
            self.hx_up()
        length = len(self.w.find_elements_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]"
                                                   "/UIATableCell[3]/UIATableView[1]/UIATableCell[@name]"))
        if length > 3:
            num = random.randint(2, length-1)
            print "港美股新闻列表随机数：{}, 港美股新闻列表长度：{}".format(num, length)
            celln = self.w.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/"
                                                 "UIATableCell[3]/UIATableView[1]/UIATableCell[{}]".format(num))
            celln_title = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIATableView[1]"
                "/UIATableCell[{}]/UIAStaticText[1]".format(num)).text
            celln.click()
            sleep(1)
            pic_name = '搜索-分时-新闻/研报-资讯详情{}_9'.format(num)
            public_method.public_screenshot_as_file(caseName="test_fenshikxian_yidenglu", picName=pic_name)
            assert zixun_page.shoucang_btn
            assert zixun_page.fenxiang_btn
            assert zixun_page.shezhi_btn
            assert zixun_page.xiangqing_title.text == celln_title

    def hkus_zixun_celllast_click(self):
        """
        点击资讯列表最后一行对象
        :return:
        """
        zixun_page = ZixunPage(self.w)
        public_method = PublicMethod(self.w)

        length = len(self.w.find_elements_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]"
                                                   "/UIATableCell[3]/UIATableView[1]/UIATableCell[@name]"))
        print "港美股新闻列表长度：{}".format(length)
        if length > 1:
            celllast = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIATableView[1]"
                "/UIATableCell[{}]".format(length))

            celllast_title = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIATableView[1]"
                "/UIATableCell[{}]/UIAStaticText[1]".format(length)).text
            celllast.click()
            sleep(1)
            pic_name = '搜索-分时-新闻/研报-资讯详情{}_9'.format(length)
            public_method.public_screenshot_as_file(caseName="test_fenshikxian_yidenglu", picName=pic_name)
            assert zixun_page.shoucang_btn
            assert zixun_page.fenxiang_btn
            assert zixun_page.shezhi_btn
            assert zixun_page.xiangqing_title.text == celllast_title

    def gonggao_celln_click(self):
        """
        点击公告列表随机一行对象
        :return:
        """
        zixun_page = ZixunPage(self.w)
        public_method = PublicMethod(self.w)

        for i in range(7):
            self.hx_up()
        length = len(self.w.find_elements_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/"
                                                   "UIATableCell[2]/UIAWebView[1]/UIALink[@name]"))
        if length > 50:
            length = 50

        if length > 3:
            num = random.randint(3, length-1)
            print "随机数：{}, 列表长度：{}".format(num, length)
            celln = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/"
                "UIAWebView[1]/UIALink[{}]".format(num))
            celln_title = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAWebView[1]"
                "/UIALink[{}]/UIAStaticText[1]".format(num)).text
            celln.click()
            sleep(1)
            pic_name = '搜索-分时-公告-资讯详情{}_17'.format(length)
            public_method.public_screenshot_as_file(caseName="test_fenshikxian_yidenglu", picName=pic_name)
            assert zixun_page.shoucang_btn
            assert zixun_page.fenxiang_btn
            assert zixun_page.xiangqing_title.text == celln_title

    def gonggao_celllast_click(self):
        """
        点击公告列表最后一行对象
        :return:
        """
        zixun_page = ZixunPage(self.w)
        public_method = PublicMethod(self.w)

        length = len(self.w.find_elements_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAWebView[1]"
            "/UIALink[@name]"))
        print "列表长度：{}".format(length)

        if length > 50:
            length = 50
        if length > 3:
            celllast = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/"
                "UIAWebView[1]/UIALink[{}]".format(length))

            celllast_title = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAWebView[1]"
                "/UIALink[{}]/UIAStaticText[1]".format(length)).text
            celllast.click()
            sleep(1)
            pic_name = '搜索-分时-公告-资讯详情{}_19'.format(length)
            public_method.public_screenshot_as_file(caseName="test_fenshikxian_yidenglu", picName=pic_name)
            assert zixun_page.shoucang_btn
            assert zixun_page.fenxiang_btn
            assert zixun_page.xiangqing_title.text == celllast_title

    def hkus_gonggao_celln_click(self):
        """
        返回公告列表随机一行对象
        :return:资讯列表随机某行
        """
        zixun_page = ZixunPage(self.w)
        public_method = PublicMethod(self.w)

        length = len(self.w.find_elements_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIAWebView[1]"
            "/UIALink[@name]"))

        if length > 50:
            length = 50

        if length > 3:
            num = random.randint(3, length-1)
            print "随机数：{}, 列表长度：{}".format(num, length)

            celln = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/"
                "UIAWebView[1]/UIALink[{}]".format(num))
            celln_title = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIAWebView[1]"
                "/UIALink[{}]/UIAStaticText[1]".format(num)).text
            celln.click()
            sleep(1)
            pic_name = '搜索-分时-公告-资讯详情{}_17'.format(length)
            public_method.public_screenshot_as_file(caseName="test_fenshikxian_yidenglu", picName=pic_name)
            assert zixun_page.shoucang_btn
            assert zixun_page.fenxiang_btn
            assert zixun_page.xiangqing_title.text == celln_title

    def hkus_gonggao_celllast_click(self):
        """
        返回公告列表最后一行对象
        :return:
        """
        zixun_page = ZixunPage(self.w)
        public_method = PublicMethod(self.w)

        lenth = len(self.w.find_elements_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/"
                                                   "UIATableCell[3]/UIAWebView[1]/UIALink[@name]"))
        print "列表长度：{}".format(lenth)

        if lenth > 50:
            lenth = 50

        if 3 < lenth:
            celllast = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/"
                "UIAWebView[1]/UIALink[{}]".format(lenth))

            celln_title = self.w.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIAWebView[1]"
                "/UIALink[{}]/UIAStaticText[1]".format(lenth)).text
            celllast.click()
            sleep(1)
            pic_name = '搜索-分时-公告-资讯详情{}_17'.format(lenth)
            public_method.public_screenshot_as_file(caseName="test_fenshikxian_yidenglu", picName=pic_name)
            assert zixun_page.shoucang_btn
            assert zixun_page.fenxiang_btn
            assert zixun_page.xiangqing_title.text == celln_title

