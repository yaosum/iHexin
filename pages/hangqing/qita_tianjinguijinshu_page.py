#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class QitaTianjinguijinshuPage(PageObject):
    """
    行情－> 其他－> 天津贵金属
    天津贵金属页面相关元素及操作
    """
    fanhui_button = page_element(accessibility_id='返回')
    kaihu_btn = page_element(accessibility_id= '开户')
    kehufuwuzhongxin_btn = page_element(xpath= "/UIAButton[@name='客户服务中心']")

    cell01 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableCell[1]/UIAElement[1]')
    cell01_title = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')

    sell_btn = page_element(accessibility_id= '卖价')
    buy_btn = page_element(accessibility_id= '买价')
    zhangfu_btn = page_element(accessibility_id= '涨幅')
    zhangdie_btn = page_element(accessibility_id= '涨跌')
    shijian_btn = page_element(accessibility_id= '时间')
    zuojiesuan_btn = page_element(accessibility_id= '昨结算')

    def tjgjs_clickOperation(self):
        """
        天津贵金属页面的排序操作
        :return:
        """
        listheader = ('zuojiesuan', 'shijian', 'zhangdie', 'zhangfu', 'buy', 'sell', )
        for n in range(3):
            header = random.choice(listheader)
            eval('self.{0}_btn.click()'.format(header))
            eval('self.{0}_btn.click()'.format(header))

    def tjgjs_right(self):
        """
        向右滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (240 / 375.0)
        start_y = height * (350 / 667.0)
        end_x = width * (340 / 375.0)
        end_y = height * (350 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def tjgjs_left(self):
        """
        向左滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (350 / 375.0)
        start_y = height * (350 / 667.0)
        end_x = width * (240 / 375.0)
        end_y = height * (350 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)