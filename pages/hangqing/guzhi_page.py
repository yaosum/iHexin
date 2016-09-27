#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage

class GuzhiPage(PageObject):
    kanzijin_btn = page_element(accessibility_id = '看资金')
    guzhi_btn = page_element(accessibility_id = '股指')
    guoneiZhishu_btn = page_element(accessibility_id = '国内指数')
    qihuo_btn =  page_element(accessibility_id = '股指期货')
    fushiA50Qihuo_btn = page_element(accessibility_id = '富时A50指数期货')
    qita_btn = page_element(accessibility_id = '其他指数')

    guoneiZhishu_gengduo_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]/UIAButton[2]')
    qihuo_gengduo_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[2]')
    qita_gengduo_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[4]/UIAButton[2]')

    #国内指数宫格按钮
    gn_cell1_btn1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]')
    gn_cell1_btn2 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAButton[2]')
    gn_cell1_btn3 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAButton[3]')
    gn_cell2_btn1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAButton[1]')
    gn_cell2_btn2 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAButton[2]')
    gn_cell2_btn3 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAButton[3]')

    #股指期货
    qh_cell1_btn1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIAButton[1]')
    qh_cell1_btn2 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIAButton[2]')
    qh_cell1_btn3 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIAButton[3]')
    qh_cell2_btn1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[4]/UIAButton[1]')
    qh_cell2_btn2 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[4]/UIAButton[2]')
    qh_cell2_btn3 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[4]/UIAButton[3]')
    qh_cell3_btn1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[5]/UIAButton[1]')
    qh_cell3_btn2 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[5]/UIAButton[2]')
    qh_cell3_btn3 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[5]/UIAButton[3]')

    #富时A50指数期货
    fs_cell1_btn1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[6]/UIAButton[1]')
    fs_cell1_btn2 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[6]/UIAButton[2]')
    fs_cell1_btn3 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[6]/UIAButton[3]')
    fs_cell2_btn1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[7]/UIAButton[1]')
    fs_cell2_btn2 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[7]/UIAButton[2]')
    fs_cell2_btn3 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[7]/UIAButton[3]')

    #其他指数
    qt_cell1_btn1 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[8]/UIAButton[1]')
    qt_cell1_btn2 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[8]/UIAButton[2]')
    qt_cell1_btn3 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[8]/UIAButton[3]')
    qt_cell2_btn1 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[9]/UIAButton[1]')
    qt_cell2_btn2 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[9]/UIAButton[2]')
    qt_cell2_btn3 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[9]/UIAButton[3]')
    qt_cell3_btn1 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[10]/UIAButton[1]')
    qt_cell3_btn2 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[10]/UIAButton[2]')
    qt_cell3_btn3 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[10]/UIAButton[3]')

    def gn_operation(self):
        fenshikxian_page = FenshiKxianPage(self)
        self.gn_cell1_btn1.click()
        fenshikxian_page.fanhui_button.click()
        self.gn_cell1_btn2.click()
        fenshikxian_page.fanhui_button.click()
        self.gn_cell1_btn3.click()
        fenshikxian_page.fanhui_button.click()
        self.gn_cell2_btn1.click()
        fenshikxian_page.fanhui_button.click()
        self.gn_cell2_btn2.click()
        fenshikxian_page.fanhui_button.click()
        self.gn_cell2_btn3.click()
        fenshikxian_page.change_gupiao(6)

    def qh_operation(self):
        fenshikxian_page = FenshiKxianPage(self)
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
        self.gn_cell3_btn3.click()

    def fs_operation(self):
        fenshikxian_page = FenshiKxianPage(self)
        self.fs_cell1_btn1.click()
        fenshikxian_page.fanhui_button.click()
        self.fs_cell1_btn2.click()
        fenshikxian_page.fanhui_button.click()
        self.fs_cell1_btn3.click()
        fenshikxian_page.fanhui_button.click()
        self.fs_cell2_btn1.click()
        fenshikxian_page.fanhui_button.click()
        self.fs_cell2_btn2.click()
        fenshikxian_page.fanhui_button.click()
        self.gn_cell2_btn3.click()

    def qt_operation(self):
        fenshikxian_page = FenshiKxianPage(self)
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
        self.gt_cell3_btn3.click()