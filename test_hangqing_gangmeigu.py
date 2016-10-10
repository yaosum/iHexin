# -*- coding: utf-8 -*-

from pages.public.public_page import PublicPage
from pages.hangqing.hangqing_page import HangqingPage
from pages.hangqing.gangmeigu_page import GangmeiguPage
from pages.fenshikxian.fenshiKxian_page import FenshiKxianPage
from pages.hangqing.gangmeigu_hangyebankuai_cell_page import HangyebankuaiPage
from pages.hangqing.hangqing_gengduo_page import HangqingGengduoPage

def test_step1(driver):
    public_page = PublicPage(driver)
    hangqing_page = HangqingPage(driver)
    gangmeigu_page = GangmeiguPage(driver)
    fenshikxian_page = FenshiKxianPage(driver)
    hangyebankuai_page = HangyebankuaiPage(driver)
    hangqinggengduo_page = HangqingGengduoPage(driver)

    # step2
    public_page.hangqing_button.click()

    #step 3
    hangqing_page.gangmeigu_btn.click()
    cell_list = ['cell1_1', 'cell1_2', 'cell1_3']
    hybk_list = ['cell2_1', 'cell2_2','cell2_3','cell2_4', 'cell2_5','cell2_6']
    usa_list = [('group_usa2', 'gengduo_usa2'), ('group_usa3', 'gengduo_usa3'), ('group_usa4', 'gengduo_usa4'), ('group_usa5', 'gengduo_usa5')]
    hk_group_list = [('group_hk2', 'gengduo_hk2'), ('group_hk3', 'gengduo_hk3')]
    gengduo_list = ['gengduo_usa1','gengduo_hk1']
    group_list = ['group_usa1','group_hk1']
    #step 4-15
    """
    for cell in cell_list:
        eval('gangmeigu_page.{}.click()'.format(cell))
        fenshikxian_page.hx_left()
        fenshikxian_page.hx_right()
        fenshikxian_page.fanhui_button.click()
    """

    #港股和美股的页面布局结构差不多,测试步骤一致,所以用循环实现,"k = 0"代表美股,"k = 1"代表港股
    for k in range(2):
        # step 16-48
        # 行业板块
        """
        for cell in hybk_list:
            eval('gangmeigu_page.{}.click()'.format(cell))
            hangyebankuai_page.hybk_up()
            hangyebankuai_page.gengduoshuju_btn.click()
            hangqinggengduo_page.hybk_clickOperation()
            fenshikxian_page.change_gupiao(2)
            fenshikxian_page.fanhui_button.click()
            hangqinggengduo_page.fanhui_btn.click()
            hangyebankuai_page.lingdiegu_btn.click()

            hangyebankuai_page.hybk_up()
            hangyebankuai_page.gengduoshuju_btn.click()
            hangqinggengduo_page.hybk_clickOperation()
            fenshikxian_page.change_gupiao(2)
            fenshikxian_page.fanhui_button.click()
            hangqinggengduo_page.fanhui_btn.click()
            for n in range(5):
                hangyebankuai_page.xiayigegupiao_button.click()
            for n in range(5):
                hangyebankuai_page.shangyigegupiao_button.click()
            hangyebankuai_page.fanhui_btn.click()

        #行业板块
        if k == 0 :
            hybk_gengduo = gengduo_list[0]
        if k == 1 :
            hybk_gengduo = gengduo_list[1]
        eval('gangmeigu_page.{}.click()'.format(hybk_gengduo))
        hangqinggengduo_page.zhangfu_btn.click()
        hangqinggengduo_page.zhangfu_btn.click()
        hangqinggengduo_page.cell01.click()
        for n in range(5):
            hangyebankuai_page.xiayigegupiao_button.click()
        for n in range(5):
            hangyebankuai_page.shangyigegupiao_button.click()
        hangyebankuai_page.fanhui_btn.click()
        hangqinggengduo_page.fanhui_btn.click()
        """
        if k == 0 :
            hybk_group = group_list[0]
        if k == 1 :
            hybk_group = group_list[1]
        eval('gangmeigu_page.{}.click()'.format(hybk_group))

        if k == 0:
            list = usa_list
        if k == 1:
            list = hk_group_list
        # step49
        for group,gengduo in list:
            gangmeigu_page.cell1.click()
            fenshikxian_page.change_gupiao(10)
            fenshikxian_page.fanhui_button.click()
            eval('gangmeigu_page.{}.click()'.format(gengduo))
            hangqinggengduo_page.zuixin_btn.click()
            hangqinggengduo_page.zuixin_btn.click()
            hangqinggengduo_page.zhangfu_btn.click()
            hangqinggengduo_page.zhangfu_btn.click()
            #hangqinggengduo_page.zongshizhi_btn.click()
            hangqinggengduo_page.hq_up()
            hangqinggengduo_page.hq_up()
            hangqinggengduo_page.hq_down()
            hangqinggengduo_page.hq_down()
            hangqinggengduo_page.cell01.click()
            fenshikxian_page.change_gupiao(5)
            fenshikxian_page.fanhui_button.click()
            hangqinggengduo_page.fanhui_btn.click()
            eval('gangmeigu_page.{}.click()'.format(group))





