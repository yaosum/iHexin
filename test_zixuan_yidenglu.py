# -*- coding: utf-8 -*-
from time import sleep

from page_object.appium_page_objects import page_element
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.public.denglu_page import DengluPage
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
from pages.index_page import IndexPage
from pages.public.denglu_page import DengluPage
from pages.gerenzhongxin.gerenzhongxin_page import GerenzhongxinPage

# 首页
def test_step1(driver):
    home_page = HomePage(driver)
    denglu_page = DengluPage(driver)
    gerenzhongxin_page = GerenzhongxinPage(driver)
    if home_page.gerenzhongxin_btn.text == u'个人中心':
        home_page.gerenzhongxin_btn.click()
        gerenzhongxin_page.denglu_zhuce_btn.click()
        denglu_page.sign_in('337705299', '123456')
    assert home_page.gerenzhongxin_button
    assert home_page.feivip_button
    assert home_page.qiehuanyejianmoshi_button
    assert home_page.sousuo_button

# 自选股页面
def test_step2(driver):
    optional_page = OptionalPage(driver)
    public_page = PublicPage(driver)
    public_page.zixuan_button.click()
    assert optional_page.zixuan_staticText
    assert optional_page.tongbuzixuangu_btn
    assert optional_page.duoshoujiPCtongbu_staText
    assert optional_page.cell001_stock_staText.text == u'上证指数'
    assert optional_page.cell002_stock_staText.text == u'创业板指'
    assert optional_page.cell003_stock_staText.text == u'同花顺'

# 资金页面
def test_step3(driver):
    optional_page = OptionalPage(driver)
    kanzhulizijin_page = KanZhulizijinPage(driver)
    public_page = PublicPage(driver)
    public_page.zixuan_button.click()
    optional_page.zijin_btn.click()
    assert kanzhulizijin_page.kanzhulizijin_staticText
    assert kanzhulizijin_page.gengduo_button
    assert kanzhulizijin_page.zixuan_btn
    assert kanzhulizijin_page.hushen_btn
    assert kanzhulizijin_page.hangye_btn
    assert kanzhulizijin_page.gainian_btn

    # step4 点击更多按钮
    kanzhulizijin_page.gengduo_button.click()

    # step5
    # 点击更多旁边的删除按钮和引导图差不多,只会出现一次,以后在做

    # step6  点击沪深按钮
    kanzhulizijin_page.hushen_btn.click()
    assert not kanzhulizijin_page.zixuangushunxu_btn
    # 判断列表不为空

    # step7 上滑动
    kanzhulizijin_page.hx_upglide()

    # step8 下滑动
    kanzhulizijin_page.hx_glide()

    # step9 左滑动
    kanzhulizijin_page.hx_left()
    kanzhulizijin_page.hx_left()
    kanzhulizijin_page.hx_left()
    kanzhulizijin_page.hx_left()

    # step10 右滑动
    kanzhulizijin_page.hx_right()
    kanzhulizijin_page.hx_right()
    kanzhulizijin_page.hx_right()

    # step11-18
    kanzhulizijin_page.hx_ergodic_hushen_zhibiao()
    kanzhulizijin_page.hangye_btn.click()
    kanzhulizijin_page.hx_ergodic_zhibiao()
    kanzhulizijin_page.gainian_btn.click()
    kanzhulizijin_page.hx_ergodic_zhibiao()
    kanzhulizijin_page.fanhui_btn.click()

# 资产页面
def test_step19(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    wodezichan_page = WodezichanPage(driver)
    public_page.zixuan_button.click()
    optional_page.zichan_btn.click()
    # step20 返回
    wodezichan_page.fanhui_btn.click()

# 沪,深,创大盘页面
def test_step21(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    searchStock_page = SearchStockPage(driver)
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


# 编辑页面
def test_step41(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    bianjizixuan_page = BianjizixuanPage(driver)
    tianjiazixuan_page = TianjiazixuanPage(driver)
    searchStock_page = SearchStockPage(driver)
    home_page = HomePage(driver)
    fenshikxian_page = FenshiKxianPage(driver)

    public_page.zixuan_button.click()
    optional_page.bianji_button.click()
    assert bianjizixuan_page.bianjizixuan_StaticText

    # step42 进入股票搜索页面
    bianjizixuan_page.tianjiagupiao_button.click()
   # assert tianjiazixuan_page.tianjiazixuan_staticText()
    sleep(1)

    # step43-45 输入股票代码 添加自选股
    stocks = [('600000', 'addPFYH_btn'), ('000001', 'addPAYH_btn'), ('900901', 'addYSBG_btn'),
              ('200011', 'addSWYB_btn'), ('010107', 'add21GZ_btn'),
              ('100213', 'addGZ0213_btn'), ('500058', 'addJJYF_btn'), ('150008', 'addRHXK_btn'),
              ('400002', 'addCB5_btn'), ('399001', 'addSZCZ_btn'),
              ('dji', 'addDQS_btn'), ('BIDU', 'addBD_btn'), ('510050', 'add50ETF_btn'), ('TJAG00', 'addXHBY_btn'),
              ('00001', 'addCH_btn'),
              ('hsi', 'addHSZS_btn')]
    for stockCode, stockName in stocks:
        print stockCode, stockName
        searchStock_page.hx_send_keys(stockCode)
        try:
            eval('tianjiazixuan_page.{}.click()'.format(stockName))
        except:
            print '该股票已添加过'
        tianjiazixuan_page.qingchuwenben_button.click()
    # step 46 返回编辑自选页面
    tianjiazixuan_page.fanhui_button.click()
    # step 47 返回自选页面
    bianjizixuan_page.fanhui_button.click()
    assert optional_page.zixuan_staticText
    assert optional_page.tongbuzixuangu_btn
    assert optional_page.duoshoujiPCtongbu_staText

    # step 48 点击首页
    public_page.shouye_button.click()

#编辑自选
def test_step49(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    bianjizixuan_page = BianjizixuanPage(driver)
    searchStock_page = SearchStockPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)

    # step 49 点击自选
    public_page.zixuan_button.click()

    # step50-52
    optional_page.bianji_button.click()
    bianjizixuan_page.hx_upglide()
    sleep(1)

    # 置顶三次操作
    lenth = len(driver.find_elements_by_xpath("//UIATableCell[@name]"))
    if lenth > 1:
        for n in range(3):
            print n
            bianjizixuan_page.cell010_zhiding_btn.click()
            sleep(1)
    # 第一条为上证指数
    bianjizixuan_page.hx_glide()
    sleep(1)
    #assert bianjizixuan_page.cell001_stock_staText.text == u'上证指数'
    bianjizixuan_page.fanhui_button.click()
    optional_page.hx_glide()
    sleep(1)
    #assert optional_page.cell001_stock_staText.text == u'上证指数'
    # step53
    optional_page.bianji_button.click()
    from appium.webdriver.common.touch_action import TouchAction
    action1 = TouchAction(driver)
    action1.press(bianjizixuan_page.cell002_tuodong_btn).wait(100).move_to(bianjizixuan_page.cell001_tuodong_btn).wait(
        100).release()
    action1.perform()
    action2 = TouchAction(driver)
    action2.press(bianjizixuan_page.cell003_tuodong_btn).wait(100).move_to(bianjizixuan_page.cell001_tuodong_btn).wait(
        100).release()
    action2.perform()
    print optional_page.cell001_stock_staText.text
    #assert optional_page.cell001_stock_staText.text == u'同花顺'
    # step54
    bianjizixuan_page.fanhui_button.click()
    optional_page.bianji_button.click()
    # 删除前三支股票
    bianjizixuan_page.cell001_btn.click()
    bianjizixuan_page.cell002_btn.click()
    bianjizixuan_page.cell003_btn.click()
    bianjizixuan_page.shanchu_button.click()
    # step55
    bianjizixuan_page.fanhui_button.click()

    # step56-66
    optional_page.sousuo_button.click()
    sleep(1)
    searchStock_page.hx_send_keys('1A0001')
    try:
        eval("searchStock_page.zixuanadd_button.click()")
    except:
        print '该股票已添加过'
    searchStock_page.qingchuwenben_button.click()
    searchStock_page.hx_send_keys('399006')
    sleep(1)
    try:
        eval("fenshikxian_page.jiazixuan_staText.click()")
    except:
        print '该股票已添加过'
    fenshikxian_page.fanhui_button.click()
    optional_page.sousuo_button.click()
    sleep(1)
    searchStock_page.hx_send_keys('300033')
    sleep(1)
    try:
        eval("fenshikxian_page.jiazixuan_staText.click()")
    except:
        print '该股票已添加过'
    fenshikxian_page.fanhui_button.click()


#资金
def test_step067_71(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    kanzhulizijin_page = KanZhulizijinPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)

    public_page.zixuan_button.click()
    optional_page.zijin_btn.click()
    kanzhulizijin_page.hx_ergodic_hushen_zhibiao()

    # step 72
    kanzhulizijin_page.cell001.click()
    sleep(1)
    # step73-76
    fenshikxian_page.change_gupiao(17)
    # step 77
    fenshikxian_page.fanhui_button.click()
    kanzhulizijin_page.fanhui_btn.click()

#新闻
def test_step78_88(driver):
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
    zixuanguxinwen_page.cell01.click()
    zixun_page.fanhui_btn.click()
    zixuanguxinwen_page.yanbao_btn.click()
    zixuanguxinwen_page.hx_upglide()
    zixuanguxinwen_page.hx_downglide()
    zixuanguxinwen_page.hx_downglide()
    zixuanguxinwen_page.cell01.click()
    zixun_page.fanhui_btn.click()
    zixuanguxinwen_page.fanhui_btn.click()

def test_step89(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    zixuangugonggao_page=ZixuangugonggaoPage(driver)
    zixun_page = ZixunPage(driver)

    public_page.zixuan_button.click()

    optional_page.gonggao_btn.click()
    assert zixuangugonggao_page.zixuangugonggao_staText.text == u'自选股公告'
    #step 90-96
    zixuangugonggao_page.hx_upglide()
    zixuangugonggao_page.hx_downglide()
    zixuangugonggao_page.hx_downglide()
    zixuangugonggao_page.cell01.click()
    zixun_page.fanhui_btn.click()
    zixuangugonggao_page.fanhui_btn.click()

    #step 97-98
    #  上下滑
    for n in range(2):
        optional_page.hx_upglide()
    for n in range(2):
        optional_page.hx_glide()
    # step99-100
    # 左右滑
    for n in range(12):
        optional_page.hx_right()
    for n in range(13):
        optional_page.hx_left()
    # step101-103
    optional_page.zuixin_staText.click()
    optional_page.zuixin_staText.click()
    optional_page.quxiaopaixu_btn.click()

    #step 104
    for n in range(12):
        optional_page.hx_right()

    optional_page.zhenfu_staText.click()
    optional_page.zhenfu_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.weibi_staText.click()
    optional_page.weibi_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.zuidi_staText.click()
    optional_page.zuidi_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.zuigao_staText.click()
    optional_page.zuigao_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.zuoshou_staText.click()
    optional_page.zuoshou_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.kaipan_staText.click()
    optional_page.kaipan_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.xianshou_staText.click()
    optional_page.xianshou_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.shijinglv_staText.click()
    optional_page.shijinglv_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.shiyingdong_staText.click()
    optional_page.shiyingdong_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.liangbi_staText.click()
    optional_page.liangbi_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.huanshou_staText.click()
    optional_page.huanshou_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.zongshou_staText.click()
    optional_page.zongshou_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.zhangsu_staText.click()
    optional_page.zhangsu_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.zhangdie_staText.click()
    optional_page.zhangdie_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.zhangfu_staText.click()
    optional_page.zhangfu_staText.click()
    optional_page.quxiaopaixu_btn.click()

    optional_page.zuixin_staText.click()
    optional_page.zuixin_staText.click()
    optional_page.quxiaopaixu_btn.click()

    # step105
    optional_page.hx_glide()
    sleep(1)

    #step 106
    optional_page.cell001.click()
    sleep(1)
    # step107-109
    length = int(len(driver.find_elements_by_xpath("//UIATableView[1]/UIATableCell[@name]")))
    fenshikxian_page.change_gupiao(length)
    # step110-128
    fenshikxian_page.fanhui_button.click()

'''
#长按操作
def test_step114(driver):
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
'''
#自选股分组
def test_step130_144(driver):
    public_page = PublicPage(driver)
    optional_page = OptionalPage(driver)
    zixuangufenzu_page = ZixuangufenzuPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)

    public_page.zixuan_button.click()
    optional_page.fenzu_btn.click()

    # zixuangufenzu_page.xinjianfenzu_btn.click()
    # zixuangufenzu_page.guanbi_btn.click()
    # zixuangufenzu_page.guanlifenzu_btn.clcik()
    # zixuangufenzu_page.guanbi_btn.click()
    zixuangufenzu_page.chakanxiangqing_btn.click()
    sleep(1)
    zixuangufenzu_page.guanbi_btn.click()

    bankuainame = ['bankuai1', 'bankuai2','bankuai3','bankuai4','bankuai5','bankuai6','bankuai7','bankuai8']
    for name in bankuainame:
        eval('zixuangufenzu_page.{}_btn.click()'.format(name))
        lenth = len(driver.find_elements_by_xpath("//UIATableView[1]/UIATableCell[@name]"))
        optional_page.cell001.click()
        for n in range(lenth):
            fenshikxian_page.xiayigegupiao_button.click()
        fenshikxian_page.fanhui_button.click()
        optional_page.zx_right()
    zixuangufenzu_page.zixuangu_btn.click()
    optional_page.zx_right()
    optional_page.zx_left()
    optional_page.fenzu_btn.click()

    zixuangufenzu_page.hx_tapblank()



