#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pages.fenshikxian.fenshikxian_wubaidang_page import QuanjingwubaidangPage
from time import sleep

from pages.hangqing.hangqing_gengduo_page import HangqingGengduoPage
from pages.public.denglu_page import DengluPage
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.shouye.home_page import HomePage
from pages.fenshikxian.fenshikxian_yujing_page import FenshikxianYujingPage
from pages.fenshikxian.fenshikxian_lungutang_page import FenshikxianLungutangPage
from pages.fenshikxian.fenshikxian_zhibiao_page import FenshikxianZhibiaoPage
from pages.fenshikxian.fenshikxian_hengping_page import FenshikxianHengpingPage
from pages.public.public_method import PublicMethod
from pages.zixuangu.zixun_page import ZixunPage
import random


case_name = 'test_fenshikxian_shuping'
args = ('BIDU', 'HK0001' )

# 分时-行情数据
def test_step1_7(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    public_method = PublicMethod(driver)
    wubaidang_page = QuanjingwubaidangPage(driver)
    fenshikxian_hengping_page = FenshikxianHengpingPage(driver)

    for arg in args:
        fenshikxian_page.searchtofenshi(arg)
        pic_name = '搜索-{}-分时_2'.format(arg)
        public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
        title = fenshikxian_page.title_staText.text

        # 进入行情数据
        try:
            fenshikxian_page.shuping_hqsj_click()
            pic_name = '搜索-分时-行情数据_3'
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
            fenshikxian_page.guanbi_btn.click()
        except:
            print arg, ", 这只股票没有行情数据"

        if fenshikxian_page.mingxi_btn:
            fenshikxian_page.mingxi_btn.click()
            pic_name = '搜索-分时-明细_5'
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
        else:
            print arg, ", 这只股票没有明细"

        if fenshikxian_page.chengjiao_btn:
            fenshikxian_page.chengjiao_btn.click()
            pic_name = '搜索-分时-成交_6'
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
        else:
            print arg, ", 这只股票没有成交"

        if fenshikxian_page.wudang_btn:
            fenshikxian_page.wudang_btn.click()
            pic_name = '搜索-分时-五档_7'
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
        elif fenshikxian_page.shidang_btn:
            print arg, ", 这只股票没有五档"
            fenshikxian_page.shidang_btn.click()
            pic_name = '搜索-分时-十档_7'
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
            if fenshikxian_page.quanjingwubaidang_btn:
                fenshikxian_page.quanjingwubaidang_btn.click()
                sleep(1)
                pic_name = '搜索-分时-500档_7'
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                assert wubaidang_page.wubaidang_title
                wubaidang_page.fanhui_btn.click()
            else:
                print arg, ", 这只股票没有五百档按钮"
        else:
            print arg, ", 这只股票没有十档按钮"
        fenshikxian_page.qiehuanmingxi()

        # 切换分时指标
        if fenshikxian_page.maimaiduilie_tab_btn:
            for i in range(7):
                fenshikxian_page.zhibiaoqiehuan_up_click()
                pic_name = '搜索-分时-量/大单/散户数量/净量/量比/高抛低吸/资金博弈_12'
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
            for i in range(7):
                fenshikxian_page.zhibiaoqiehuan_down_click()
                pic_name = '搜索-分时-量/资金博弈/高抛低吸/量比/净量/散户数量/大单_14'
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
        else:
            for i in range(5):
                fenshikxian_page.zhibiaoqiehuan_up_click()
                pic_name = '搜索-分时-量/资金博弈/量比/净量/大单_12'
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
            for i in range(5):
                fenshikxian_page.zhibiaoqiehuan_down_click()
                pic_name = '搜索-分时-量/大单/净量/量比/资金博弈_14'
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

        fenshikxian_page.fenshi_qiehengping_btn.click()
        sleep(1)
        pic_name = '搜索-分时-横屏_15'
        public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
        assert fenshikxian_hengping_page.title_staText.text == title
        fenshikxian_hengping_page.x_btn.click()
        fenshikxian_page.fanhui_button.click()

# 分时－底部功能按钮
def test_step25_33(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    home_page = HomePage(driver)
    fenshikxian_yujing_page = FenshikxianYujingPage(driver)
    fenshikxian_lungutang_page = FenshikxianLungutangPage(driver)
    public_method = PublicMethod(driver)
    denglu_page = DengluPage(driver)

    isShenhe = True  # 默认是审核状态下
    if home_page.xiaoxizhongxin_btn_feishen:     # 如果首页的消息中心是非审核状态下的，目前状态就是非审核状态
        isShenhe = False

    for arg in args:
        fenshikxian_page.searchtofenshi(arg)
        pic_name = '搜索-{}-分时_2'.format(arg)
        public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

        # 大盘(appium找不到其元素)

        # 预警
        if not isShenhe:
            if fenshikxian_page.yujing_btn:
                fenshikxian_page.yujing_btn.click()
                pic_name = '搜索-{}-分时-预警_3'.format(arg)
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                if fenshikxian_yujing_page.tishi_window:
                    fenshikxian_yujing_page.tishi_fanhui_btn.click()
                else:
                    fenshikxian_yujing_page.wodeyujing_btn.click()
                    pic_name = '搜索-分时-预警－我的预警_4'
                    public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                    sleep(1)
                    fenshikxian_yujing_page.tianjiayujing_btn.click()
                    fenshikxian_yujing_page.fanhui_button.click()
            else:
                print arg, ", 这只股票没有预警"

        # 下单
        if fenshikxian_page.xiadan_btn:
            fenshikxian_page.xiadan_btn.click()
            fenshikxian_page.quxiaojiaoyi_btn.click()
        else:
            print arg, ", 这只股票没有下单"

        # 论股堂
        if fenshikxian_page.lungu_btn:
            fenshikxian_page.lungu_btn.click()
            pic_name = '搜索-分时-论股_9'
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
            fenshikxian_lungutang_page.xuantie_btn.click()
            fenshikxian_lungutang_page.zuiretiezi_btn.click()
            fenshikxian_lungutang_page.xuantie_btn.click()
            fenshikxian_lungutang_page.zuixintiezi_btn.click()
            fenshikxian_lungutang_page.fanhui_button.click()
        else:
            print arg, ", 这只股票没有论股堂"

        # 港股-刷新
        if fenshikxian_page.shuaxin_btn:
            fenshikxian_page.shuaxin_btn.click()
        else:
            print arg, ", 这只股票没有刷新按钮"

        # 现货市场-开户
        if fenshikxian_page.kaihu_btn:
            fenshikxian_page.kaihu_btn.click()
            sleep(1)
            pic_name = '搜索-分时-开户_33-1'
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
            denglu_page.guanbi_btn.click()
        else:
            print arg, ", 这只股票没有开户按钮"

        # 天津贵金属-品种概述
        if fenshikxian_page.pinzhonggaishu_btn:
            fenshikxian_page.pinzhonggaishu_btn.click()
            sleep(1)
            pic_name = '搜索-分时-品种概述_33-3'
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
            denglu_page.guanbi_btn.click()
        else:
            print arg, ", 这只股票没有品种概述按钮"

# 分时-新闻／盘口等tab
def test_step86(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    public_method = PublicMethod(driver)
    zixun_page = ZixunPage(driver)
    hangqing_gengduo_page = HangqingGengduoPage(driver)

    for arg in args:
        fenshikxian_page.searchtofenshi(arg)
        pic_name = '搜索-{}-分时_2'.format(arg)
        public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
        gupiao_name = fenshikxian_page.title_staText.text
        print gupiao_name
        fenshikxian_page.hx_up()
        # 盘口
        if fenshikxian_page.pankou_tab_btn:
            fenshikxian_page.pankou_tab_btn.click()
            pic_name = '搜索-{}-分时-盘口_11'.format(arg)
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
            # (不能点击盘口-板块,会报错)
        else:
            print arg, "这只股票没有盘口tab"

        # L2账号：买卖队列
        if fenshikxian_page.maimaiduilie_tab_btn:
            fenshikxian_page.maimaiduilie_tab_btn.click()
            pic_name = '搜索-{}-分时-买卖队列_85'.format(arg)
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

        # 新闻
        if fenshikxian_page.xinwen_tab_btn:
            fenshikxian_page.xinwen_tab_btn.click()
            pic_name = '搜索-分时-新闻_4'
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
            if fenshikxian_page.zixun_cell01:
                title = fenshikxian_page.zixun_cell01_title.text
                fenshikxian_page.zixun_cell01.click()
                sleep(1)
                pic_name = '搜索-{}-分时-新闻-资讯详情1_5'.format(arg)
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                assert zixun_page.shezhi_btn
                assert zixun_page.shoucang_btn
                assert zixun_page.fenxiang_btn
                assert zixun_page.xiangqing_title.text == title
                zixun_page.fanhui_btn.click()

                fenshikxian_page.zixun_celln_click()
                zixun_page.fanhui_btn.click()

                fenshikxian_page.zixun_celllast_click()
                zixun_page.fanhui_btn.click()
            elif fenshikxian_page.hkus_zixun_cell01:
                fenshikxian_page.hkus_zixun_cell01.click()
                sleep(1)
                pic_name = '搜索-{}-分时-新闻-资讯详情_5'.format(arg)
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                assert zixun_page.shezhi_btn
                zixun_page.fanhui_btn.click()

                fenshikxian_page.hkus_zixun_celln_click()
                zixun_page.fanhui_btn.click()

                fenshikxian_page.hkus_zixun_celllast_click()
                zixun_page.fanhui_btn.click()
        else:
            print arg, "这只股票没有新闻tab"

        # 公告
        if fenshikxian_page.gonggao_tab_btn:
            fenshikxian_page.gonggao_tab_btn.click()
            pic_name = '搜索-{}-分时-公告_91'.format(arg)
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
            if fenshikxian_page.chakangonggao_cell01:
                fenshikxian_page.chakangonggao_cell01.click()
                sleep(2)
                pic_name = '搜索-{}-分时-公告-查看公告资讯详情1_15'.format(arg)
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                # 港美股没有收藏和分享
                assert zixun_page.shoucang_btn
                assert zixun_page.fenxiang_btn
                zixun_page.fanhui_btn.click()

            if fenshikxian_page.gonggao_cell01:
                title = fenshikxian_page.gonggao_cell01_title.text
                fenshikxian_page.gonggao_cell01.click()
                sleep(2)
                pic_name = '搜索-{}-分时-公告-资讯详情1_15'.format(arg)
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                assert zixun_page.shoucang_btn
                assert zixun_page.fenxiang_btn
                assert zixun_page.xiangqing_title.text == title
                zixun_page.fanhui_btn.click()
            elif fenshikxian_page.hkus_gonggao_cell01:
                fenshikxian_page.hkus_gonggao_cell01.click()
                sleep(1)
                pic_name = '搜索-分时-公告-资讯详情1_15'
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                zixun_page.fanhui_btn.click()
        else:
            print arg, "这只股票没有公告tab"


        # 简况（F10）
        if fenshikxian_page.jiankuang_tab_btn:
            fenshikxian_page.jiankuang_tab_btn.click()
            sleep(1)
            pic_name = '搜索-{}-分时-简况_94'.format(arg)
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

            # jiankuang_list = [("caiwu_cell01", "主要指标详细"), ("caiwu_cell02", "公司概念详细"), ("caiwu_cell03", "最新动态详情"),
                              # ("caiwu_cell04", "公司资料详细"), ("caiwu_cell05", "公司高管详细"), ("caiwu_cell06", "股本股东详细"),
                              # ("caiwu_cell07", "主力持仓"), ("caiwu_cell08", "分红融资详细"), ("caiwu_cell09", "行业对比"),
                              # ("caiwu_cell10", "机构评级详细")]

            if fenshikxian_page.hk_jiankuang_cell01:    # 港美股

                if (arg[0] == u"H" and arg[1] == u"K") or (arg[0] == u"h" and arg[1] == u"k"):
                    hk_jiankuang_list = ("hk_jiankuang_cell01", "hk_jiankuang_cell02", "hk_jiankuang_cell03",
                                         "hk_jiankuang_cell04")
                    for hk_jk_name in hk_jiankuang_list:
                        print "港股简况***********", hk_jk_name
                        eval("fenshikxian_page.{}.click()".format(hk_jk_name))
                        sleep(2)
                        pic_name = '搜索-{}-分时-简况-{}-更多_94'.format(arg, hk_jk_name)
                        public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                        zixun_page.jkxq_fanhui_btn.click()
                else:
                    us_jiankuang_list = ("us_jiankuang_cell01", "us_jiankuang_cell02", )
                    for us_jk_name in us_jiankuang_list:
                        print "美股简况***********", us_jk_name
                        eval("fenshikxian_page.{}.click()".format(us_jk_name))
                        sleep(2)
                        pic_name = '搜索-{}-分时-简况-{}-更多_94'.format(arg, us_jk_name)
                        public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                        zixun_page.jkxq_fanhui_btn.click()
            else:
                jiankuang_list = [("caiwu_cell01", "主要指标详细"), ("caiwu_cell02", "公司概念详细/评级总览"),
                                  ("caiwu_cell03", "最新动态详情/董事会成员"), ("caiwu_cell04", "公司资料详细/高管成员")]
                for jk_name, name in jiankuang_list:
                    if "fenshikxian_page.{}".format(jk_name):
                        print "沪深AB股、港美股（审核）简况***********", jk_name, name
                        eval("fenshikxian_page.{}.click()".format(jk_name))
                        sleep(2)
                        pic_name = '搜索-{}-分时-简况-{}-更多_27'.format(arg, name)
                        public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                        zixun_page.jkxq_fanhui_btn.click()
        else:
            print arg, "这只股票没有简况（F10）tab"
        if not fenshikxian_page.xiadan_btn:
            zixun_page.jkxq_fanhui_btn.click()
        # 诊股
        if fenshikxian_page.zhengu_tab_btn:
            fenshikxian_page.zhengu_tab_btn.click()
            pic_name = '搜索-{}-分时-诊股_96'.format(arg)
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
        else:
            print arg, "这只股票没有诊股tab"
        # 财务
        if fenshikxian_page.caiwu_tab_btn:
            fenshikxian_page.caiwu_tab_btn.click()
            pic_name = '搜索-{}-分时-财务_97'.format(arg)
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

            if fenshikxian_page.hkus_caiwu_cell01:
                hkus_caiwu_list = ["hkus_caiwu_cell01", "hkus_caiwu_cell02", "hkus_caiwu_cell03"]
                for hkus_cw_name in hkus_caiwu_list:
                    if "fenshikxian_page.{}".format(hkus_cw_name):
                        print "港美股财务***********", hkus_cw_name
                        eval("fenshikxian_page.{}.click()".format(hkus_cw_name))
                        pic_name = '搜索-{}-分时-财务_47'.format(arg)
                        public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                        zixun_page.fanhui_btn.click()
            else:
                caiwu_list = [("caiwu_cell01", "主要指标"), ("caiwu_cell02", "利润表"), ("caiwu_cell03", "资产负债表"),
                              ("caiwu_cell04", "现金流量表")]
                for caiwu_name, name in caiwu_list:
                    if "fenshikxian_page.{}".format(caiwu_name):
                        print "沪深AB股、港美股（审核）财务***********", caiwu_name
                        eval("fenshikxian_page.{}.click()".format(caiwu_name))
                        pic_name = '搜索-{}-分时-财务-{}详情_47'.format(arg, name)
                        public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                        zixun_page.fanhui_btn.click()
        else:
            print arg, "这只股票没有财务tab"
        # 研报
        if fenshikxian_page.yanbao_tab_btn:
            fenshikxian_page.yanbao_tab_btn.click()
            pic_name = '搜索-{}-分时-研报_55'.format(arg)
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
            if fenshikxian_page.zixun_cell01:
                title = fenshikxian_page.zixun_cell01_title
                fenshikxian_page.zixun_cell01.click()
                sleep(1)
                pic_name = '搜索-{}-分时-研报-资讯详情1_56'.format(arg)
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                assert zixun_page.shezhi_btn
                assert zixun_page.shoucang_btn
                assert zixun_page.fenxiang_btn
                assert zixun_page.xiangqing_title.text == title.text
                zixun_page.fanhui_btn.click()

                fenshikxian_page.zixun_celln_click()
                zixun_page.fanhui_btn.click()

                fenshikxian_page.zixun_celllast_click()
                zixun_page.fanhui_btn.click()
        else:
            print arg, "这只股票没有研报tab"

        # 板块：概念解析
        if fenshikxian_page.gainianjiexi_tab_btn:
            fenshikxian_page.gainianjiexi_tab_btn.click()
            pic_name = '搜索-{}-分时-概念解析_62'.format(arg)
            public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

        # 板块：涨幅榜、跌幅榜
        if fenshikxian_page.zhangfubang_tab_btn:
            tab_list = [('zhangfubang', '涨幅榜'), ('diefubang', '跌幅榜')]
            for tab, tab_name in tab_list:
                eval('fenshikxian_page.{}_tab_btn.click()'.format(tab))
                pic_name = '搜索-{}-分时-{}_63'.format(arg, tab_name)
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
                lenth = public_method.public_getlength()
                fenshikxian_page.gupaio_cell001_btn.click()
                fenshikxian_page.change_gupiao(lenth - 1)
                fenshikxian_page.fanhui_button.click()
                fenshikxian_page.gengduogupiao_btn.click()
                pic_name = '搜索-{}-分时-{}-更多_100'.format(arg, tab_name)
                public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

                hangqing_gengduo_page.jijin_clickOperation()
                hangqing_gengduo_page.hq_up()
                hangqing_gengduo_page.hq_down()
                hangqing_gengduo_page.hq_down()
                lenth = public_method.public_getlength()
                hangqing_gengduo_page.cell01.click()
                fenshikxian_page.change_gupiao(5)
                fenshikxian_page.fanhui_button.click()
                hangqing_gengduo_page.fanhui_btn.click()
        else:
            print arg, "这只股票不是板块"
        fenshikxian_page.fanhui_button.click()

# k线指标切换－日／周／月/分钟周期
def test_step34_47(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    fenshikxian_zhibiao_page = FenshikxianZhibiaoPage(driver)
    public_method = PublicMethod(driver)

    fenshikxian_page.searchtofenshi(args[0])

    fenshikxian_page.hx_left()
    pic_name = '搜索-{}-分时-k线_34'.format(args[0])
    public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

    fenshikxian_page.shezhi_btn.click()
    pic_name = '搜索-{}-分时-k线-设置_35'.format(args[0])
    public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)

    isplus = True   # 默认是大屏手机（6及以上）
    if fenshikxian_zhibiao_page.cell01_shanchu:
        isplus = False

    fenshikxian_zhibiao_page.tianjiazhibiao_btn.click()
    if fenshikxian_zhibiao_page.title.text == u'添加指标':
        # 添加指标
        cells = driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell')
        for cell in cells:
            cell.click()
        fenshikxian_zhibiao_page.fanhui_button.click()

    lenth = public_method.public_getlength()
    fenshikxian_zhibiao_page.guanbi_btn.click()
    # 日k
    fenshikxian_page.ri_btn.click()
    print "k线周期：日",
    for n in range(lenth):
        zhibiao_name = fenshikxian_page.zhibiao_name_btn.text
        print "第 {} 个指标：".format(n), zhibiao_name
        fenshikxian_page.kxian_action_operation()

    time_list = ['zhou_btn', 'yue_btn']
    cycle_1 = random.choice(time_list)
    # 周 月
    eval('fenshikxian_page.{}.click()'.format(cycle_1))
    print "k线周期：", cycle_1
    for n in range(lenth):
        zhibiao_name = fenshikxian_page.zhibiao_name_btn.text
        print "第 {} 个指标：".format(n), zhibiao_name
        fenshikxian_page.kxian_action_operation()

    # 分钟周期
    fenshikxian_page.fenzhon_btn.click()
    fenzhon_list = ['one_btn', 'five_btn', 'fifteen_btn', 'thirty_btn', 'sixty_btn']
    cycle_2 = random.choice(fenzhon_list)
    print "k线周期：{}".format(cycle_2)
    eval('fenshikxian_page.{}.click()'.format(cycle_2))
    fenshikxian_page.fenzhon_btn.click()
    for n in range(lenth):
        zhibiao_name = fenshikxian_page.zhibiao_name_btn.text
        print "第 {} 个指标：".format(n), zhibiao_name
        fenshikxian_page.kxian_action_operation()

    if isplus:
        print "切换成交额和成交量"
        fenshikxian_page.chengjiaoeliang_click()
        fenshikxian_page.kxian_action_operation()

# k线设置
def test_step48_63(driver):
    fenshikxian_page = FenshiKxianPage(driver)
    fenshikxian_zhibiao_page = FenshikxianZhibiaoPage(driver)
    public_method = PublicMethod(driver)
    fenshikxian_hengping_page = FenshikxianHengpingPage(driver)

    fenshikxian_page.searchtofenshi(args[0])

    fenshikxian_page.hx_left()
    gupiao_title = fenshikxian_page.title_staText.text
    fenshikxian_page.shezhi_btn.click()

    fenshikxian_zhibiao_page.tianjiazhibiao_btn.click()
    if fenshikxian_zhibiao_page.title.text == u'添加指标':
        # 添加指标
        cells = driver.find_elements_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell')
        for cell in cells:
            cell.click()
        fenshikxian_zhibiao_page.fanhui_button.click()

    # 选择除权
    fenshikxian_zhibiao_page.chuquan_btn.click()
    fenshikxian_zhibiao_page.guanbi_btn.click()

    fenshikxian_page.kxian_action_operation()

    # 选择前复权 关闭k线均线
    fenshikxian_page.shezhi_btn.click()
    fenshikxian_zhibiao_page.qianfuquan_btn.click()
    fenshikxian_zhibiao_page.kjunxian_switch.click()
    fenshikxian_zhibiao_page.guanbi_btn.click()
    fenshikxian_page.kxian_action_operation()

    # 关闭k线均线设置 打开缺口
    fenshikxian_page.shezhi_btn.click()
    fenshikxian_zhibiao_page.kjunxian_switch.click()
    fenshikxian_zhibiao_page.quekou_switch.click()
    fenshikxian_zhibiao_page.guanbi_btn.click()
    fenshikxian_page.kxian_action_operation()

    # 关闭缺口
    fenshikxian_page.shezhi_btn.click()
    fenshikxian_zhibiao_page.quekou_switch.click()
    fenshikxian_page.hx_left()

    # 信息页、设置页
    fenshikxian_zhibiao_page.kjunxian_shezhi_image.click()
    sleep(1)
    assert fenshikxian_zhibiao_page.title.text == u"K线均线"
    fenshikxian_zhibiao_page.fanhui_button.click()
    fenshikxian_zhibiao_page.quekou_xinxi_image.click()
    sleep(1)
    assert fenshikxian_zhibiao_page.title.text == u"跳空缺口"
    fenshikxian_zhibiao_page.fanhui_button.click()

    fenshikxian_zhibiao_page.chengbenxian_xinxi_image.click()
    sleep(1)
    assert fenshikxian_zhibiao_page.title.text == u"指标说明"
    fenshikxian_zhibiao_page.fanhui_button.click()

    if fenshikxian_zhibiao_page.cell01_shanchu:   # 如果第一个指标有删除按钮，表示这是小屏幕手机
        start_num = 1    # 指标操作的起始点
    else:    # 否则这是大屏幕手机
        start_num = 3
        fenshikxian_zhibiao_page.chengjiaoe_shezhi.click()
        assert fenshikxian_zhibiao_page.title.text == u"成交额"
        fenshikxian_zhibiao_page.fanhui_button.click()
        fenshikxian_zhibiao_page.chengjiaoliang_shezhi.click()
        assert fenshikxian_zhibiao_page.title.text == u"成交量"
        fenshikxian_zhibiao_page.fanhui_button.click()

    lenth = public_method.public_getlength()

    for i in range(start_num, lenth):
        zhibiao_name = driver.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[{}]/UIAStaticText[1]".format(start_num))
        print "删除指标：".format(i), zhibiao_name.text
        if zhibiao_name.text == u"MACD":
            driver.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[{}]/UIAButton[1]".format(start_num)).click()
            sleep(1)
            assert fenshikxian_zhibiao_page.title.text == zhibiao_name.text
            fenshikxian_zhibiao_page.fanhui_button.click()
            num = start_num
            start_num = num + 1
        else:
            driver.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[{}]/UIAButton[2]".format(start_num)).click()
            sleep(1)
            assert fenshikxian_zhibiao_page.title.text == zhibiao_name.text
            fenshikxian_zhibiao_page.fanhui_button.click()
            driver.find_element_by_xpath(
                "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[{}]/UIAButton[1]".format(start_num)).click()
            fenshikxian_zhibiao_page.shanchu_btn.click()

    # 点击切换横屏
    fenshikxian_zhibiao_page.guanbi_btn.click()
    fenshikxian_page.kLine_qiehengping_btn.click()
    sleep(1)
    pic_name = '搜索-k线-横屏_15'
    public_method.public_screenshot_as_file(caseName=case_name, picName=pic_name)
    assert fenshikxian_hengping_page.title_staText.text == gupiao_title
    fenshikxian_hengping_page.x_btn.click()

    # 点击收回/展开放大缩小等按钮
    if fenshikxian_page.shouqi_btn:
        fenshikxian_page.shouqi_btn.click()
        sleep(0.5)
        fenshikxian_page.zhankai_btn.click()
        sleep(0.5)
    else:
        fenshikxian_page.zhankai_btn.click()
        sleep(0.5)
        fenshikxian_page.shouqi_btn.click()
        sleep(0.5)

    fenshikxian_page.fanhui_button.click()
