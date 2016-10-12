#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "yaosumei@myhexin.com"

from page_object.appium_page_objects import PageObject, page_element

class HushenPage(PageObject):
    hushen_title = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]")

    szzs_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAButton[1]")
    szcz_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAButton[2]")
    ahbijia_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAButton[3]")

    zhangtinfenxi_btn = page_element(accessibility_id = "涨停分析")


    zfb_shousuo_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]"
                                           "/UIAButton[1]")
    zfb_cell1_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]")
    zfb_gengduo_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]"
                                           "/UIAButton[3]")

    dfb_shousuo_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]"
                                           "/UIAButton[1]")
    dfb_cell1_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]")
    dfb_gengduo_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]"
                                           "/UIAButton[2]")

    kszf_shousuo_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[3]"
                                            "/UIAButton[1]")
    kszf_cell1_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]")
    kszf_gengduo_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[3]"
                                            "/UIAButton[2]")

    hslb_shousuo_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[4]"
                                            "/UIAButton[1]")
    hslb_cell1_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]")
    hslb_gengduo_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[4]"
                                            "/UIAButton[2]")

    lbb_shousuo_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[5]"
                                           "/UIAButton[1]")
    lbb_cell1_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]")
    lbb_gengduo_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[5]"
                                           "/UIAButton[2]")

    cjeb_shousuo_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[6]"
                                            "/UIAButton[1]")
    cjeb_cell1_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]")
    cjeb_gengduo_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[6]"
                                             "/UIAButton[2]")

