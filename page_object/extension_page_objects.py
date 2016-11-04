#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element


class ExtensionPageObject(PageObject):
	def id(self, a, b):
		a = page_element(accessibility_id='b')

