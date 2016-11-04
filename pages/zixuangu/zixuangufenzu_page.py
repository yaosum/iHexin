#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page_object.appium_page_objects import PageObject, page_element
class ZixuangufenzuPage(PageObject):
    """
    自选股分组相关元素及操作
    """
    xinjianfenzu_btn = page_element(accessibility_id = "新建分组")
    guanlifenzu_btn = page_element(accessibility_id = "管理分组")
    zixuangu_btn = page_element(accessibility_id="自选股")
    bankuai1_btn = page_element(accessibility_id="板块1")
    bankuai2_btn = page_element(accessibility_id="板块2")
    bankuai3_btn = page_element(accessibility_id="板块3")
    bankuai4_btn = page_element(accessibility_id="板块4")
    bankuai5_btn = page_element(accessibility_id="板块5")
    bankuai6_btn = page_element(accessibility_id="板块6")
    bankuai7_btn = page_element(accessibility_id="板块7")
    bankuai8_btn = page_element(accessibility_id="板块8")

    chakanxiangqing_btn = page_element(accessibility_id = "查看详情")
    guanbi_btn = page_element(accessibility_id = "关闭")

    cell01_title = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')

    def hx_tapblank(self):
        """
        点击自选股分组页面外的空白处，即自选股分组页面右侧
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (365 / 375.0)
        tap_y = height * (100 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
