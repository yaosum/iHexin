#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element
from pages.public.searchStock_page import SearchStockPage
from time import sleep

class DebugPage(PageObject):
    """
    切换服务器方法
    """
    switch_server_btn = page_element(accessibility_id = '切换服务器')
    search_stock_btn = page_element(accessibility_id = '搜索')
    ip_textview = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATextView[1]/UIATextField[1]')
    port_testview = page_element(xpath = '//UIAApplication[1]/UIAWindow[1]/UIATextView[1]/UIATextField[2]')
    lianjie_btn = page_element(accessibility_id = '连接')

    def switch_server(self, ip, port):
        """
        切换服务器操作
        前置条件:使用该方法的时候,当前界面有搜索按钮
        功   能:切换服务器
        使用方式:直接调用
        :param ip: 服务器的IP地址
        :param port: 服务器的端口
        :return:
        """
        search_stock_page = SearchStockPage(self.w)
        self.search_stock_btn.click()
        search_stock_page.hx_send_keys('10jqka')
        sleep(1)
        self.switch_server_btn.click()
        self.ip_textview.click()
        self.ip_textview.send_keys(ip)
        self.port_testview.click()
        self.port_testview.send_keys(port)
        self.lianjie_btn.click()
