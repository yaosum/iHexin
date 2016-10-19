# -*- coding: utf-8 -*-

from pages.hangqing.bankuai_page import BankuaiPage
from pages.public.public_page import PublicPage
from pages.hangqing.hangqing_page import HangqingPage
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.hangqing.hangqing_gengduo_page import HangqingGengduoPage

def test_step1(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    bankuai_page = BankuaiPage(driver)

    # step1-2
    public_page.hangqing_button.click()
    hangqing_page.bankuai_btn.click()
    assert bankuai_page.group1_btn

def test_step2(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    bankuai_page = BankuaiPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)

    # step2-7
    public_page.hangqing_button.click()
    hangqing_page.bankuai_btn.click()

    groups = ['group1_btn', 'group2_btn']
    gengduos = ['hy_gengduo_btn', 'gn_gengduo_btn']
    #"n = 0 表示行业板块  n == 1 表示概念板块"
    for n in range(2):
        if n == 0:
            title = bankuai_page.cell1_1_title.text
            bankuai_page.cell1_1.click()
            assert fenshikxian_page.title_staText.text == title
        else:
            title = bankuai_page.cell2_1_title.text
            bankuai_page.cell2_1.click()
            assert fenshikxian_page.title_staText.text == title
        assert fenshikxian_page.shangyigegupiao_button
        fenshikxian_page.change_gupiao(5)
        fenshikxian_page.fanhui_button.click()
        # step8
        if n == 0:
            bankuai_page.hy_gengduo_btn.click()
        else:
            bankuai_page.gn_gengduo_btn.click()
        hangqing_gengduo_page.hq_left()
        hangqing_gengduo_page.hq_left()
        hangqing_gengduo_page.bk_clickOperation()
        hangqing_gengduo_page.hq_up()
        hangqing_gengduo_page.hq_up()
        hangqing_gengduo_page.hq_down()
        hangqing_gengduo_page.hq_down()
        lenth = len(driver.find_elements_by_xpath("//UIATableCell[@name]"))
        if lenth > 10:
            lenth = 10
            title = hangqing_gengduo_page.cell01_title.text
            hangqing_gengduo_page.cell01.click()
            assert fenshikxian_page.title_staText.text == title

        if lenth > 1:
            fenshikxian_page.change_gupiao(lenth)
            fenshikxian_page.fanhui_button.click()
        hangqing_gengduo_page.fanhui_btn.click()

