#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class GangmeiguPage(PageObject):
    us_btn = page_element(accessibility_id = '美股');
    hk_btn = page_element(accessibility_id = '港股')

    #这个属性表示港媒股页面第一个单元格。注意:当组缩紧以后,表示可见组的第一个单元格
    us_cell1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[2]')
    hk_cell1 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[2]')

    #美股和港股行业版块以及行业版块上面的三个按钮
    us_cell1_1 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIAButton[1]')
    us_cell1_2 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIAButton[2]')
    us_cell1_3 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIAButton[3]')

    hk_cell1_1 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAButton[1]')
    hk_cell1_2 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAButton[2]')
    hk_cell1_3 = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAButton[3]')

    us_cell2_1 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[1]')
    us_cell2_2 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[4]')
    us_cell2_3 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[7]')
    us_cell2_4 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[10]')
    us_cell2_5 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[13]')
    us_cell2_6 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[16]')

    hk_cell2_1 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')
    hk_cell2_2 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[4]')
    hk_cell2_3 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[7]')
    hk_cell2_4 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[10]')
    hk_cell2_5 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[13]')
    hk_cell2_6 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[16]')

    #美股
    #组标题按钮
    us_group_1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[1]/UIAButton[1]')
    us_group_2 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[2]/UIAButton[1]')
    us_group_3 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[3]/UIAButton[1]')
    us_group_4 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[4]/UIAButton[1]')
    us_group_5 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[5]/UIAButton[1]')
    us_group_6 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[6]/UIAButton[1]')
    #组更多
    us_gengduo_1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[1]/UIAButton[2]')
    us_gengduo_2 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[2]/UIAButton[2]')
    us_gengduo_3 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[3]/UIAButton[2]')
    us_gengduo_4 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[4]/UIAButton[2]')
    us_gengduo_5 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[5]/UIAButton[2]')
    us_gengduo_6 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableGroup[6]/UIAButton[2]')


    #港股
    #组标题按钮
    hk_group_1 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]/UIAButton[1]')
    hk_group_2 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[1]')
    hk_group_3 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[3]/UIAButton[1]')
    #组更多
    hk_gengduo_1 = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[1]/UIAButton[2]')
    hk_gengduo_2 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[2]')
    hk_gengduo_3 = page_element(
        xpath='//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableGroup[3]/UIAButton[2]')

    def glide_up(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (200 / 375.0)
        start_y = height * (500 / 667.0)
        end_x = width * (200 / 375.0)
        end_y = height * (200 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def glide_down(self):
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (200 / 375.0)
        start_y = height * (200 / 667.0)
        end_x = width * (200 / 375.0)
        end_y = height * (500 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)



