# -*- coding: utf-8 -*-
from pages.hangqing.ahbijiagu_page import AHBijiaguPage
from pages.hangqing.ganggutong_page import GanggutongPage
from pages.public.debug_page import DebugPage
from pages.public.public_page import PublicPage
from pages.hangqing.hangqing_page import HangqingPage
from pages.hangqing.gangmeigu_page import GangmeiguPage
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.hangqing.gangmeigu_hangyebankuai_cell_page import HangyebankuaiPage
from pages.hangqing.hangqing_gengduo_page import HangqingGengduoPage
from pages.public.public_method import PublicMethod

from time import sleep

caseName = 'test_hangqing_gangmeigu'

# 港股通
def tst_step86(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    gangmeigu_page = GangmeiguPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    ganggutong_page = GanggutongPage(driver)
    public_method = PublicMethod(driver)
    debug_page = DebugPage(driver)

    public_page.hangqing_button.click()
    # step 3
    hangqing_page.gangmeigu_btn.click()
    gangmeigu_page.hk_btn.click()
    gangmeigu_page.hushengangtong.click()

    picName = '首页-行情-港美股-港股-沪深港通-港股通_86'
    public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
    assert ganggutong_page.hushenangtong_title
    assert ganggutong_page.shuaxin_btn

    ganggutong_page.ruhecanyu_btn.click()
    sleep(1)
    picName = '首页-行情-港美股-港股-沪深港通-港股通-如何参与_86'
    public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
    ganggutong_page.fanhui_btn.click()
    ganggutong_page.hushi_gengduo_click()
    sleep(2)
    picName = '首页-行情-港美股-港股-沪深港通-港股通-沪市更多_86'
    public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
    ganggutong_page.fanhui_btn.click()
    ganggutong_page.shenshi_gengduo_click()
    sleep(2)
    picName = '首页-行情-港美股-港股-沪深港通-港股通-深市更多_86'
    public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
    ganggutong_page.fanhui_btn.click()
    ganggutong_page.up_glide()
    ganggutong_page.down_glide()
    ganggutong_page.down_glide()
    ganggutong_page.ganggutong_operation_click()
    ganggutong_page.ganggutong_cell01_click()
    fenshikxian_page.change_gupiao(5)
    fenshikxian_page.fanhui_button.click()

    ggt_list = [('hugutong', '沪股通'), ('shengutong', '深股通')]
    for ggt, ggtname in ggt_list:
        eval('ganggutong_page.{}_tab.click()'.format(ggt))

        ganggutong_page.zijinliuru_btn.click()
        sleep(1)
        picName = '首页-行情-港美股-港股-沪深港通-{}-资金流入_86'.format(ggtname)
        public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
        ganggutong_page.fanhui_btn.click()
        ganggutong_page.shengyuedu_btn.click()
        sleep(1)
        picName = '首页-行情-港美股-港股-沪深港通-{}-剩余额度_87'.format(ggtname)
        public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
        ganggutong_page.fanhui_btn.click()
        ganggutong_page.zongedu_btn.click()
        sleep(1)
        picName = '首页-行情-港美股-港股-沪深港通-{}-今日总额度_88'.format(ggtname)
        public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
        ganggutong_page.fanhui_btn.click()
        ganggutong_page.up_glide()
        ganggutong_page.down_glide()
        ganggutong_page.down_glide()
        ganggutong_page.hushengutong_operation_click()
        ganggutong_page.hushengutong_cell01_click()
        fenshikxian_page.change_gupiao(5)
        fenshikxian_page.fanhui_button.click()
    ganggutong_page.fanhui_btn.click()

# 指数
def tst_step(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    gangmeigu_page = GangmeiguPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    public_method = PublicMethod(driver)
    debug_page = DebugPage(driver)

    public_page.hangqing_button.click()
    # step 3
    hangqing_page.gangmeigu_btn.click()

    market_list = ['us', 'hk']
    for market in market_list:
        # step 4-15：三个指数
        eval('gangmeigu_page.{}_btn.click()'.format(market))
        picName = '首页-行情-港美股-{}_3'.format(market)
        public_method.public_screenshot_as_file(caseName=caseName, picName=picName)
        for n in range(1, 4):
            if market == 'hk' and n == 3:
                pass
            else:
                eval('gangmeigu_page.{0}_cell1_{1}.click()'.format(market, n))
                fenshikxian_page.hx_left()
                fenshikxian_page.hx_right()
                fenshikxian_page.fanhui_button.click()

# 板块
def tst_step16(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    gangmeigu_page = GangmeiguPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangyebankuai_page = HangyebankuaiPage(driver)
    hangqinggengduo_page = HangqingGengduoPage(driver)
    public_method = PublicMethod(driver)
    debug_page = DebugPage(driver)

    public_page.hangqing_button.click()
    # step 3
    hangqing_page.gangmeigu_btn.click()

    picName = '行情-港美股_3'
    public_method.public_screenshot_as_file(caseName=caseName, picName=picName)

    gangmeigu_page.glide_up()
    gangmeigu_page.glide_down()
    gangmeigu_page.glide_down()

    market_list = ['us', 'hk']

    # 港股和美股的页面布局结构差不多,测试步骤一致,所以用循环实现,"k = 0"代表美股,"k = 1"代表港股
    for market in market_list:
        # step 16-48: 行业板块操作
        eval('gangmeigu_page.{}_btn.click()'.format(market))
        eval('gangmeigu_page.{0}_cell2_1.click()'.format(market))

        if market == u'us':
            picName_hybk_gongge = '首页-行情-港美股-美股-行业板块第1宫格_16'
            picName_hybk_gengduoshuju = '首页-行情-港美股-美股-板块宫格-查看更多数据_18'
            picName_hybk_gengduo = '首页-行情-港美股-美股-行业板块更多_39'
        else:
            picName_hybk_gongge = '首页-行情-港美股-港股-行业板块第1宫格_99'
            picName_hybk_gengduoshuju = '首页-行情-港美股-港股-板块宫格-查看更多数据_101'
            picName_hybk_gengduo = '首页-行情-港美股-港股-行业板块更多_113'
        public_method.public_screenshot_as_file(caseName=caseName, picName=picName_hybk_gongge)

        # 领涨股
        for n in range(3):
            hangyebankuai_page.hybk_up()
        sleep(1)
        hangyebankuai_page.gengduoshuju_btn.click()
        public_method.public_screenshot_as_file(caseName=caseName, picName=picName_hybk_gengduoshuju)

        hangqinggengduo_page.hybk_clickOperation()
        hangqinggengduo_page.hq_down()
        sleep(1)
        title = hangqinggengduo_page.cell01_title.text
        lenth = public_method.public_getlength()
        hangqinggengduo_page.cell01.click()
        assert fenshikxian_page.title_staText.text == title
        fenshikxian_page.change_gupiao(2)
        fenshikxian_page.fanhui_button.click()
        hangqinggengduo_page.fanhui_btn.click()

        # 领跌股
        hangyebankuai_page.lingdiegu_btn.click()
        for n in range(3):
            hangyebankuai_page.hybk_up()
        sleep(1)
        hangyebankuai_page.gengduoshuju_btn.click()
        hangqinggengduo_page.hybk_clickOperation()
        lenth = public_method.public_getlength()
        title = hangqinggengduo_page.cell01_title.text
        hangqinggengduo_page.cell01.click()
        assert fenshikxian_page.title_staText.text == title

        fenshikxian_page.change_gupiao(2)
        fenshikxian_page.fanhui_button.click()
        hangqinggengduo_page.fanhui_btn.click()

        for m in range(6):
            hangyebankuai_page.xiayigegupiao_button.click()
        for m in range(6):
            hangyebankuai_page.shangyigegupiao_button.click()
        hangyebankuai_page.fanhui_btn.click()

        for n in range(1, 7):
            eval('gangmeigu_page.{0}_cell2_{1}.click()'.format(market, n))
            hangyebankuai_page.fanhui_btn.click()

        # 进入行业板块更多
        eval('gangmeigu_page.{0}_gengduo_1.click()'.format(market))
        public_method.public_screenshot_as_file(caseName=caseName, picName=picName_hybk_gengduo)
        sleep(1)
        hangqinggengduo_page.zhangfu_btn.click()
        hangqinggengduo_page.zhangfu_btn.click()
        hangqinggengduo_page.cell01.click()
        for m in range(5):
            hangyebankuai_page.xiayigegupiao_button.click()
        for m in range(5):
            hangyebankuai_page.shangyigegupiao_button.click()
        hangyebankuai_page.fanhui_btn.click()
        hangqinggengduo_page.fanhui_btn.click()
        # 收缩行业板块
        eval('gangmeigu_page.{}_group_1.click()'.format(market))

        if market == u'us':
            market = 'hk'
        else:
            market = 'us'
        eval("gangmeigu_page.{0}_btn.click()".format(market))
        picName = '首页-行情-港美股-港美股-港股_77'
        public_method.public_screenshot_as_file(caseName=caseName, picName=picName)

# ah比价股
def test_step49(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    gangmeigu_page = GangmeiguPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    public_method = PublicMethod(driver)
    debug_page = DebugPage(driver)
    ahbijiagu_page = AHBijiaguPage(driver)

    # step2
    public_page.hangqing_button.click()
    # step 3
    hangqing_page.gangmeigu_btn.click()

    gangmeigu_page.hk_btn.click()
    sleep(0.5)
    title = gangmeigu_page.hk_cell1_title.text
    gangmeigu_page.hk_cell1_title.click()
    assert fenshikxian_page.title_staText.text == title
    fenshikxian_page.change_gupiao(10)
    fenshikxian_page.fanhui_button.click()
    gangmeigu_page.hk_gengduo_2.click()
    sleep(1)
    assert ahbijiagu_page.shuaxin_btn
    assert ahbijiagu_page.sousuo_btn
    assert ahbijiagu_page.wenben_text
    ahbijiagu_page.zuixin_btn.click()
    ahbijiagu_page.zuixin_btn.click()
    ahbijiagu_page.zhangfu_btn.click()
    ahbijiagu_page.zhangfu_btn.click()
    ahbijiagu_page.yijialv_btn.click()
    ahbijiagu_page.yijialv_btn.click()
    # ahbijiagu_page.xiaochuwenben_btn.click()
    ahbijiagu_page.hq_up()
    ahbijiagu_page.hq_down()
    ahbijiagu_page.hq_down()
    title = ahbijiagu_page.cell01_title.text
    ahbijiagu_page.cell01_btn.click()
    assert fenshikxian_page.title_staText.text == title
    lenth = public_method.public_getlength()
    fenshikxian_page.change_gupiao(5)
    fenshikxian_page.fanhui_button.click()
    ahbijiagu_page.fanhui_btn.click()
    gangmeigu_page.hk_group_2.click()
    public_page.shouye_button.click()

# 列表
def tst_step50(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    gangmeigu_page = GangmeiguPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangqinggengduo_page = HangqingGengduoPage(driver)
    public_method = PublicMethod(driver)
    debug_page = DebugPage(driver)

    # step2
    public_page.hangqing_button.click()
    # step 3
    hangqing_page.gangmeigu_btn.click()

    gangmeigu_page.glide_up()
    gangmeigu_page.glide_down()
    gangmeigu_page.glide_down()

    market_list = ['us', 'hk']
    us_group_list = [('us_group_2', 'us_gengduo_2'), ('us_group_3', 'us_gengduo_3'),
                     ('us_group_4', 'us_gengduo_4'), ('us_group_5', 'us_gengduo_5'), ('us_group_6', 'us_gengduo_6')]
    hk_group_list = [('hk_group_2', 'hk_gengduo_2'), ('hk_group_3', 'hk_gengduo_3'), ('hk_group_4', 'hk_gengduo_4')]

    # 港股和美股的页面布局结构差不多,测试步骤一致,所以用循环实现
    for market in market_list:
        eval('gangmeigu_page.{}_btn.click()'.format(market))
        group_list = us_group_list
        if market == u'us':
            picName_zu_gengduo = '首页-行情-港美股-美股-组更多_'
        else:
            picName_zu_gengduo = '首页-行情-港美股-港股-组更多_'
            group_list = hk_group_list

        # step49
        for group, gengduo in group_list:
            if group == u'hk_group_2':
                gangmeigu_page.hk_group_2.click()
            else:
                eval('gangmeigu_page.{0}_cell1_title.click()'.format(market))
                fenshikxian_page.change_gupiao(5)
                fenshikxian_page.fanhui_button.click()
                eval('gangmeigu_page.{}.click()'.format(gengduo))
                sleep(1)
                public_method.public_screenshot_as_file(caseName=caseName, picName=picName_zu_gengduo)
                hangqinggengduo_page.zuixin_btn.click()
                hangqinggengduo_page.zuixin_btn.click()
                hangqinggengduo_page.zhangfu_btn.click()
                hangqinggengduo_page.zhangfu_btn.click()
                try:
                    hangqinggengduo_page.zongshizhi_btn.click()
                    hangqinggengduo_page.zongshizhi_btn.click()
                except:
                    print "没有总市值列"
                hangqinggengduo_page.hq_up()
                hangqinggengduo_page. hq_down()
                hangqinggengduo_page.hq_down()
                title = hangqinggengduo_page.cell01_title.text
                hangqinggengduo_page.cell01.click()
                assert fenshikxian_page.title_staText.text == title
                fenshikxian_page.change_gupiao(5)
                fenshikxian_page.fanhui_button.click()
                hangqinggengduo_page.fanhui_btn.click()
                eval('gangmeigu_page.{}.click()'.format(group))

        # for group in group_list[:: -1]:
            # eval('gangmeigu_page.{}.click()'.format(group))
