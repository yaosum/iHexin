#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "yaosumei@myhexin.com"

from page_object.appium_page_objects import PageObject, page_element

class HushenPage(PageObject):
    """
    行情－> 沪深
    沪深页面的相关元素及擦偶走
    """

    hushen_title = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]")

    # 第一个单元格的标题,与组缩进有关,第一个组缩进后,表示第二个组的第一个单元格
    hs_cell1_title = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[3]')
    # 沪深页面每个列表下的第一行元素
    cell1_btn = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]")
    # 指数
    szzs_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAButton[1]")
    szcz_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAButton[2]")
    cybz_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAButton[3]")

    zhangtinfenxi_btn = page_element(accessibility_id = "涨停分析")

    # 每个分组下的收缩按钮和更多按钮
    zfb_shousuo_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]/UIAButton[@name='涨幅榜']")
    zfb_gengduo_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]/UIAButton[@name='•••']")

    dfb_shousuo_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[@name='跌幅榜']")
    dfb_gengduo_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[@name='•••']")

    kszf_shousuo_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[3]/UIAButton[@name='快速涨幅']")
    kszf_gengduo_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[3]/UIAButton[@name='•••']")

    hslb_shousuo_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[4]/UIAButton[@name='换手率榜']")
    hslb_gengduo_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[4]/UIAButton[@name='•••']")

    lbb_shousuo_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[5]/UIAButton[@name='量比榜']")
    lbb_gengduo_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[5]/UIAButton[@name='•••']")

    cjeb_shousuo_btn = page_element(
        xpath = "//UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[6]/UIAButton[@name='成交额榜']")
    cjeb_gengduo_btn = page_element(
        xpath = "//UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[6]/UIAButton[@name='•••']")

