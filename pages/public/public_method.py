#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page_object.appium_page_objects import PageObject

class Public_method(PageObject):

    def hx_tap_element(self, element):
        """
        Custom method. Tap element by tapping it's coordiante
        :param element: Element instance. Should have location and size attribute
        :return:
        """
        location = element.location
        el_size = element.size
        return self.w.tap([(el_size['width'] / 2 + location['x'], el_size['height'] / 2 + location['y'],)])