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
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)

    # step2-7
    public_page.hangqing_button.click()
    hangqing_page.bankuai_btn.click()
    groups = ['group1_btn', 'group2_btn']
    dengduos = ['hy_gengduo_btn', 'gn_gengduo_btn']
    for n in range(2):
        if n == 0:
            bankuai_page.cell1_1.click()
        else:
            bankuai_page.cell2_1.click()
        fenshikxian_page.change_gupiao(5)
        fenshikxian_page.fanhui_button.click()

        # step8
        if n == 0:
            bankuai_page.hy_gengduo_btn.click()
        else:
            bankuai_page.gn_gengduo_btn.click()
        hangqing_gengduo_page.hq_left();
        hangqing_gengduo_page.hq_left();
        hangqing_gengduo_page.bk_clickOperation()
        hangqing_gengduo_page.hq_up()
        hangqing_gengduo_page.hq_up()
        hangqing_gengduo_page.hq_down()
        hangqing_gengduo_page.hq_down()
        lenth = len(driver.find_elements_by_xpath("//UIATableCell[@name]"))
        if lenth > 10:
            lenth = 10;
            hangqing_gengduo_page.cell01.click()
        if lenth > 1:
            fenshikxian_page.change_gupiao(lenth)
        fenshikxian_page.fanhui_button.click()
        hangqing_gengduo_page.fanhui_btn.click()

