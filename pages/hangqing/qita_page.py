#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class Qita(PageObject):
    gn_qihuo_btn = page_element(accessibility_id = '国内期货')
    gw_qihuo_btn = page_element(accessibility_id = '国外期货')
    waihui_btn = page_element(accessibility_id = '外汇')
    gp_qiquan_btn = page_element(accessibility_id = '股票期权')

    sh_huangjin_btn = page_element(accessibility_id = '上海黄金')
    tj_guijinshu_btn = page_element(accessibility_id = '天津贵金属')

    tonghuashunaijijin_btn = page_element(accessibility_id = 'ths love jj')

    hushen_fbjj_btn = page_element(accessibility_id = '沪深封闭基金')
    shangzheng_fbjj_btn = page_element(accessibility_id = '上证封闭基金')
    shenzheng_fbjj_btn = page_element(accessibility_id = '深证封闭基金')

    shangzhengA_btn = page_element(accessibility_id = '上证A股')
    shangzhengB_btn = page_element(accessibility_id = '上证B股')
    shenzhenA_btn = page_element(accessibility_id = '深圳A股')
    shenzhenB_btn = page_element(accessibility_id = '深圳B股')
    zhongxiaoban_btn = page_element(accessibility_id = '中小板')
    chuangyeban_btn = page_element(accessibility_id = '创业板')
    xinsanban_btn = page_element(accessibility_id = '新三板')
    sanban_btn = page_element(accessibility_id = '三板')
    fengxianjingshi_btn = page_element(accessibility_id = '风险警示')
    tuishizhengli_btn = page_element(accessibility_id = '退市整理')

    hushenguozhai_btn = page_element(accessibility_id = '沪深国债（放贷宝）')

    hushenzhaiquan_btn = page_element(accessibility_id = '沪深债券')
    shangzhengzhaiquan_btn = page_element(accessibility_id = '上证债券')
    shenzhenzhaiquan_btn = page_element(accessibility_id = '深圳债券')
