#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from pages.public.public_page import PublicPage
from pages.zixuangu.optional_page import OptionalPage
from pages.zixuangu.zixuanguxinwen_page import ZixuanguxinwenPage
def test_step1(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    zixuan_xinwen_page = ZixuanguxinwenPage(driver)
    public_page.zixuan_button.click()
    for n in range(1000):
        optional_page.xinwen_btn.click()
        driver.tap([(200, 127)])
        zixuan_xinwen_page.fanhui_btn.click()
        zixuan_xinwen_page.yanbao_btn.click()
        driver.tap([(200, 127)])
        zixuan_xinwen_page.fanhui_btn.click()
        zixuan_xinwen_page.xinwen_btn.click()
        zixuan_xinwen_page.fanhui_btn.click()
        print('第{}次运行成功'.format(n))