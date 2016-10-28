#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao@myhexin.com"

from page_object.appium_page_objects import PageObject, page_element

class HangyebankuaiPage(PageObject):
    """
    行情－> 港美股
    港美股页面的相关元素及其操作
    """
    fanhui_btn =  page_element(accessibility_id = '返回')
    gengduoshuju_btn = page_element(accessibility_id = '查看更多数据项')
    lingzhanggu_btn = page_element(accessibility_id = '领涨股')
    lingdiegu_btn = page_element(accessibility_id= '领跌股')

    #港美股板块页面中的切换板块的小三角按钮
    xiayigegupiao_button = page_element(accessibility_id='下一个股票')
    shangyigegupiao_button = page_element(accessibility_id='上一个股票')

    def hybk_up(self):
        """
        板块页面的向上滑动操作
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (200 / 375.0)
        start_y = height * (500 / 667.0)
        end_x = width * (200 / 375.0)
        end_y = height * (200 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hybk_down(self):
        """
        板块页面的向下滑动操作
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (200 / 375.0)
        start_y = height * (200 / 667.0)
        end_x = width * (200 / 375.0)
        end_y = height * (500 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)