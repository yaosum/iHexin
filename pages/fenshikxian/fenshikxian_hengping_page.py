#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

class FenshikxianHengpingPage(PageObject):
    """
    	分时k线横屏页面的相关元素及操作
    """
    fanhui_button = page_element(accessibility_id='返回')
    x_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAButton[3]')

    wudang_btn = page_element(accessibility_id='五档')
    mingxi_btn = page_element(accessibility_id='明细')
    chengjiao_btn = page_element(accessibility_id='成交')

    #行情数据
    hangqingshuju_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAButton[2]')
    guanbi_btn = page_element(accessibility_id='关闭')

    kLine_scrollview = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]')

    fenshi_btn = page_element(accessibility_id = '分时')
    riK_btn = page_element(accessibility_id = '日K')
    zhouK_btn = page_element(accessibility_id = '周K')
    yueK_btn = page_element(accessibility_id = '月K')
    sixty_btn = page_element(accessibility_id = '60分')
    gengduo_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAButton[10]')

    #下面这几个按钮appium找不到 目前使用坐标点击
    # one_btn = page_element(accessibility_id = '1分钟')
    # five_btn = page_element(accessibility_id = '5分钟')
    # fifteen_btn = page_element(accessibility_id ='15分钟')
    # thirty_btn = page_element(accessibility_id ='30分钟')
    zhibiao_btn = page_element(accessibility_id = '指标')

    zhibiao_cell01 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]')
    #手势
    """
        放大手势
        说明:按照固定的点,多点触摸,滑动手势。其相对坐标以iPhone 6 为基准机型计算
    """
    def kLine_enlarge(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        a1 = TouchAction()
        a1.press(x=width * 400/667.0, y=height * 250/375.0).move_to(x=40, y=0).release()
        a2 = TouchAction()
        a2.press(x=width * 400/667.0, y=height * 250/375.0).move_to(x=-40, y=0).release()
        ma = MultiAction(self.w)
        ma.add(a1, a2)
        ma.perform()

    """
        缩小手势
        说明:按照固定的点,多点触摸,滑动手势。其相对坐标以iPhone 6 为基准机型计算
    """

    def kLine_narrow(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        a1 = TouchAction()
        a1.press(x=width * 300/667.0, y=height * 250/375.0).move_to(x=40, y=0).release()
        a2 = TouchAction()
        a2.press(x=width * 500/667.0, y=height * 250/375.0).move_to(x=-40, y=0).release()
        ma = MultiAction(self.w)
        ma.add(a1, a2)
        ma.perform()

    """
        左移手势
    """
    def left_shift(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (526 / 667.0)
        start_y = height * (184 / 375.0)
        end_x = width * (170 / 667.0)
        end_y = height * (184 / 375.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    """
        右移手势
    """

    def right_shift(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (170 / 667.0)
        start_y = height * (184 / 375.0)
        end_x = width * (526 / 667.0)
        end_y = height * (184 / 375.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    # k线放大 缩小 左移 右移操作
    def kxian_action_operation(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        for n in range(5):
            self.kLine_enlarge()
        for n in range(5):
            self.kLine_narrow()
        for n in range(5):
            self.right_shift()
        for n in range(5):
            self.left_shift()
        self.w.tap([(width * 100 / 667.0, height * 275 / 375.0,)])