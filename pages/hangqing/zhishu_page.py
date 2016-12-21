#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pages.public.public_method import PublicMethod
from time import sleep

__author__ = "tianmaotao@myhexin.com"

from page_object.appium_page_objects import PageObject, page_element
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage

class ZhishuPage(PageObject):
    """
    行情－> 股指
    股指页面的相关元素与操作
    """
    kanzijin_btn = page_element(accessibility_id = '看资金')
    zhishu_btn = page_element(accessibility_id = '指数')
    guoneiZhishu_btn = page_element(accessibility_id = '国内指数')
    qihuo_btn =  page_element(accessibility_id = '股指期货')
    fushiA50Qihuo_btn = page_element(accessibility_id = '富时A50指数期货')
    qita_btn = page_element(accessibility_id = '其他指数')

    guoneiZhishu_gengduo_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]/UIAButton[2]')
    qihuo_gengduo_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[2]')
    qita_gengduo_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[4]/UIAButton[2]')

    #国内指数宫格按钮
    gn_cell1_btn1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]')
    gn_cell1_btn2 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAButton[2]')
    gn_cell1_btn3 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAButton[3]')
    gn_cell2_btn1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAButton[1]')
    gn_cell2_btn2 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAButton[2]')
    gn_cell2_btn3 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAButton[3]')

    #股指期货
    qh_cell1_btn1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIAButton[1]')
    qh_cell1_btn2 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIAButton[2]')
    qh_cell1_btn3 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIAButton[3]')
    qh_cell2_btn1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[4]/UIAButton[1]')
    qh_cell2_btn2 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[4]/UIAButton[2]')
    qh_cell2_btn3 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[4]/UIAButton[3]')
    qh_cell3_btn1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[5]/UIAButton[1]')
    qh_cell3_btn2 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[5]/UIAButton[2]')
    qh_cell3_btn3 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[5]/UIAButton[3]')

    #富时A50指数期货
    fs_cell1_btn1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[6]/UIAButton[1]')
    fs_cell1_btn2 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[6]/UIAButton[2]')
    fs_cell1_btn3 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[6]/UIAButton[3]')

    #其他指数
    qt_cell1_btn1 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[7]/UIAButton[1]')
    qt_cell1_btn2 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[7]/UIAButton[2]')
    qt_cell1_btn3 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[7]/UIAButton[3]')
    qt_cell2_btn1 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[8]/UIAButton[1]')
    qt_cell2_btn2 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[8]/UIAButton[2]')
    qt_cell2_btn3 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[8]/UIAButton[3]')
    qt_cell3_btn1 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[9]/UIAButton[1]')
    qt_cell3_btn2 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[9]/UIAButton[2]')
    qt_cell3_btn3 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[9]/UIAButton[3]')



    def gn_operation(self):
        """
        国内指数进入每个单元格的操作
        :return:
        """
        fenshikxian_page = FenshiKxianPage(self.w)
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (60 / 375.0)
        tap_y = height * (161 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
        fenshikxian_page.fanhui_button.click()
        tap_x = width * (189 / 375.0)
        tap_y = height * (161 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
        fenshikxian_page.fanhui_button.click()
        tap_x = width * (310 / 375.0)
        tap_y = height * (161 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
        fenshikxian_page.fanhui_button.click()
        tap_x = width * (60 / 375.0)
        tap_y = height * (237 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
        fenshikxian_page.fanhui_button.click()
        tap_x = width * (189 / 375.0)
        tap_y = height * (237 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
        fenshikxian_page.fanhui_button.click()
        tap_x = width * (310 / 375.0)
        tap_y = height * (237 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
        fenshikxian_page.change_gupiao(6)
        fenshikxian_page.fanhui_button.click()

    def qh_operation(self):
        """
        股指期货进入每个单元格的操作
        :return:
        """
        fenshikxian_page = FenshiKxianPage(self.w)
        self.qh_cell1_btn1.click()
        fenshikxian_page.fanhui_button.click()
        self.qh_cell1_btn2.click()
        fenshikxian_page.fanhui_button.click()
        self.qh_cell1_btn3.click()
        fenshikxian_page.fanhui_button.click()
        self.qh_cell2_btn1.click()
        fenshikxian_page.fanhui_button.click()
        self.qh_cell2_btn2.click()
        fenshikxian_page.fanhui_button.click()
        self.qh_cell2_btn3.click()
        fenshikxian_page.fanhui_button.click()
        self.qh_cell3_btn1.click()
        fenshikxian_page.fanhui_button.click()
        self.qh_cell3_btn2.click()
        fenshikxian_page.fanhui_button.click()
        self.qh_cell3_btn3.click()
        fenshikxian_page.change_gupiao(9)
        fenshikxian_page.fanhui_button.click()

    def fs_operation(self):
        """
        富时A50指数进入每个单元格的操作
        :return:
        """
        fenshikxian_page = FenshiKxianPage(self.w)
        self.fs_cell1_btn1.click()
        fenshikxian_page.fanhui_button.click()
        self.fs_cell1_btn2.click()
        fenshikxian_page.fanhui_button.click()
        self.fs_cell1_btn3.click()
        sleep(1)
        fenshikxian_page.change_gupiao(3)
        fenshikxian_page.fanhui_button.click()

    def qt_operation(self):
        """
        其他指数，进入每个单元格的操作
        :return:
        """
        fenshikxian_page = FenshiKxianPage(self.w)
        self.qt_cell1_btn1.click()
        fenshikxian_page.fanhui_button.click()
        self.qt_cell1_btn2.click()
        fenshikxian_page.fanhui_button.click()
        self.qt_cell1_btn3.click()
        fenshikxian_page.fanhui_button.click()
        self.qt_cell2_btn1.click()
        fenshikxian_page.fanhui_button.click()
        self.qt_cell2_btn2.click()
        fenshikxian_page.fanhui_button.click()
        self.qt_cell2_btn3.click()
        fenshikxian_page.fanhui_button.click()
        self.qt_cell3_btn1.click()
        fenshikxian_page.fanhui_button.click()
        self.qt_cell3_btn2.click()
        fenshikxian_page.fanhui_button.click()
        self.qt_cell3_btn3.click()
        sleep(1)
        fenshikxian_page.change_gupiao(9)
        fenshikxian_page.fanhui_button.click()

    def up_glide(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (344 / 375.0)
        start_y = height * (500 / 667.0)
        end_x = width * (344 / 375.0)
        end_y = height * (10 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def down_glide(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (344 / 375.0)
        start_y = height * (10 / 667.0)
        end_x = width * (344 / 375.0)
        end_y = height * (500 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)
