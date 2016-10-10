#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class GangmeiguPage(PageObject):
    USA_btn = page_element(accessibility_id = '美股');
    HK_btn = page_element(accessibility_id = '港股')

    #这个属性表示港媒股页面第一个单元格。注意:当组缩紧以后,表示可见组的第一个单元格
    cell1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[2]')

    #美股和港股行业版块以及行业版块上面的三个按钮
    cell1_1 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIAButton[1]')
    cell1_2 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIAButton[2]')
    cell1_3 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIAButton[3]')

    cell2_1 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[1]')
    cell2_2 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[4]')
    cell2_3 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[7]')
    cell2_4 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[10]')
    cell2_5 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[13]')
    cell2_6 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[16]')

    #美股
    #组标题按钮
    #group_usa1 = page_element(accessibility_id = '行业板块')
    group_usa1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[1]/UIAButton[1]')
    group_usa2 = page_element(accessibility_id='热点中概股')
    group_usa3 = page_element(accessibility_id='热点美股')
    group_usa4 = page_element(accessibility_id='热点ETF')
    group_usa5 = page_element(accessibility_id='中概股涨幅榜')
    group_usa6 = page_element(accessibility_id='中概股跌幅榜')
    #组更多
    gengduo_usa1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[1]/UIAButton[2]')
    gengduo_usa2 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[2]/UIAButton[2]')
    gengduo_usa3 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[3]/UIAButton[2]')
    gengduo_usa4 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[4]/UIAButton[2]')
    gengduo_usa5 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[5]/UIAButton[2]')
    gengduo_usa6 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[6]/UIAButton[2]')


    #港股
    #组标题按钮
    group_hk1 = page_element(accessibility_id= '行业板块')
    group_hk2 = page_element(accessibility_id='港股主板')
    group_hk3 = page_element(accessibility_id='港股创业板')
    #组更多
    gengduo_hk1 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]/UIAButton[2]')
    gengduo_hk2 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[2]')
    gengduo_hk3 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[3]/UIAButton[2]')




