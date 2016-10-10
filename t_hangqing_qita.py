# -*- coding: utf-8 -*-

from pages.public.public_page import PublicPage
from pages.hangqing.hangqing_page import HangqingPage
from pages.hangqing.qita_page import Qita
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.hangqing.qita_qihuo_page import QitaQihuoPage
from pages.hangqing.hangqing_gengduo_page import HangqingGengduoPage
from pages.hangqing.qita_50ETF_page import Qita50ETFPage
from pages.hangqing.qita_tianjinguijinshu_page import QitaTianjinguijinshuPage
from pages.public.denglu_page import DengluPage
from pages.public.kefuzhongxin_page import Kefuzhongxin
from pages.hangqing.qita_xinsanban_page import QitaXinsanbanPage
from pages.hangqing.qita_hushenguozhai_page import QitaHushenguozhai

def test_step1(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    qita_page = Qita(driver)
    qita_qihuo_page = QitaQihuoPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)
    qita_50ETF_page = Qita50ETFPage(driver)
    qita_tianjinguijinshu_page = QitaTianjinguijinshuPage(driver)
    denglu_page = DengluPage(driver)
    kefuzhongxin_page = Kefuzhongxin(driver)
    qita_xinsanban_page = QitaXinsanbanPage(driver)
    qita_hushenguozhai_page = QitaHushenguozhai(driver)

    #step2
    public_page.hangqing_button.click()
    #step3
    hangqing_page.qita_btn.click()
    """
    #step4-56 全球市场---国内期货和外汇
    name_list = ['gn_qihuo_btn','waihui_btn']
    for name in name_list:
        eval('qita_page.{}.click()'.format(name))
        for n in range(2):
            driver.execute_script("mobile: tap",{"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 373, "y": 124})
        for n in range(5):
            hangqing_gengduo_page.hq_up()
        for n in range(5):
            hangqing_gengduo_page.hq_down()
        driver.execute_script("mobile: tap",{"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 100, "y": 124})
        fenshikxian_page.change_gupiao(5)
        fenshikxian_page.fanhui_button.click()
        qita_qihuo_page.fanhui_button.click()

    #国外期货
    qita_page.gw_qihuo_btn.click()
    for n in range(2):
        driver.execute_script("mobile: tap",{"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 373, "y": 113})
    for n in range(5):
        hangqing_gengduo_page.hq_up()
    for n in range(6):
        hangqing_gengduo_page.hq_down()
    driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 100, "y": 113})
    fenshikxian_page.change_gupiao(5)
    fenshikxian_page.fanhui_button.click()
    qita_qihuo_page.fanhui_button.click()

    qita_page.gp_qiquan_btn.click()
    hangqing_gengduo_page.qita_gpqq_clickOperation()
    #step34-37
    hangqing_gengduo_page.qita_50ETF_btn.click()
    qita_50ETF_page.cell_etf_btn.click()
    fenshikxian_page.hx_right()
    fenshikxian_page.hx_left()
    fenshikxian_page.fanhui_button.click()

    #step38
    qita_50ETF_page.qtgpqq_up()
    qita_50ETF_page.qtgpqq_down()
    for n in range(3):
        qita_50ETF_page.qtgpqq_L_right()
    for n in range(3):
        qita_50ETF_page.qtgpqq_L_left()
    for n in range(3):
        qita_50ETF_page.qtgpqq_R_left()
    for n in range(3):
        qita_50ETF_page.qtgpqq_R_right()

    qita_50ETF_page.group1.click()
    qita_50ETF_page.group4.click()
    qita_50ETF_page.group3.click()
    qita_50ETF_page.group2.click()
    qita_50ETF_page.group1.click()

    driver.tap([(80, 216)], duration=0.5)

    fenshikxian_page.change_gupiao(5)
    fenshikxian_page.fanhui_button.click()
    qita_50ETF_page.fanhui_button.click()
    qita_qihuo_page.fanhui_button.click()


    #现货市场
    #step57-72
    qita_page.sh_huangjin_btn.click()
    for n in range(2):
        hangqing_gengduo_page.hq_left()
    hangqing_gengduo_page.cell01.click()
    fenshikxian_page.change_gupiao(5)
    fenshikxian_page.fanhui_button.click()
    hangqing_gengduo_page.fanhui_btn.click()


    qita_page.tj_guijinshu_btn.click()
    qita_tianjinguijinshu_page.kaihu_btn.click()
    denglu_page.guanbi_btn.click()
    qita_tianjinguijinshu_page.kehufuwuzhongxin_btn.click()
    kefuzhongxin_page.fanhui_btn.click()
    for n in range(2):
        qita_tianjinguijinshu_page.tjgjs_left()
    qita_tianjinguijinshu_page.tjgjs_clickOperation()
    qita_tianjinguijinshu_page.cell01.click()
    fenshikxian_page.change_gupiao(5)
    fenshikxian_page.fanhui_button.click()
    qita_tianjinguijinshu_page.fanhui_button.click()


    #基金
    name_list = ['hushen_fbjj_btn', 'shangzheng_fbjj_btn', 'shenzheng_fbjj_btn']
    for name in name_list:
        eval('qita_page.{}.click()'.format(name))
        for n in range(4):
            hangqing_gengduo_page.hq_left()
        hangqing_gengduo_page.jijin_clickOperation()
        hangqing_gengduo_page.cell01.click()
        fenshikxian_page.change_gupiao(5)
        fenshikxian_page.fanhui_button.click()
        hangqing_gengduo_page.fanhui_btn.click()
    """
    #个股和债券
    name_list = ['shangzhengA_btn', 'shangzhengB_btn', 'shenzhenA_btn', 'shenzhenB_btn', 'zhongxiaoban_btn', 'chuangyeban_btn',
                 'sanban_btn', 'fengxianjingshi_btn','hushenzhaiquan_btn','shangzhengzhaiquan_btn','shenzhenzhaiquan_btn']
    for name in name_list:
        eval('qita_page.{}.click()'.format(name))
        for n in range(5):
            hangqing_gengduo_page.hq_up()
        for n in range(6):
            hangqing_gengduo_page.hq_down()
        for n in range(4):
            hangqing_gengduo_page.hq_left()
        hangqing_gengduo_page.jijin_clickOperation()
        hangqing_gengduo_page.cell01.click()
        fenshikxian_page.change_gupiao(5)
        fenshikxian_page.fanhui_button.click()
        hangqing_gengduo_page.fanhui_btn.click()


    #个股---新三板
    qita_page.xinsanban_btn.click()
    #三板做市
    qita_xinsanban_page.sanbanzuoshi_btn.click()
    fenshikxian_page.hx_left()
    fenshikxian_page.hx_right()
    fenshikxian_page.fanhui_button.click()
    #三板成指
    qita_xinsanban_page.sanbanchengzhi_btn.click()
    fenshikxian_page.hx_left()
    fenshikxian_page.hx_right()
    fenshikxian_page.fanhui_button.click()
    #成分股
    qita_xinsanban_page.chengfengu_btn.click()
    for m in range(2):

        for n in range(5):
            hangqing_gengduo_page.hq_up()
        for n in range(6):
            hangqing_gengduo_page.hq_down()
        for n in range(4):
            hangqing_gengduo_page.hq_left()
        hangqing_gengduo_page.jijin_clickOperation()
        hangqing_gengduo_page.cell01.click()
        fenshikxian_page.change_gupiao(5)
        fenshikxian_page.fanhui_button.click()
        hangqing_gengduo_page.fanhui_btn.click()
        hangqing_gengduo_page.sanbanchengzhi_btn.click()
    hangqing_gengduo_page.fanhui_btn.click()

    list = ['chuangxin_btn','jichu_btn','zuoshi_btn','xieyi_btn','youxiangu_btn']
    for name_head in list:
        eval('qita_xinsanban_page.{}.click()'.format(name_head))
        sub_list = [('group1', 'gengduo1'), ('group2', 'gengduo2'), ('group3', 'gengduo3')]
        for group, gengduo in sub_list:
            qita_xinsanban_page.cell1.click()
            fenshikxian_page.change_gupiao(5)
            fenshikxian_page.fanhui_button.click()
            eval('qita_xinsanban_page.{}.click()'.format(gengduo))
            for n in range(5):
                hangqing_gengduo_page.hq_up()
            for n in range(6):
                hangqing_gengduo_page.hq_down()
            for n in range(4):
                hangqing_gengduo_page.hq_left()
            hangqing_gengduo_page.jijin_clickOperation()
            hangqing_gengduo_page.cell01.click()
            fenshikxian_page.change_gupiao(5)
            fenshikxian_page.fanhui_button.click()
            hangqing_gengduo_page.fanhui_btn.click()
            eval('qita_xinsanban_page.{}.click()'.format(group))
        qita_xinsanban_page.group1.click()
        qita_xinsanban_page.group2.click()
        qita_xinsanban_page.group3.click()
    hangqing_gengduo_page.fanhui_btn.click()

    qita_hushenguozhai_page.cell1.click()
    fenshikxian_page.change_gupiao(8)
    fenshikxian_page.fanhui_button.click()
    qita_hushenguozhai_page.shenshi_btn.click()
    qita_hushenguozhai_page.cell1.click()
    fenshikxian_page.change_gupiao(8)
    fenshikxian_page.fanhui_button.click()
    qita_hushenguozhai_page.hushi_btn.click()
    qita_hushenguozhai_page.fanhui_btn.click()

    qita_page.tuishizhengli_btn.click()
    for n in range(5):
        hangqing_gengduo_page.hq_up()
    for n in range(6):
        hangqing_gengduo_page.hq_down()
    for n in range(4):
        hangqing_gengduo_page.hq_left()
    hangqing_gengduo_page.jijin_clickOperation()
    hangqing_gengduo_page.fanhui_btn.click()
