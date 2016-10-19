#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element

class QitaXinsanbanPage(PageObject):
    fanhui_btn = page_element(accessibility_id = '返回')
    sanbanzuoshi_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAButton[1]')
    sanbanchengzhi_btn = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAButton[2]')

    chengfengu_btn = page_element(accessibility_id = '成分股')

    chuangxin_btn = page_element(accessibility_id = '创新')
    jichu_btn = page_element(accessibility_id = '基础')
    zuoshi_btn = page_element(accessibility_id = '做市')
    xieyi_btn = page_element(accessibility_id = '协议')
    youxiangu_btn = page_element(accessibility_id = '优先股')

    group1 = page_element(accessibility_id = '涨幅榜')
    group2 = page_element(accessibility_id = '跌幅榜')
    group3 = page_element(accessibility_id = '成交额榜')

    gengduo1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]/UIAButton[2]')
    gengduo2 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[2]')
    gengduo3 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[3]/UIAButton[2]')

    cell1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[2]')
    cell1_title = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[3]')
