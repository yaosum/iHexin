#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.touch_action import TouchAction
from pages.gerenzhongxin.gerenzhongxin_page import GerenzhongxinPage
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.gerenzhongxin.gerenzhongxin_page import GerenzhongxinPage
from pages.public.denglu_page import DengluPage
from pages.public.public_method import PublicMethod
from pages.public.public_page import PublicPage
from pages.public.searchStock_page import SearchStockPage
from pages.shouye.home_page import HomePage
from pages.zixuangu.bianjizixuan_page import BianjizixuanPage
from pages.zixuangu.kanZhulizijin_page import KanZhulizijinPage
from pages.zixuangu.optional_page import OptionalPage
from pages.zixuangu.tianjiazixuan_page import TianjiazixuanPage
from pages.zixuangu.wodezichan_page import WodezichanPage
from pages.zixuangu.zixuanDapan_page import ZixuanDapanPage
from pages.zixuangu.zixuangufenzu_page import ZixuangufenzuPage
from pages.zixuangu.zixuangugonggao_page import ZixuangugonggaoPage
from pages.zixuangu.zixuanguxinwen_page import ZixuanguxinwenPage
from pages.zixuangu.zixun_page import ZixunPage
from time import sleep

# 先判断当前是否有账号登录,如果有,则先退出
def test_step0(driver):
    home_page = HomePage(driver)
    gerenzhongxin_page = GerenzhongxinPage(driver)

    if not home_page.gerenzhongxin_btn:
        home_page.yonghu_btn.click()
        sleep(2)
        gerenzhongxin_page.tuichudenglu_btn.click()
        sleep(1)
        if gerenzhongxin_page.tishi_allert:
            gerenzhongxin_page.quedin_btn.click()
            sleep(2)

    # step1
    assert home_page.gerenzhongxin_btn
    assert home_page.feivip_button
    assert home_page.qiehuanyejianmoshi_button
    """
# 默认状态
def test_delete(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    public_method = PublicMethod(driver)
    bianjizixuan_page = BianjizixuanPage(driver)

    public_page.zixuan_button.click()
    optional_page.bianji_button.click()
    lenth = public_method.public_getlength()
    num = 1
    for n in range(lenth):
        cell_text = driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[{}]/UIAStaticText[1]'.format(num))
        if cell_text.text == u"同花顺":
            num += 1
        elif cell_text.text == u"上证指数":
            num += 1
        elif cell_text.text == u"创业板指":
            num += 1
        else:
            cell_text.click()
            sleep(1)
            bianjizixuan_page.shanchu_button.click()

    if bianjizixuan_page.cell003_stock_staText.text == u"上证指数":
        print "情况1"
        bianjizixuan_page.cell003_zhiding_btn.click()
        if bianjizixuan_page.cell002_stock_staText.text == u"同花顺":
            action1 = TouchAction(driver)
            action1.press(bianjizixuan_page.cell002_tuodong_btn).wait(100).move_to(
                bianjizixuan_page.cell003_tuodong_btn).wait(100).release()
            action1.perform()
            sleep(1)
    elif bianjizixuan_page.cell003_stock_staText.text == u"同花顺":
        print "情况2"
        if bianjizixuan_page.cell001_stock_staText.text == u"创业板指":
            action1 = TouchAction(driver)
            action1.press(bianjizixuan_page.cell001_tuodong_btn).wait(100).move_to(
                bianjizixuan_page.cell002_tuodong_btn).wait(100).release()
            action1.perform()
            sleep(1)
    elif bianjizixuan_page.cell003_stock_staText.text == u"创业板指":
        print "情况3"
        action1 = TouchAction(driver)
        action1.press(bianjizixuan_page.cell003_tuodong_btn).wait(100).move_to(
            bianjizixuan_page.cell002_tuodong_btn).wait(100).release()
        action1.perform()
        sleep(1)
        if bianjizixuan_page.cell001_stock_staText.text == u"同花顺":
            bianjizixuan_page.cell003_zhiding_btn.click()

# 首页－>自选
def test_step001(driver):
    home_page = HomePage(driver)
    optional_page = OptionalPage(driver)
    bianjizixuan_page = BianjizixuanPage(driver)
    tianjiazixuan_page = TianjiazixuanPage(driver)
    public_page = PublicPage(driver)
    public_method = PublicMethod(driver)
    denglu_page = DengluPage(driver)
    gerenzhongxin_page = GerenzhongxinPage(driver)

    # step2
    public_page.zixuan_button.click()
    assert optional_page.zixuan_staticText
    assert optional_page.tongbuzixuangu_btn
    assert optional_page.duoshoujiPCtongbu_staText

    public_method.public_tap_element(optional_page.bianji_button)
    assert bianjizixuan_page.bianjizixuan_StaticText
    assert bianjizixuan_page.cell001_stock_staText.text == u'上证指数'
    assert bianjizixuan_page.cell002_stock_staText.text == u'创业板指'
    assert bianjizixuan_page.cell003_stock_staText.text == u'同花顺'

    # step4
    bianjizixuan_page.tianjiagupiao_button.click()
    assert tianjiazixuan_page.tianjiazixuan_staticText

    tianjiazixuan_page.fanhui_button.click()
    bianjizixuan_page.fanhui_button.click()

# 自选－>看主力资金
def test_step051(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    kanzhulizijin_page = KanZhulizijinPage(driver)
    denglu_page = DengluPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)

    public_page.zixuan_button.click()
    optional_page.zijin_btn.click()

    # step4 点击更多按钮
    # kanzhulizijin_page.gengduo_button.click()
    # step5
    # 点击更多旁边的删除按钮和引导图差不多,只会出现一次,以后在做

    #看资金－自选
    kanzhulizijin_page.denglu_btn.click()
    denglu_page.guanbi_btn.click()
    #看资金－沪深
    kanzhulizijin_page.hushen_btn.click()
    kanzhulizijin_page.hx_ergodic_hushen_zhibiao()
    # 上下滑
    kanzhulizijin_page.hx_upglide()
    kanzhulizijin_page.hx_glide()
    kanzhulizijin_page.hx_glide()
    # 左右滑
    for n in range(4):
        kanzhulizijin_page.hx_left()
    for n in range(3):
        kanzhulizijin_page.hx_right()
    kanzhulizijin_page.cell001.click()
    fenshikxian_page.change_gupiao(5)
    fenshikxian_page.fanhui_button.click()
    #看资金－行业
    kanzhulizijin_page.hangye_btn.click()
    kanzhulizijin_page.hx_ergodic_zhibiao()
    # 上下滑
    kanzhulizijin_page.hx_upglide()
    kanzhulizijin_page.hx_glide()
    kanzhulizijin_page.hx_glide()
    # 左右滑
    for n in range(4):
        kanzhulizijin_page.hx_left()
    for n in range(3):
        kanzhulizijin_page.hx_right()
    kanzhulizijin_page.cell001.click()
    fenshikxian_page.change_gupiao(5)
    fenshikxian_page.fanhui_button.click()
    #看资金－概念
    kanzhulizijin_page.gainian_btn.click()
    kanzhulizijin_page.hx_ergodic_zhibiao()
    # 上下滑
    kanzhulizijin_page.hx_upglide()
    kanzhulizijin_page.hx_glide()
    kanzhulizijin_page.hx_glide()
    # 左右滑
    for n in range(4):
        kanzhulizijin_page.hx_left()
    for n in range(3):
        kanzhulizijin_page.hx_right()
    kanzhulizijin_page.cell001.click()
    fenshikxian_page.change_gupiao(5)
    fenshikxian_page.fanhui_button.click()

    kanzhulizijin_page.fanhui_btn.click()

# 自选－> 资产页面
def test_step019(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    wodezichan_page = WodezichanPage(driver)
    public_page.zixuan_button.click()
    optional_page.zichan_btn.click()
    # step20 返回
    assert wodezichan_page.wodezichan_staText
    wodezichan_page.fanhui_btn.click()

# 自选－> 沪,深,创大盘页面
def test_step52(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    zixuanDapan_page = ZixuanDapanPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)

    public_page.zixuan_button.click()
    # step22-40
    optional_page.zixuanIndexItemName_staText.click()
    zixuanDapan_page.shen_btn.click()
    zixuanDapan_page.chuang_btn.click()
    zixuanDapan_page.hx_left()
    sleep(1)
    zixuanDapan_page.shen_btn.click()
    zixuanDapan_page.hu_btn.click()
    zixuanDapan_page.hx_right()
    sleep(1)
    zixuanDapan_page.hx_tapblank()
    optional_page.zixuanIndexItemName_staText.click()
    zixuanDapan_page.shen_btn.click()
    zixuanDapan_page.hx_tapblank()
    optional_page.zixuanIndexItemName_staText.click()
    zixuanDapan_page.chuang_btn.click()
    zixuanDapan_page.hx_tapblank()

    optional_page.zixuanIndexItemName_staText.click()
    zixuanDapan_page.fenshitu_scr.click()
    fenshikxian_page.change_gupiao(3)
    fenshikxian_page.fanhui_button.click()

#自选－>编辑自选－>添加股票
def test_step005(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    tianjiazixuan_page = TianjiazixuanPage(driver)
    bianjizixuan_page = BianjizixuanPage(driver)
    searchStock_page = SearchStockPage(driver)
    public_method = PublicMethod(driver)

    # step5-10
    public_page.zixuan_button.click()
    optional_page.bianji_button.click()
    bianjizixuan_page.tianjiagupiao_button.click()
    sleep(1)
    # 添加股票
    stocks = [('AU9999', 'addHJ9999_btn'), ('600000', 'addPFYH_btn'), ('000001', 'addPAYH_btn'),
              ('900901', 'addYSBG_btn'), ('200011', 'addSWYB_btn'), ('010107', 'add21GZ_btn'),
              ('100213', 'addGZ0213_btn'), ('500058', 'addJJYF_btn'), ('150008', 'addRHXK_btn'),
              ('400002', 'addCB5_btn'), ('399001', 'addSZCZ_btn'), ('dji', 'addDQS_btn'), ('BIDU', 'addBD_btn'),
              ('510050', 'add50ETF_btn'), ('TJAG00', 'addY15_btn'), ('00001', 'addCH_btn'), ('hsi', 'addHSZS_btn')]
    for stockCode, stockName in stocks:
        print stockCode, stockName
        searchStock_page.hx_send_keys(stockCode)
        try:
            eval('tianjiazixuan_page.{}.click()'.format(stockName))
        except:
            print '该股票已添加过'
        tianjiazixuan_page.qingchuwenben_button.click()
    # step11
    tianjiazixuan_page.fanhui_button.click()
    sleep(1)
    bianjizixuan_page.fanhui_button.click()
    sleep(1)

    public_method.public_tap_element(optional_page.bianji_button)
    # 对添加的股票进行判断
    assert optional_page.Y15_stock_staText
    assert optional_page.ETF50_stock_staText
    assert optional_page.BD_stock_staText
    assert optional_page.DQS_stock_staText
    assert optional_page.SZCZ_stock_staText
    assert optional_page.CB5_stock_staText
    assert optional_page.RHXK_stock_staText
    assert optional_page.JJYF_stock_staText
    assert optional_page.GZ0213_stock_staText
    assert optional_page.GZ217_stock_staText
    assert optional_page.SWYB_stock_staText
    assert optional_page.YSBG_stock_staText
    assert optional_page.PAYH_stock_staText
    assert optional_page.PFYH_stock_staText
    assert optional_page.HJ9999_stock_staText

    bianjizixuan_page.fanhui_button.click()

# 自选－>编辑自选->置顶
def test_step14(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    bianjizixuan_page = BianjizixuanPage(driver)
    public_method = PublicMethod(driver)

    # step14
    public_page.zixuan_button.click()
    # step15
    optional_page.bianji_button.click()
    bianjizixuan_page.hx_upglide()
    bianjizixuan_page.hx_upglide()
    bianjizixuan_page.hx_upglide()
    sleep(1)

    lenth = public_method.public_getlength()
    # 置顶三次操作
    for n in range(3):
        eval(
            'driver.find_element_by_xpath('
            '"//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[{0}]/UIAButton[2]").click()'.format(lenth))
        sleep(1)
    # 第一条为上证指数
    bianjizixuan_page.fanhui_button.click()

    public_method.public_tap_element(optional_page.bianji_button)
    sleep(1)
    assert bianjizixuan_page.cell001_stock_staText.text == u'上证指数'
    assert bianjizixuan_page.cell002_stock_staText.text == u'创业板指'
    assert bianjizixuan_page.cell003_stock_staText.text == u'同花顺'

    bianjizixuan_page.fanhui_button.click()


# 自选－> 编辑自选－> 拖动股票
def test_step18(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    bianjizixuan_page = BianjizixuanPage(driver)
    public_method = PublicMethod(driver)

    # step 49 点击自选
    public_page.zixuan_button.click()
    public_method.public_tap_element(optional_page.bianji_button)

    action1 = TouchAction(driver)
    action1.press(bianjizixuan_page.cell002_tuodong_btn).wait(100).move_to(bianjizixuan_page.cell001_tuodong_btn).wait(
        100).release()
    action1.perform()
    action2 = TouchAction(driver)
    action2.press(bianjizixuan_page.cell003_tuodong_btn).wait(100).move_to(bianjizixuan_page.cell001_tuodong_btn).wait(
        100).release()
    action2.perform()
    sleep(1)
    bianjizixuan_page.fanhui_button.click()
    sleep(1)

    public_method.public_tap_element(optional_page.bianji_button)

    assert bianjizixuan_page.cell001_stock_staText.text == u'同花顺'
    assert bianjizixuan_page.cell002_stock_staText.text == u'创业板指'
    assert bianjizixuan_page.cell003_stock_staText.text == u'上证指数'

    bianjizixuan_page.fanhui_button.click()

#自选－>编辑自选->删除
def test_step20(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    bianjizixuan_page = BianjizixuanPage(driver)

    # step14
    public_page.zixuan_button.click()
    # step15
    optional_page.bianji_button.click()
    # 删除前三支股票
    bianjizixuan_page.cell001_btn.click()
    bianjizixuan_page.cell002_btn.click()
    bianjizixuan_page.cell003_btn.click()
    bianjizixuan_page.shanchu_button.click()
    # step19
    bianjizixuan_page.fanhui_button.click()

#首页－>搜索，进入股票分时页面->添加股票
def test_step21(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    searchStock_page = SearchStockPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    bianjizixuan_page = BianjizixuanPage(driver)
    public_method = PublicMethod(driver)

    # step20
    optional_page.sousuo_button.click()
    sleep(1)
    searchStock_page.hx_send_keys('1A0001')
    try:
        searchStock_page.zixuanadd_button.click()
    except:
        print "1A0001已添加"
    searchStock_page.qingchuwenben_button.click()
    searchStock_page.hx_send_keys('399006')
    sleep(1)
    try:
        fenshikxian_page.jiazixuan_staText.click()
    except:
        print "399006已添加"
    fenshikxian_page.fanhui_button.click()
    optional_page.sousuo_button.click()
    sleep(1)
    searchStock_page.hx_send_keys('300033')
    sleep(1)
    try:
        fenshikxian_page.jiazixuan_staText.click()
    except:
        print "300033已添加"
    fenshikxian_page.fanhui_button.click()
    public_page.zixuan_button.click()

    public_method.public_tap_element(optional_page.bianji_button)

    assert bianjizixuan_page.cell001_stock_staText.text == u'同花顺'
    assert bianjizixuan_page.cell002_stock_staText.text == u'创业板指'
    assert bianjizixuan_page.cell003_stock_staText.text == u'上证指数'

    bianjizixuan_page.fanhui_button.click()

#自选－>上下滑动->排序,取消排序
def test_step90(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)

    public_page.zixuan_button.click()

    # step93  自选列表排序操作
    optional_page.hx_zixuan_ergodic()

    # step90 上下滑
    optional_page.hx_upglide()
    optional_page.hx_glide()
    optional_page.hx_glide()
    # step91  左右滑
    optional_page.hx_right()
    optional_page.hx_left()

    # step 106
    optional_page.pageGotoFenshikxian()
    sleep(1)

#自选->新闻／研报
def test_step69(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    zixuanguxinwen_page = ZixuanguxinwenPage(driver)
    zixun_page = ZixunPage(driver)

    public_page.zixuan_button.click()
    optional_page.xinwen_btn.click()
    assert zixuanguxinwen_page.zixuanguxinwen_staText
    zixuanguxinwen_page.hx_upglide()
    zixuanguxinwen_page.hx_downglide()
    zixuanguxinwen_page.hx_downglide()
    num = len(driver.find_elements_by_xpath("//UIATableCell[@name]"))
    if num > 0:
        zixuanguxinwen_page.cell01.click()
        zixun_page.fanhui_btn.click()
    else:
        print("自选-->新闻/研报-->新闻列表为空!")
    zixuanguxinwen_page.yanbao_btn.click()
    zixuanguxinwen_page.hx_upglide()
    zixuanguxinwen_page.hx_downglide()
    zixuanguxinwen_page.hx_downglide()
    num = len(driver.find_elements_by_xpath("//UIATableCell[@name]"))
    if num > 0:
        zixuanguxinwen_page.cell01.click()
        zixun_page.fanhui_btn.click()
    else:
        print("自选-->新闻/研报-->研报列表为空!")
    zixuanguxinwen_page.fanhui_btn.click()

# 自选－>自选股公告
def test_step80(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    zixuangugonggao_page=ZixuangugonggaoPage(driver)
    zixun_page = ZixunPage(driver)

    public_page.zixuan_button.click()
    optional_page.gonggao_btn.click()
    assert zixuangugonggao_page.zixuangugonggao_staText.text == u'自选股公告'
    zixuangugonggao_page.hx_upglide()
    zixuangugonggao_page.hx_downglide()
    zixuangugonggao_page.hx_downglide()
    zixuangugonggao_page.cell01.click()

    zixun_page.fanhui_btn.click()
    zixuangugonggao_page.fanhui_btn.click()

# 自选－>长按操作
def t_step104(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)

    public_page.zixuan_button.click()

    optional_page.zuixin_staText.click()
    optional_page.hx_longPress(optional_page.cell001)
    optional_page.zhidi_btn.click()
    # 待扩展
    optional_page.quxiaopaixu_btn.click()
    optional_page.zuixin_staText.click()
    optional_page.hx_upglide()
    optional_page.hx_longPress(optional_page.cell017)
    optional_page.zhiding_btn.click()
    optional_page.quxiaopaixu_btn.click()
    optional_page.hx_glide()
    optional_page.hx_longPress(optional_page.cell001)
    optional_page.shanchu_btn.click()
    optional_page.hx_longPress(optional_page.cell001)
    optional_page.shanchu_btn.click()

# 自选－>自选股分组
def test_step130_144(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    zixuangufenzu_page = ZixuangufenzuPage(driver)

    public_page.zixuan_button.click()
    optional_page.fenzu_btn.click()
    #zixuangufenzu_page.xinjianfenzu_btn.click()
    #zixuangufenzu_page.guanbi_btn.click()
    #zixuangufenzu_page.guanlifenzu_btn.clcik()
    #zixuangufenzu_page.guanbi_btn.click()
    zixuangufenzu_page.chakanxiangqing_btn.click()
    sleep(1)
    zixuangufenzu_page.guanbi_btn.click()

    zixuangufenzu_page.zixuangu_btn.click()
    optional_page.zx_right()
    optional_page.zx_left()
    optional_page.fenzu_btn.click()

    zixuangufenzu_page.hx_tapblank()
    """