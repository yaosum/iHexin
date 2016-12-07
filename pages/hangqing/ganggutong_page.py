#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "yaosumei@myhexin.com"

from page_object.appium_page_objects import PageObject, page_element

class GanggutongPage(PageObject):
    """
    行情－ 港美股－ 港股－ 沪深港通
    港股通页面内相关元素及其操作
    """
    hushenangtong_title = page_element(accessibility_id = "沪、深港通")
    fanhui_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]")
    shuaxin_btn = page_element(accessibility_id = "刷新")
    sousuo_btn = page_element(accessibility_id = "search home")
    ganggutong_tab = page_element(accessibility_id = "港股通")
    hugutong_tab = page_element(accessibility_id="沪股通")
    shengutong_tab = page_element(accessibility_id="深股通")

    zuixin2_btn = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableCell[1]"
              "/UIAStaticText[1]")
    zuixin_btn = page_element(accessibility_id = "最新")
    zhangfu_btn = page_element(accessibility_id="涨幅")
    zhangdie_btn = page_element(accessibility_id="涨跌")

    # 港股通
    ruhecanyu_btn = page_element(accessibility_id="如何参与?")
    hushi_gengduo_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableView[1]/UIATableCell[1]")
    shenshi_gengduo_btn = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableView[2]/UIATableCell[1]")
    # 沪股通/深股通
    zijinliuru_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIACollectionView[1]/UIACollectionCell[1]"
                "/UIAStaticText[1]")
    shengyuedu_btn = page_element(
        xpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIACollectionView[1]/UIACollectionCell[2]"
                "/UIAStaticText[1]")
    zongedu_btn = page_element(
        xpath="//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIACollectionView[1]/UIACollectionCell[3]"
              "/UIAStaticText[1]")

    def ganggutong_cell01_click(self):
        """
        点击港股通列表第一行元素
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (50 / 375.0)
        tap_y = height * (327 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})

    def hushengutong_cell01_click(self):
        """
        点击沪深股通列表第一行元素
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (52 / 375.0)
        tap_y = height * (238 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})

    def ganggutong_operation_click(self):
        self.zuixin_btn.click()
        self.zuixin_btn.click()
        self.zhangfu_btn.click()
        self.zhangfu_btn.click()
        self.zhangdie_btn.click()
        self.zhangdie_btn.click()

    def hushengutong_operation_click(self):
        self.zuixin2_btn.click()
        self.zuixin2_btn.click()
        self.zhangfu_btn.click()
        self.zhangfu_btn.click()
        self.zhangdie_btn.click()
        self.zhangdie_btn.click()

    def up_glide(self):
        """
            从下向上滑动
            :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (200 / 375.0)
        start_y = height * (579 / 667.0)
        end_x = width * (200 / 375.0)
        end_y = height * (247 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def down_glide(self):
        """
            从上向下滑动
            :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (200 / 375.0)
        start_y = height * (247 / 667.0)
        end_x = width * (200 / 375.0)
        end_y = height * (579 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hushi_gengduo_click(self):
        """
            点击港股通（沪市）-更多
            :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (97 / 375.0)
        tap_y = height * (214 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})

    def shenshi_gengduo_click(self):
        """
            点击港股通（深市）-更多
            :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (263 / 375.0)
        tap_y = height * (214 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})
