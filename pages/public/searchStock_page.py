#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException

from page_object.appium_page_objects import PageObject, page_element


class SearchStockPage(PageObject):
	zixuanadd_button = page_element(xpath='//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]')
	qingchuwenben_button = page_element(accessibility_id = "清除文本")

	Keyboard_Digits_Indicator = page_element(accessibility_id = "字母键盘_numAltButton")
	Keyboard_Letter_Indicator = page_element(accessibility_id = "数字键盘_altButton")
	Search_Stock_Keyboard_Tuple = (Keyboard_Digits_Indicator, Keyboard_Letter_Indicator,)


	def hx_tap_element(self, element):
		"""
		Custom method. Tap element by tapping it's coordiante
		:param element: Element instance. Should have location and size attribute
		:return:
		"""
		location = element.location
		el_size = element.size
		return self.w.tap([(el_size['width'] / 2 + location['x'], el_size['height'] / 2 + location['y'],)])


	def hx_tap_element_name(self, name):
		"""
		Custom method. Tap element by it's name
		:param name: Element instance. Should have location and size attribute
		:return:
		"""
		el = self.w.find_element_by_name(name=name)
		# el = self.find_element_by_accessibility_id(name=name)
		return self.hx_tap_element(el)


	def hx_tap_element_name_sequence(self, sequence):
		"""
		Custom method. Tap elements by it's name
		:param sequence: A sequence of elements for a keyboard.
		:return:
		"""
		return [self.hx_tap_element_name(name=name) for name in sequence]


	@staticmethod
	def hx_util_is_number(args):
		is_number = False
		number_str = ''.join([str(arg) for arg in args])

		try:
			int(number_str)
			is_number = True
		except ValueError, e:
			pass
		return is_number


	@staticmethod
	def hx_util_taken_same_type_args(args):
		"""
			获取同种类型的连续输入序列   如: 1234adfa 分割为1345 adfa
		:param self:
		:param args:
		:return:
		"""
		is_number = False
		taken_args = None
		remain_args = None

		i = 0
		for arg in args:
			now_is_number = SearchStockPage.hx_util_is_number(arg)
			if i > 0 and not now_is_number == is_number:
				taken_args = args[:i]
				remain_args = args[i:]
				break
			else:
				is_number = now_is_number
				if i == len(args) - 1:
					taken_args = args
					remain_args = []
			i += 1

		return is_number, taken_args, remain_args


	def hx_send_keys(self, *args):
		"""
		Custom method. Keyboard input numbers or English
		eg: self.driver.hx_send_keys('j', 'p', 'y', '1', '0', '1')
		:param args: A sequence of elements for a keyboard.
		:return:
		"""
		remain_args = None
		if len(args) == 1:
			remain_args = args[0]
		else:
			remain_args = args
		while remain_args:
			is_number, taken_args, remain_args = SearchStockPage.hx_util_taken_same_type_args(remain_args)

			element = None
			is_number_keyboard = False
			while True:
				try:
					# 数字键盘
					element = self.Keyboard_Digits_Indicator
					is_number_keyboard = element.is_displayed()
					break
				except NoSuchElementException:
					pass
				try:
					# 字母键盘
					element = self.Keyboard_Letter_Indicator
					is_number_keyboard = not element.is_displayed()
				except NoSuchElementException:
					pass

			if is_number and is_number_keyboard:
				self.hx_tap_element_name_sequence(taken_args)
			if is_number and not is_number_keyboard:
				self.hx_tap_element(element)
				self.hx_tap_element_name_sequence(taken_args)
			if not is_number and not is_number_keyboard:
				self.hx_tap_element_name_sequence(taken_args)
			if not is_number and is_number_keyboard:
				self.hx_tap_element(element)
				self.hx_tap_element_name_sequence(taken_args)

	def hx_send_keys_with_addStock(self, *args):
		self.hx_send_keys(*args)
		try:
			self.zixuanadd_button.click()
		except:
			print '该股票已添加过'
			pass
		self.qingchuwenben_button.click()

	def hx_addStock(self, stockName):
		self.stockName.click()






