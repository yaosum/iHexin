#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element
import types
from time import sleep
from pages.public.public_method import PublicMethod

class FenshiKxianPage(PageObject):
    """
    分时k线页面的相关元素及操作
    """
    fanhui_button = page_element(accessibility_id = '返回')
    xiayigegupiao_button = page_element(accessibility_id = '下一个股票')
    title_staText = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAScrollView[1]/UIAStaticText[1]')
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

    ri_btn = page_element(accessibility_id='日')
    zhou_btn = page_element(accessibility_id='周')
    yue_btn = page_element(accessibility_id='月')

    fenzhong_btn = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[14]')
    oneMinute_btn = page_element(accessibility_id='1分')
    five_btn = page_element(accessibility_id='5分')
    fifteen_btn = page_element(accessibility_id='15分')
    thirty_btn = page_element(accessibility_id='30分')
    sixty_btn = page_element(accessibility_id='60分')

    VR_btn = page_element(accessibility_id='VR')
    shezhi_btn = page_element(accessibility_id='设置')

    # 分时
    wudang_btn = page_element(accessibility_id='五档')
    mingxi_btn = page_element(accessibility_id='明细')
    chengjiao_btn = page_element(accessibility_id='成交')
    #十档按钮
    shidang_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAButton[3]')
    quanjingwubaidang_btn = page_element(accessibility_id = '全景500档')
    #分时切换横屏按钮
    fenshi_qiehengping_btn = page_element(xpath = "//UIAButton[@name='toLandscape']")

    yujing_btn = page_element(accessibility_id='预警')
    xiadan_btn = page_element(accessibility_id='下单')
    lungu_btn = page_element(accessibility_id='论股')

    jiazixuan_staText = page_element(accessibility_id='加自选')

    #闪电下单
    quickbuy_btn = page_element(accessibility_id = 'xiadan QuickBuy')
    quicksell_btn = page_element(accessibility_id = 'xiadan QuickSell')
    chedan_btn = page_element(accessibility_id = 'xiadan CheDanChaXun')
    qujiaoyi_btn = page_element(accessibility_id = '去交易下单')
    quxiaojiaoyi_btn = page_element(accessibility_id = '取 消')

    #行情数据
    hangqingshuju_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAButton[2]')
    guanbi_btn = page_element(accessibility_id = '关闭')

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

    #切换股票,切换分时和k线
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
        if self.zhankai_btn != None:
            self.zhankai_btn.click()
        public_method.public_longPress(self.fangda_btn, 1)
        public_method.public_longPress(self.suoxiao_btn, 1)
        public_method.public_longPress(self.zuoyi_btn, 1)
        public_method.public_longPress(self.youyi_btn, 1)
        self.w.tap([(width * 190 / 375.0, height * 572 / 667.0,)])
