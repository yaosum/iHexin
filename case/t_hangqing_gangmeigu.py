# -*- coding: utf-8 -*-
from pages.hangqing.ganggutong_page import GanggutongPage
from pages.public.public_page import PublicPage
from pages.hangqing.hangqing_page import HangqingPage
from pages.hangqing.gangmeigu_page import GangmeiguPage
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.hangqing.gangmeigu_hangyebankuai_cell_page import HangyebankuaiPage
from pages.hangqing.hangqing_gengduo_page import HangqingGengduoPage

from time import sleep

def test_step16(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    gangmeigu_page = GangmeiguPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangyebankuai_page = HangyebankuaiPage(driver)
    hangqinggengduo_page = HangqingGengduoPage(driver)
    ganggutong_page = GanggutongPage(driver)

    # step2
    public_page.hangqing_button.click()
    #step 3
    hangqing_page.gangmeigu_btn.click()

    gangmeigu_page.glide_up()
    gangmeigu_page.glide_down()
    gangmeigu_page.glide_down()

    market_list = ['us', 'hk']
    us_group_list = [('us_group_2', 'us_gengduo_2'), ('us_group_3', 'us_gengduo_3'),
                     ('us_group_4', 'us_gengduo_4'), ('us_group_5', 'us_gengduo_5'), ('us_group_6', 'us_gengduo_6')]
    hk_group_list = [('hk_group_2', 'hk_gengduo_2'), ('hk_group_3', 'hk_gengduo_3')]

    #港股和美股的页面布局结构差不多,测试步骤一致,所以用循环实现
    for market in market_list:
        # step 4-15：三个指数和港股通
        for n in range(1, 4):
            eval('gangmeigu_page.{0}_cell1_{1}.click()'.format(market, n))
            if market == 'hk' and n == 3:
                assert ganggutong_page.ganggutong_title
                hangqinggengduo_page.ganggutong_clickOperation()
                ganggutong_page.cell01_click()
                fenshikxian_page.change_gupiao(10)
                fenshikxian_page.fanhui_button.click()
                ganggutong_page.fanhui_btn.click()
            else:
                fenshikxian_page.hx_left()
                fenshikxian_page.hx_right()
                fenshikxian_page.fanhui_button.click()

        # step 16-48: 行业板块操作
        eval('gangmeigu_page.{0}_cell2_1.click()'.format(market))
        hangyebankuai_page.hybk_up()
        hangyebankuai_page.hybk_up()
        hangyebankuai_page.hybk_up()
        sleep(1)
        hangyebankuai_page.gengduoshuju_btn.click()
        hangqinggengduo_page.hybk_clickOperation()
        title = hangqinggengduo_page.cell01_title.text
        length = int(len(driver.find_elements_by_xpath("//UIATableView[1]/UIATableCell[@name]")))
        hangqinggengduo_page.cell01.click()
        assert fenshikxian_page.title_staText.text == title
        fenshikxian_page.change_gupiao(2)
        fenshikxian_page.fanhui_button.click()
        hangqinggengduo_page.fanhui_btn.click()

        hangyebankuai_page.lingdiegu_btn.click()
        hangyebankuai_page.hybk_up()
        hangyebankuai_page.hybk_up()
        hangyebankuai_page.hybk_up()
        sleep(1)
        hangyebankuai_page.gengduoshuju_btn.click()
        hangqinggengduo_page.hybk_clickOperation()
        length = int(len(driver.find_elements_by_xpath("//UIATableView[1]/UIATableCell[@name]")))
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

        #进入行业板块更多
        eval('gangmeigu_page.{0}_gengduo_1.click()'.format(market))
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
        #收缩行业板块
        eval('gangmeigu_page.{}_group_1.click()'.format(market))

        group_list = us_group_list
        if market == 'hk':
            group_list = hk_group_list

        # step49
        for group, gengduo in group_list:
            sleep(1)
            eval('gangmeigu_page.{0}_cell1.click()'.format(market))
            fenshikxian_page.change_gupiao(10)
            fenshikxian_page.fanhui_button.click()
            eval('gangmeigu_page.{}.click()'.format(gengduo))
            hangqinggengduo_page.zuixin_btn.click()
            hangqinggengduo_page.zuixin_btn.click()
            hangqinggengduo_page.zhangfu_btn.click()
            hangqinggengduo_page.zhangfu_btn.click()
            ##hangqinggengduo_page.zongshizhi_btn.click()
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


        #for group in group_list[:: -1]:
            #eval('gangmeigu_page.{}.click()'.format(group))

        if market == 'us':
            market = 'hk'
        else:
            market = 'us'
        eval("gangmeigu_page.{0}_btn.click()".format(market))
    public_page.shouye_button.click()
