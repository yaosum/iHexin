#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element
import random

class HangqingGengduoPage(PageObject):
    """
    首页－> 行情
    行情,所有进入更多页面,需要查找的元素和操作放在此类(除了一些特殊，特殊的放在自己本身所属的page中)。
    """
    fanhui_btn = page_element(accessibility_id = '返回')
    zuixin_btn = page_element(accessibility_id = '最新')
    zhangfu_btn = page_element(accessibility_id = '涨幅')
    zhangdie_btn = page_element(accessibility_id = '涨跌')
    xingji_btn = page_element(accessibility_id = '星级')
    zhangfu5_btn = page_element(accessibility_id = '5日涨幅')
    huanshou_btn = page_element(accessibility_id = '换手')
    liangbi_btn = page_element(accessibility_id = '量比')
    zhenfu_btn = page_element(accessibility_id = '振幅')
    zhangsu_btn = page_element(accessibility_id = '涨速')
    shiying_btn = page_element(accessibility_id = '市盈(动)')
    shijinglv_btn = page_element(accessibility_id = '市净率')
    liutong_btn = page_element(accessibility_id = '流通市值')
    jine_btn = page_element(accessibility_id = '金额')
    zongshizhi_btn = page_element(accessibility_id = '总市值')
    zongshou_btn = page_element(accessibility_id = '总手')
    xianshou_btn = page_element(accessibility_id = '现手')

    chengjiaoliang_btn = page_element(accessibility_id = '成交量')
    chengjiaoe_btn = page_element(accessibility_id = '成交额')
    #排序的升序图标和降序图标
    desc_img = page_element(accessibility_id='DescImg')
    asc_img = page_element(accessibility_id='AscImg')

    qita_50ETF_btn = page_element(accessibility_id= '50ETF')
    kaipan_btn = page_element(accessibility_id= '开盘')
    zuoshou_btn = page_element(accessibility_id= '昨收')
    zuigao_btn = page_element(accessibility_id= '最高')
    zuidi_btn = page_element(accessibility_id= '最低')
    weibi_btn = page_element(accessibility_id= '委比')
    zuojiesuan_btn = page_element(accessibility_id= '昨结算')
    chicangliang_btn = page_element(accessibility_id= '持仓量')

    #板块更多新增排序
    zhangfu20_btn = page_element(accessibility_id = '20日涨幅')
    zhangfu10_btn = page_element(accessibility_id = '10日涨幅')
    diejiashu_btn = page_element(accessibility_id = '跌家数')
    zhangjiashu_btn = page_element(accessibility_id = '涨家数')


    #更多列表中的第一行元素
    cell01 = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]')
    #更多列表中的第一行元素的股票名称
    cell01_title = page_element(
        xpath = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')

    #行情里边每个分组进入页面后的操作不一样，当图标不在页面上，进行assert判断会报错
    def bk_clickOperation(self):
        """
        板块更多排序
        :return:
        """
        listheader = ('zongshou', 'jine', 'zuixin', 'huanshou', 'zhangfu5', 'zhangfu')
        length = int(len(listheader))
        for n in range(3):
            num = random.randint(0, length - 1)
            eval('self.{0}_btn.click()'.format(listheader[num]))
            eval('self.{0}_btn.click()'.format(listheader[num]))


    def hybk_clickOperation(self):
        """
        港美股－> 行业板块点击单元格-> 点击查看更多数据页面操作
        :return:
        """
        self.hq_left()
        listheader = ('chengjiaoe', 'chengjiaoliang', 'zhangdie', 'zhangfu', 'zuixin', 'zhangfu')
        length = int(len(listheader))
        for n in range(3):
            num = random.randint(0, length - 1)
            eval('self.{0}_btn.click()'.format(listheader[num]))
            eval('self.{0}_btn.click()'.format(listheader[num]))
        self.hq_up()
        self.hq_down()

    def qita_gpqq_clickOperation(self):
        """
        行情-> 其他-> 股票期权排序
        :return:
        """
        listheader = ('zhenfu', 'weibi', 'zuidi', 'zuigao', 'zuoshou', 'xianshou', 'shijinglv', 'shiying', 'liangbi',
                      'huanshou', 'zongshou', 'zhangsu', 'zhangdie', 'zhangfu', 'zuixin')
        length = int(len(listheader))
        for n in range(3):
            num = random.randint(0, length - 1)
            eval('self.{0}_btn.click()'.format(listheader[num]))
            eval('self.{0}_btn.click()'.format(listheader[num]))

    def shhj_clickOperation(self):
        """
        上海黄金列表排序
        :return:
        """
        listheader = ('zuojiesuan', 'chicangliang', 'zongshou', 'zhangdie', 'zhangfu', 'zuixin')
        length = int(len(listheader))
        for n in range(3):
            num = random.randint(0, length - 1)
            eval('self.{0}_btn.click()'.format(listheader[num]))
            eval('self.{0}_btn.click()'.format(listheader[num]))

    def jijin_clickOperation(self):
        """
        基金(包括沪深封闭基金),以及个股里的除了新三板的其它股，排序操作
        :return:
        """
        listheader = ('xianshou', 'zongshou', 'jine', 'zongshizhi', 'liutong', 'shijinglv', 'shiying', 'zhangsu',
                      'zhenfu', 'liangbi', 'huanshou', 'xingji', 'zhangdie', 'zhangfu', 'zuixin')
        length = int(len(listheader))
        for n in range(3):
            num = random.randint(0, length - 1)
            eval('self.{0}_btn.click()'.format(listheader[num]))
            eval('self.{0}_btn.click()'.format(listheader[num]))

    def hs_clickOperation(self):
        """
        沪深排序操作
        :return:
        """
        listheader = ('xianshou', 'zongshou', 'zongshizhi', 'liutong', 'shijinglv', 'shiying', 'zhangsu', 'zhangfu', 'liangbi',
                      'huanshou', 'xingji', 'zhangdie', 'zhangfu', 'zuixin')
        length = int(len(listheader))
        for n in range(3):
            num = random.randint(0, length - 1)
            eval('self.{0}_btn.click()'.format(listheader[num]))
            eval('self.{0}_btn.click()'.format(listheader[num]))

    def bankuai_clickOperation(self):
        """
            板块排序操作
            :return:
        """

        listheader = ('zongshou', 'jine', 'huanshou', 'zuixin', 'zhangfu20', 'zhangfu10', 'diejiashu', 'zhangjiashu',
                      'zhangsu', 'zhangfu')
        length = int(len(listheader))
        for n in range(3):
            num = random.randint(0, length - 1)
            eval('self.{0}_btn.click()'.format(listheader[num]))
            eval('self.{0}_btn.click()'.format(listheader[num]))

    def ganggutong_clickOperation(self):
        """
        港股通排序操作
        :return:
        """
        listheader = ('zuixin', 'zhangfu', 'zhangdie')
        length = int(len(listheader))
        for n in range(3):
            num = random.randint(0, length - 1)
            eval('self.{0}_btn.click()'.format(listheader[num]))
            eval('self.{0}_btn.click()'.format(listheader[num]))

    def hq_right(self):
        """
        从左向右滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (240 / 375.0)
        start_y = height * (350 / 667.0)
        end_x = width * (340 / 375.0)
        end_y = height * (350 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hq_left(self):
        """
        从右向左滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (350 / 375.0)
        start_y = height * (350 / 667.0)
        end_x = width * (240 / 375.0)
        end_y = height * (350 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hq_up(self):
        """
        从下向上滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (220 / 375.0)
        start_y = height * (500 / 667.0)
        end_x = width * (220 / 375.0)
        end_y = height * (220 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def hq_down(self):
        """
        从上向下滑动
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        start_x = width * (220 / 375.0)
        start_y = height * (220 / 667.0)
        end_x = width * (220 / 375.0)
        end_y = height * (500 / 667.0)
        self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

    def cell01_click(self):
        """
        某些列表中的元素过多，按照路径点击第一行元素可能因查找时间过长会报错，因此使用坐标点击
        :return:
        """
        el1 = self.w.get_window_size()
        width = el1.get('width')
        height = el1.get('height')
        tap_x = width * (42 / 375.0)
        tap_y = height * (124 / 667.0)
        self.w.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": tap_x, "y": tap_y})