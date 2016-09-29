# -*- coding: utf-8 -*-

from pages.public.public_page import PublicPage
from pages.hangqing.hangqing_page import HangqingPage

def step1(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)

    # step2
    public_page.hangqing_button.click()