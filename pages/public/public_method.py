#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page_object.appium_page_objects import PageObject

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