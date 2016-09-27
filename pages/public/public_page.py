#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element


class PublicPage(PageObject):
	shouye_button = page_element(accessibility_id = "首页")
	zixuan_button = page_element(accessibility_id = "自选")
	hangqing_button = page_element(accessibility_id = '行情')
