#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from time import sleep
import random

class KanZhulizijinPage(PageObject):
    """
    首页－> 自选－> 资金
    首页－> 行情－> 资金
    看主力资金页面的相关元素及操作
    """
    fanhui_btn = page_element(xpath= '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]')
    cell001 = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]")
    cell002 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]')
    cell002_title = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[1]')
    cell001_title = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')
    kanzhulizijin_staticText = page_element(xpath= "//UIAStaticText[@name= '看主力资金']")
    gengduo_button = page_element(accessibility_id= '更多')
    #closeTip_button = page_element()

    denglu_btn = page_element(accessibility_id='登录')

    zixuan_btn = page_element(xpath= "//UIAWindow[1]/UIAButton[@name='自选']")
    hushen_btn = page_element(accessibility_id='沪深')
    hangye_btn = page_element(accessibility_id='行业')
    gainian_btn = page_element(accessibility_id='概念')

    zixuangushunxu_btn = page_element(accessibility_id='自选股顺序')
    zuixin_staText = page_element(accessibility_id='最新')
    dadanjingliang_staText = page_element(accessibility_id='大单净量')
    zhangfu_staText = page_element(accessibility_id='涨幅')
    zhuliliuru_staText = page_element(accessibility_id='主力流入')
    zhuliliuchu_staText = page_element(accessibility_id='主力流出')
    zhulijingliuru_staText = page_element(accessibility_id='主力净流入')
    jingliuru_staText = page_element(accessibility_id='净流入')
    zhulijingezhanbi_staText = page_element(accessibility_id='主力净额占比')
    rijingliang5_staText = page_element(accessibility_id='5日净量')
    rijingliang10_staText = page_element(accessibility_id='10日净量')
    rizhangfu5_staText = page_element(accessibility_id='5日涨幅')
    rizhangfu10_staText = page_element(accessibility_id='10日涨幅')
    liangbi_staText = page_element(accessibility_id='量比')
    huanshou_staText = page_element(accessibility_id='换手')
    shiyingdong_staText = page_element(accessibility_id='市盈(动)')
    shijinglv_staText = page_element(accessibility_id='市净率')
    liutongshizhi_staText = page_element(accessibility_id='流通市值')
    zongshizhi_staText = page_element(accessibility_id='总市值')

    rizhangfu20_staText = page_element(accessibility_id='20日涨幅')
    zongshou_staText = page_element(accessibility_id='总手')
    jine_staText = page_element(accessibility_id='金额')

    desc_img = page_element(accessibility_id='DescImg')
    asc_img = page_element(accessibility_id='AscImg')

    def hx_ergodic_hushen_zhibiao(self):
        """
        看主力资金－> 自选/沪深下的排序操作
        :return:
        """
        listheader = ('zuixin', 'dadanjingliang', 'zhangfu', 'zhuliliuru', 'zhuliliuchu', 'jingliuru',
                      'zhulijingezhanbi', 'rijingliang5', 'rijingliang10', 'rizhangfu5', 'rizhangfu10', 'liangbi',
                      'huanshou', 'shiyingdong', 'shijinglv', 'liutongshizhi', 'zongshizhi')
        length = int(len(listheader))
        for n in range(3):
            num = random.randint(0, length - 1)
            eval('self.{0}_staText.click()'.format(listheader[num]))
            eval('self.{0}_staText.click()'.format(listheader[num]))

    def hx_ergodic_zhibiao(self):
        """
        看主力资金－> 概念／行业下的排序操作
        :return:
        """
        listheader = ('dadanjingliang', 'zhangfu', 'huanshou', 'rizhangfu5', 'rizhangfu10', 'rizhangfu20', 'zongshou',
                      'jine')
        length = int(len(listheader))
        for n in range(3):
            num = random.randint(0, length - 1)
            eval('self.{0}_staText.click()'.format(listheader[num]))
            eval('self.{0}_staText.click()'.format(listheader[num]))

    def hx_upglide(self):
        """
        向上滑动
        :return:
        """
        # 基于iPhone6 375/667
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (304 / 375.0)
        start_y = height * (598 / 667.0)
        end_x = width * (304 / 375.0)
        end_y = height * (260 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hx_glide(self):
        """
        向下滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (304 / 375.0)
        start_y = height * (260 / 667.0)
        end_x = width * (304 / 375.0)
        end_y = height * (598/667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hx_left(self):
        """
        向左滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (359 / 375.0)
        start_y = height * (466 / 667.0)
        end_x = width * (142 / 375.0)
        end_y = height * (466 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hx_right(self):
        """
        向右滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (142 / 375.0)
        start_y = height * (466 / 667.0)
        end_x = width * (359 / 375.0)
        end_y = height * (466 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def pageGotoFenshikxian(self):
        """
        从第一行及第二行元素进入分时k线页面，并进行股票切换
        :return:
        """
        fenshikxian_page = FenshiKxianPage(self.w)
        self.hx_glide()
        sleep(1)
        title1 = self.cell001_title.text
        length = int(len(self.w.find_elements_by_xpath("//UIATableView[1]/UIATableCell[@name]")))
        if length > 10:
            length = 5
        self.cell001.click()
        assert fenshikxian_page.title_staText.text == title1
        # step73-76
        fenshikxian_page.change_gupiao(length)
        # step 77
        fenshikxian_page.fanhui_button.click()
        sleep(1)
        self.hx_glide()
        if length >= 2:
            sleep(1)
            title2 = self.cell002_title.text
            self.cell002.click()
            assert fenshikxian_page.title_staText.text == title2
            fenshikxian_page.change_gupiao(length)
            fenshikxian_page.fanhui_button.click()