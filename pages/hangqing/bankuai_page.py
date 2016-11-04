#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao@myhexin.com"

from page_object.appium_page_objects import PageObject, page_element

class BankuaiPage(PageObject):
    """
    首页－> 行情－> 板块
    板块页面内相关元素与操作
    """
    #柱状图名称
    hy_histogram_title = page_element(accessibility_id = '行业主力净流入(亿)')
    gn_histogram_title = page_element(accessibility_id = '概念主力净流入(亿)')
    # 柱状图更多按钮
    hy_histogram_gengduo = page_element(accessibility_id = 'bk roll more')
    gn_histogram_gengduo = page_element(accessibility_id = 'bk roll more')
    # 柱状图板块个股按钮
    histogram_btn1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAScrollView[1]/UIAButton[2]')
    histogram_btn2 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAScrollView[1]/UIAButton[3]')
    histogram_btn3 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAScrollView[1]/UIAButton[4]')
    histogram_btn4 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAScrollView[1]/UIAButton[5]')
    histogram_btn5 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAScrollView[1]/UIAButton[6]')
    histogram_btn6 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAScrollView[1]/UIAButton[7]')

    #各类板块名称
    hy_group_title = page_element(accessibility_id = '行业板块')
    gn_group_title = page_element(accessibility_id = '概念板块')
    zs_group_title = page_element(accessibility_id = '快速涨幅')

    #板块更多按钮
    hy_gengduo_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]/UIAButton[2]')
    gn_gengduo_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[2]')
    zs_gengduo_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[3]/UIAButton[2]')

    #每个板块下的宫格路径
    hy_btn1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]')
    hy_btn2 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAButton[2]')
    hy_btn3 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAButton[3]')
    hy_btn4 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAButton[1]')
    hy_btn5 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAButton[2]')
    hy_btn6 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIAButton[3]')

    gn_btn1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIAButton[1]')
    gn_btn2 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIAButton[2]')
    gn_btn3 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIAButton[3]')
    gn_btn4 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[4]/UIAButton[1]')
    gn_btn5 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[4]/UIAButton[2]')
    gn_btn6 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[4]/UIAButton[3]')

    zs_btn1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[5]/UIAButton[1]')
    zs_btn2 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[5]/UIAButton[2]')
    zs_btn3 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[5]/UIAButton[3]')
    zs_btn4 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[6]/UIAButton[1]')
    zs_btn5 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[6]/UIAButton[2]')
    zs_btn6 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[6]/UIAButton[3]')

    #板块更多页面的第一行元素
    cell01_btn = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]')
    cell01_title = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')


    def glide_left(self):
        """
        柱状图向左滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (372 / 414.0)
        start_y = height * (180 / 736.0)
        end_x = width * (33 / 414.0)
        end_y = height * (180 / 736.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def glide_right(self):
        """
        柱状图向右滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (33 / 414.0)
        start_y = height * (180 / 736.0)
        end_x = width * (372 / 414.0)
        end_y = height * (180 / 736.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)