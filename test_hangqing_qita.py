# -*- coding: utf-8 -*-
from pages.hangqing.aijijin_page import LovejijinPage
from pages.public.public_method import Public_method
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
from time import sleep

# step4-56 全球市场---国内期货和外汇
def test_step1(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    qita_page = Qita(driver)
    qita_qihuo_page = QitaQihuoPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)
    public_method = Public_method(driver)

    # step2
    public_page.hangqing_button.click()
    # step3
    hangqing_page.qita_btn.click()

    el1 = driver.get_window_size()
    width = el1.get('width')
    height = el1.get('height')

    # step4-56 全球市场---国内期货和外汇
    name_list = ['gn_qihuo_btn', 'waihui_btn']
    for name in name_list:
        eval('qita_page.{}.click()'.format(name))
        assert qita_qihuo_page.zhangfu_statictext
        public_method.hx_tap_element(qita_qihuo_page.zhangdiefu_btn)
        assert qita_qihuo_page.zhangdie_statictext
        public_method.hx_tap_element(qita_qihuo_page.zhangdiefu_btn)
        assert qita_qihuo_page.zhangfu_statictext

        hangqing_gengduo_page.hq_up()
        hangqing_gengduo_page.hq_down()
        hangqing_gengduo_page.hq_down()

        title = qita_qihuo_page.cell01_title.text

        click_x = width * (44 / 375.0)
        click_y = height * (123 / 667.0)
        driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": click_x, "y": click_y})
        assert fenshikxian_page.title_staText.text == title
        length = int(len(driver.find_elements_by_xpath("//UIATableCell[@name]")))
        fenshikxian_page.change_gupiao(5)
        fenshikxian_page.fanhui_button.click()
        qita_qihuo_page.fanhui_button.click()

# 国外期货
def test_step24(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    qita_page = Qita(driver)
    qita_qihuo_page = QitaQihuoPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)

    # step2
    public_page.hangqing_button.click()
    # step3
    hangqing_page.qita_btn.click()

    qita_page.gw_qihuo_btn.click()

    el1 = driver.get_window_size()
    width = el1.get('width')
    height = el1.get('height')

    hangqing_gengduo_page.hq_up()
    hangqing_gengduo_page.hq_down()
    #title = qita_qihuo_page.cell01_title.text
    length = int(len(driver.find_elements_by_xpath("//UIATableCell[@name]")))

    click_x = width * (40 / 375.0)
    click_y = height * (111 / 667.0)
    driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": click_x, "y": click_y})
   #assert fenshikxian_page.title_staText.text == title #外部名称不是分时页面的名称
    fenshikxian_page.change_gupiao(length)
    fenshikxian_page.fanhui_button.click()
    qita_qihuo_page.fanhui_button.click()
    public_page.shouye_button.click()

#50ETF
def test_step34(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    qita_page = Qita(driver)
    qita_qihuo_page = QitaQihuoPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)
    qita_50ETF_page = Qita50ETFPage(driver)
    public_method = Public_method(driver)

    # step2
    public_page.hangqing_button.click()
    # step3
    hangqing_page.qita_btn.click()

    qita_page.gp_qiquan_btn.click()
    hangqing_gengduo_page.qita_gpqq_clickOperation()
    # step34-37
    hangqing_gengduo_page.cell01.click()
    qita_50ETF_page.cell_etf_btn.click()
    fenshikxian_page.hx_right()
    fenshikxian_page.hx_left()
    fenshikxian_page.fanhui_button.click()

    # step38
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


    public_method.hx_tap_element(qita_50ETF_page.group1)
    public_method.hx_tap_element(qita_50ETF_page.group4)
    public_method.hx_tap_element(qita_50ETF_page.group3)
    public_method.hx_tap_element(qita_50ETF_page.group2)
    public_method.hx_tap_element(qita_50ETF_page.group1)

    #长按方法，易出错，这里先不运行这段脚本
    #driver.tap([(80, 216)], duration=0.5)
    #fenshikxian_page.change_gupiao(5)
    #fenshikxian_page.fanhui_button.click()

    qita_50ETF_page.fanhui_button.click()
    qita_qihuo_page.fanhui_button.click()
    public_page.shouye_button.click()

# 上海黄金
def test_step57(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    qita_page = Qita(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)

    # step2
    public_page.hangqing_button.click()
    # step3
    hangqing_page.qita_btn.click()

    # step57-72
    qita_page.sh_huangjin_btn.click()
    for n in range(2):
        hangqing_gengduo_page.hq_left()
    title = hangqing_gengduo_page.cell01_title.text
    length = int(len(driver.find_elements_by_xpath("//UIATableCell[@name]")))
    hangqing_gengduo_page.cell01.click()
    assert fenshikxian_page.title_staText.text == title
    fenshikxian_page.change_gupiao(5)
    fenshikxian_page.fanhui_button.click()
    hangqing_gengduo_page.fanhui_btn.click()

#天津贵金属
def test_step58(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    qita_page = Qita(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    qita_tianjinguijinshu_page = QitaTianjinguijinshuPage(driver)
    denglu_page = DengluPage(driver)
    kefuzhongxin_page = Kefuzhongxin(driver)

    # step2
    public_page.hangqing_button.click()
    # step3
    hangqing_page.qita_btn.click()

    qita_page.tj_guijinshu_btn.click()
    qita_tianjinguijinshu_page.kaihu_btn.click()
    denglu_page.guanbi_btn.click()
    qita_tianjinguijinshu_page.kehufuwuzhongxin_btn.click()
    kefuzhongxin_page.fanhui_btn.click()
    for n in range(2):
        qita_tianjinguijinshu_page.tjgjs_left()
    qita_tianjinguijinshu_page.tjgjs_clickOperation()
    #天津贵金属的股票分时页面显示的名称和列表显示的股票名称不一致
    #title = qita_tianjinguijinshu_page.cell01_title.text
    length = int(len(driver.find_elements_by_xpath("//UIATableCell[@name]")))
    qita_tianjinguijinshu_page.cell01.click()
    #assert fenshikxian_page.title_staText.text == title
    fenshikxian_page.change_gupiao(5)
    fenshikxian_page.fanhui_button.click()
    qita_tianjinguijinshu_page.fanhui_button.click()

# 基金
def test_step73(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    qita_page = Qita(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)

    # step2
    public_page.hangqing_button.click()
    # step3
    hangqing_page.qita_btn.click()

    # 基金
    name_list = ['hushen_fbjj_btn', 'shangzheng_fbjj_btn', 'shenzheng_fbjj_btn']
    for name in name_list:
        eval('qita_page.{}.click()'.format(name))
        for n in range(4):
            hangqing_gengduo_page.hq_left()
        hangqing_gengduo_page.jijin_clickOperation()
        hangqing_gengduo_page.hq_up()
        hangqing_gengduo_page.hq_down()
        hangqing_gengduo_page.hq_down()
        #title = hangqing_gengduo_page.cell01_title.text
        length = int(len(driver.find_elements_by_xpath("//UIATableCell[@name]")))
        if length > 100:
            length = 100
        hangqing_gengduo_page.cell01_click()
        #assert fenshikxian_page.title_staText.text == title
        fenshikxian_page.change_gupiao(5)
        fenshikxian_page.fanhui_button.click()
        hangqing_gengduo_page.fanhui_btn.click()

# 个股和债券
def test_step74(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    qita_page = Qita(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)

    # step2
    public_page.hangqing_button.click()
    # step3
    hangqing_page.qita_btn.click()

    # 个股和债券
    name_list = ['shangzhengA_btn', 'shangzhengB_btn', 'shenzhenA_btn', 'shenzhenB_btn', 'zhongxiaoban_btn',
                 'chuangyeban_btn', 'sanban_btn', 'fengxianjingshi_btn', 'hushenzhaiquan_btn', 'shangzhengzhaiquan_btn',
                 'shenzhenzhaiquan_btn']
    for name in name_list:
        eval('qita_page.{}.click()'.format(name))
        for n in range(5):
            hangqing_gengduo_page.hq_up()
        for n in range(6):
            hangqing_gengduo_page.hq_down()
        for n in range(4):
            hangqing_gengduo_page.hq_left()
        # hangqing_gengduo_page.jijin_clickOperation()
        # hangqing_gengduo_page.cell01.click()
        #title = hangqing_gengduo_page.cell01_title.text

        hangqing_gengduo_page.cell01_click()
        #assert fenshikxian_page.title_staText.text == title
        fenshikxian_page.change_gupiao(5)
        fenshikxian_page.fanhui_button.click()
        hangqing_gengduo_page.fanhui_btn.click()

#个股---新三板
def test_step75(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    qita_page = Qita(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)
    qita_xinsanban_page = QitaXinsanbanPage(driver)

    #step2
    public_page.hangqing_button.click()
    #step3
    hangqing_page.qita_btn.click()

    #个股---新三板
    qita_page.xinsanban_btn.click()

    #三板做市
    qita_xinsanban_page.sanbanzuoshi_btn.click()
    sleep(1)
    assert fenshikxian_page.title_staText.text == u'三板做市'
    fenshikxian_page.hx_left()
    fenshikxian_page.hx_right()
    fenshikxian_page.fanhui_button.click()
    #三板成指
    qita_xinsanban_page.sanbanchengzhi_btn.click()
    sleep(1)
    assert fenshikxian_page.title_staText.text == u'三板成指'
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
        #hangqing_gengduo_page.jijin_clickOperation()
        qita_xinsanban_page.cell01_chengfengu_click()
        #title = qita_xinsanban_page.cell01_title_chengfengu.text
        #length = int(len(driver.find_elements_by_xpath("//UIATableCell[@name]")))
        #if length > 100:
            #length = 100
        #assert fenshikxian_page.title_staText.text == title
        fenshikxian_page.change_gupiao(5)
        fenshikxian_page.fanhui_button.click()
        qita_xinsanban_page.sanbanchengzhi_tab.click()
    qita_xinsanban_page.sanbanzuoshi_tab.click()
    hangqing_gengduo_page.fanhui_btn.click()

    list = ['chuangxin_btn', 'jichu_btn', 'zuoshi_btn', 'xieyi_btn', 'youxiangu_btn']
    for name_head in list:
        eval('qita_xinsanban_page.{}.click()'.format(name_head))
        sub_list = [('group1', 'gengduo1'), ('group2', 'gengduo2'), ('group3', 'gengduo3')]
        for group, gengduo in sub_list:
            title = qita_xinsanban_page.cell1_title.text
            qita_xinsanban_page.cell1.click()
            #assert fenshikxian_page.title_staText.text == title
            fenshikxian_page.change_gupiao(1)
            fenshikxian_page.fanhui_button.click()

            eval('qita_xinsanban_page.{}.click()'.format(gengduo))

            for n in range(5):
                hangqing_gengduo_page.hq_up()
            for n in range(6):
                hangqing_gengduo_page.hq_down()
            for n in range(4):
                hangqing_gengduo_page.hq_left()

            #hangqing_gengduo_page.jijin_clickOperation()
            #title = hangqing_gengduo_page.cell01_title.text
            hangqing_gengduo_page.cell01_click()
            #assert fenshikxian_page.title_staText.text == title
            fenshikxian_page.change_gupiao(1)
            fenshikxian_page.fanhui_button.click()
            hangqing_gengduo_page.fanhui_btn.click()
            eval('qita_xinsanban_page.{}.click()'.format(group))

        qita_xinsanban_page.group3.click()
        qita_xinsanban_page.group2.click()
        qita_xinsanban_page.group1.click()

    hangqing_gengduo_page.fanhui_btn.click()

#放贷宝
def test_step135(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    qita_page = Qita(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    qita_hushenguozhai_page = QitaHushenguozhai(driver)

    # step2
    public_page.hangqing_button.click()
    # step3
    hangqing_page.qita_btn.click()

    qita_page.hushenguozhai_btn.click()
    title = qita_hushenguozhai_page.cell1_title.text
    length = int(len(driver.find_elements_by_xpath("//UIATableCell[@name]")))
    qita_hushenguozhai_page.cell1.click()
    assert fenshikxian_page.title_staText.text == title
    fenshikxian_page.change_gupiao(length)
    fenshikxian_page.fanhui_button.click()

    qita_hushenguozhai_page.shenshi_btn.click()
    title = qita_hushenguozhai_page.cell1_title.text
    length = int(len(driver.find_elements_by_xpath("//UIATableCell[@name]")))
    qita_hushenguozhai_page.cell1.click()
    assert fenshikxian_page.title_staText.text == title
    fenshikxian_page.change_gupiao(length)
    fenshikxian_page.fanhui_button.click()
    qita_hushenguozhai_page.hushi_btn.click()
    qita_hushenguozhai_page.fanhui_btn.click()

#／退市整理
def test_step146(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    qita_page = Qita(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)

    # step2
    public_page.hangqing_button.click()
    # step3
    hangqing_page.qita_btn.click()

    qita_page.tuishizhengli_btn.click()
    hangqing_gengduo_page.hq_up()
    hangqing_gengduo_page.hq_down()
    hangqing_gengduo_page.hq_down()
    hangqing_gengduo_page.hq_left()
    length = int(len(driver.find_elements_by_xpath("//UIATableCell[@name]")))
    hangqing_gengduo_page.jijin_clickOperation()
    hangqing_gengduo_page.fanhui_btn.click()

"""
#爱基金
def test_step79(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    qita_page = Qita(driver)
    aijijin_page = LovejijinPage(driver)

    # step2
    public_page.hangqing_button.click()
    # step3
    hangqing_page.qita_btn.click()

    qita_page.tonghuashunaijijin_btn.click()
    aijijin_page.shouyipaihang_text.click()
    assert aijijin_page.shouyipaihang_text
    aijijin_page.fanhui_btn.click()
    assert aijijin_page.aijijin_text
    aijijin_page.fanhui_btn.click()
"""




