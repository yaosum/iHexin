# -*- coding: utf-8 -*-

from pages.hangqing.bankuai_page import BankuaiPage
from pages.public.public_page import PublicPage
from pages.hangqing.hangqing_page import HangqingPage
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.hangqing.hangqing_gengduo_page import HangqingGengduoPage

#进入板块
def test_step1(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    bankuai_page = BankuaiPage(driver)

    # step1-2
    public_page.hangqing_button.click()
    hangqing_page.bankuai_btn.click()
    assert bankuai_page.group1_btn

#板块页面
def test_step2(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    bankuai_page = BankuaiPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)

    # step2-7
    public_page.hangqing_button.click()
    hangqing_page.bankuai_btn.click()

    bankuais = [['cell1_1', 'group1_btn', 'hy_gengduo_btn'],
                ['cell2_1', 'group2_btn', 'gn_gengduo_btn']]
    #"n = 0 表示行业板块  n == 1 表示概念板块"
    for bankuai in bankuais:
        title = eval('bankuai_page.{0}_title.text'.format(bankuai[0]))
        eval('bankuai_page.{0}.click()'.format(bankuai[0]))
        assert fenshikxian_page.title_staText.text == title
        assert fenshikxian_page.shangyigegupiao_button
        fenshikxian_page.change_gupiao(5)
        fenshikxian_page.fanhui_button.click()

        # step8
        eval('bankuai_page.{0}.click()'.format(bankuai[2]))
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

        fenshikxian_page.change_gupiao(lenth)
        fenshikxian_page.fanhui_button.click()
        hangqing_gengduo_page.fanhui_btn.click()

