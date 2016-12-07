# -*- coding: utf-8 -*-

from pages.hangqing.bankuai_page import BankuaiPage
from pages.public.public_page import PublicPage
from pages.hangqing.hangqing_page import HangqingPage
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.hangqing.hangqing_gengduo_page import HangqingGengduoPage
from pages.public.public_method import PublicMethod
from pages.zixuangu.kanZhulizijin_page import KanZhulizijinPage
from time import sleep

caseName = 'test_hangqing_bankuai'
#进入板块
def tst_step1(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    bankuai_page = BankuaiPage(driver)
    public_method = PublicMethod(driver)

    # step1-2
    public_page.hangqing_button.click()
    hangqing_page.bankuai_btn.click()
    picName = ' 行情-板块_3'
    public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
    assert bankuai_page.hy_histogram_title

#板块柱状图
def tst_step2(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    bankuai_page = BankuaiPage(driver)
    kanzhulizijin_page = KanZhulizijinPage(driver)
    gengduo_page = HangqingGengduoPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    public_method = PublicMethod(driver)

    public_page.hangqing_button.click()
    hangqing_page.bankuai_btn.click()

    bankuai_page.hy_histogram_gengduo.click()
    picName = '板块-行业主力净流入更多_4'
    public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
    assert kanzhulizijin_page.hangye_btn
    gengduo_page.fanhui_btn.click()
    assert bankuai_page.hy_histogram_title
    bankuai_page.glide_left()
    picName = '板块-柱状图左滑概念_6'
    public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
    assert bankuai_page.gn_histogram_title
    bankuai_page.gn_histogram_gengduo.click()
    picName = '板块-概念主力净流入更多_7'
    public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
    assert kanzhulizijin_page.gainian_btn
    gengduo_page.fanhui_btn.click()
    bankuai_page.glide_left()
    assert bankuai_page.hy_histogram_title
    for n in range(1, 7):
        eval('bankuai_page.histogram_btn{0}.click()'.format(n))
        fenshikxian_page.change_gupiao(6)
        fenshikxian_page.fanhui_button.click()
    bankuai_page.glide_right()
    assert bankuai_page.gn_histogram_title
    for n in range(1, 7):
        eval('bankuai_page.histogram_btn{0}.click()'.format(n))
        fenshikxian_page.change_gupiao(6)
        fenshikxian_page.fanhui_button.click()
    bankuai_page.glide_right()
    assert bankuai_page.hy_histogram_title

#板块
def test_step15(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    bankuai_page = BankuaiPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)
    public_method = PublicMethod(driver)

    # step2-7
    public_page.hangqing_button.click()
    hangqing_page.bankuai_btn.click()

    bankuai_name = [('hy', '行业更多'), ('gn', '概念更多'), ('zs', '快速涨幅')]
    # 上滑至可见
    el1 = driver.get_window_size()
    width = el1.get('width')
    height = el1.get('height')
    start_x = width * (344 / 375.0)
    start_y = height * (500 / 667.0)
    end_x = width * (344 / 375.0)
    end_y = height * (10 / 667.0)
    driver.swipe(start_x, start_y, end_x, end_y, duration=500)
    sleep(1)

    for name, gengduo in bankuai_name:
        for n in range(1, 7):
            print name, n
            eval('bankuai_page.{0}_btn{1}.click()'.format(name, n))
            fenshikxian_page.change_gupiao(6)
            fenshikxian_page.fanhui_button.click()
        eval('bankuai_page.{0}_gengduo_btn.click()'.format(name))
        picName = '板块-{}_'.format(gengduo)
        public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
        hangqing_gengduo_page.hq_up()
        hangqing_gengduo_page.hq_down()
        hangqing_gengduo_page.hq_down()
        for i in range(5):
            hangqing_gengduo_page.hq_left()
        hangqing_gengduo_page.bankuai_clickOperation()

        lenth = public_method.public_getlength()
        if lenth > 10:
            lenth = 10
        #列表中属性name不显示为板块名称，这里先不做判断
        #title = bankuai_page.cell01_title
        bankuai_page.cell01_title.click()
        #assert fenshikxian_page.title_staText == title
        fenshikxian_page.change_gupiao(5)
        fenshikxian_page.fanhui_button.click()
        hangqing_gengduo_page.fanhui_btn.click()

    public_page.shouye_button.click()




