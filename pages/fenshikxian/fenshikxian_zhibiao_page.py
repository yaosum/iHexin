#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page_object.appium_page_objects import PageObject, page_element

class FenshikxianZhibiaoPage(PageObject):
    """
        分时k线页面---我的指标以及添加指标页面的一些操作及元素查找
    """
    # 我的指标页面
    guanbi_btn = page_element(accessibility_id = '关闭')
    qianfuquan_btn = page_element(accessibility_id = '前复权')
    chuquan_btn = page_element(accessibility_id = '除权')
    kjunxian_shezhi_image = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAImage[1]')
    kjunxian_switch = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIASwitch[1]')
    quekou_xinxi_image = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAImage[2]')
    quekou_switch = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIASwitch[2]')
    chengbenxian_xinxi_image = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAImage[3]')
    tianjiazhibiao_btn = page_element(accessibility_id = '添加指标')

    # 添加指标页面
    fanhui_button = page_element(accessibility_id='返回')
    # 指标信息/设置页面
    title = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]')
    # 删除指标按钮
    shanchu_btn = page_element(accessibility_id = "删除")

    # k线指标信息页(大屏)
    chengjiaoliang_shezhi = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]")
    chengjiaoe_shezhi = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAButton[1]")
    # 第一个指标的删除按钮(小屏)
    cell01_shanchu = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[2]")




