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

    # 长按某个元素
    # element:为需要长按的元素
    # time:长按的时间
    def public_longPress(self, element, time):
        location = element.location
        el_size = element.size

        x = el_size['width'] / 2.0 + location['x']
        y = el_size['height'] / 2.0 + location['y']

        return self.w.tap([(x, y)], duration=time)

    """
    功能:截屏,并自动放入相应的日期文件夹内

    """
    def public_screenshot_as_file(self):
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        path = GetProjectPath.getProjectPath() + '/result/' + date
        if os.path.isdir(path):
            pass
        else:
            os.makedirs(path)
        now = datetime.now()
        self.w.get_screenshot_as_file(path + '/{}.png'.format(now))