#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class Qita50ETFPage(PageObject):
    fanhui_button = page_element(accessibility_id='返回')
    cell_etf_btn = page_element(accessibility_id = 'JianBaoJiaBg')
    group1 = page_element(xpath = ' //UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[1]/UIAButton[1]')
    group2 = page_element(xpath = ' //UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[1]')
    group3 = page_element(xpath=' //UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[3]/UIAButton[1]')
    group4 = page_element(xpath=' //UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[4]/UIAButton[1]')


    def qtgpqq_R_right(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (270 / 375.0)
        start_y = height * (350 / 667.0)
        end_x = width * (350 / 375.0)
        end_y = height * (350 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def qtgpqq_R_left(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (350 / 375.0)
        start_y = height * (350 / 667.0)
        end_x = width * (270 / 375.0)
        end_y = height * (350 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)


    def qtgpqq_L_right(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (30 / 375.0)
        start_y = height * (350 / 667.0)
        end_x = width * (120 / 375.0)
        end_y = height * (350 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def qtgpqq_L_left(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (120 / 375.0)
        start_y = height * (350 / 667.0)
        end_x = width * (30 / 375.0)
        end_y = height * (350 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def qtgpqq_up(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (200 / 375.0)
        start_y = height * (500 / 667.0)
        end_x = width * (200 / 375.0)
        end_y = height * (350 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def qtgpqq_down(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (200 / 375.0)
        start_y = height * (350 / 667.0)
        end_x = width * (200 / 375.0)
        end_y = height * (500 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)