#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page_object.appium_page_objects import PageObject
from get_project_path import GetProjectPath
from datetime import datetime
import time
import os

class PublicMethod(PageObject):
    """
    该类放一些公共通用的方法,命名规则:public_***
    """
    run_case_id = "9999999"
    def __init__(self, webdriver, root_uri=None):
        #初始化,读取用例id
        PageObject.__init__(self, webdriver, root_uri=None)
        file_path = GetProjectPath.getProjectPath() + '/runConf.txt'
        if not os.path.isfile(file_path):
            file = open(file_path,'w')
            file.write('9999999')
            file.close()
            self.run_case_id = "9999999"
        else:
            file = open(file_path, 'r')
            msg = file.read()
            file.close()
            self.run_case_id = msg

    # 处理某些元素点击不了,按其坐标点击
    # element:需要点击的按钮元素
    def public_tap_element(self, element):
        """
        Custom method. Tap element by tapping it's coordiante
        :param element: Element instance. Should have location and size attribute
        :return:
        """
        location = element.location
        el_size = element.size
        return self.w.tap([(el_size['width'] / 2 + location['x'], el_size['height'] / 2 + location['y'],)])

    def public_longPress(self, element, time):
        """
        长按某个元素
        :param element: 为需要长按的元素
        :param time: 长按的时间
        :return:
        """
        location = element.location
        el_size = element.size

        x = el_size['width'] / 2.0 + location['x']
        y = el_size['height'] / 2.0 + location['y']

        return self.w.tap([(x, y)], duration=time)

    def public_screenshot_as_file(self, picName):
        """
        截屏,并自动放入相应的日期文件夹内
        截图目录层级结构:
        根目录-->result-->case运行的日期-->具体case的名字-->截图
        :param caseName: 具体的case名字
        :param picName:图片名字
        :return:
        """
        screen_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        screen_time = time.strftime('%H:%M:%S')
        path = GetProjectPath.getProjectPath() + '/result/' + screen_date + '/' + self.run_case_id
        print("runcaseid"+self.run_case_id)
        if os.path.isdir(path):
            pass
        else:
            os.makedirs(path)
        picName_ = screen_time + '_' + picName
        self.w.get_screenshot_as_file(path + '/{}.png'.format(picName_))

    def public_getlength(self):
        """
        当前页面是列表页面，获取当前页面列表长度
        :return:列表长度(int)
        """
        return int(len(self.w.find_elements_by_xpath("//UIATableView[1]/UIATableCell[@name]")))