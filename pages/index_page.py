#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page_object.appium_page_objects import PageObject, page_element


class IndexPage(PageObject):

    first_arg_textfield = page_element(accessibility_id = "IntegerA")
    second_arg_textfield = page_element(accessibility_id = "IntegerB")
    sum_button = page_element(xpath = "//UIAApplication[1]/UIAWindow[2]/UIAButton[1]")
    sum_result_label = page_element(accessibility_id = "Answer")


    def caculate_sum(self, a, b):
        self.first_arg_textfield = a
        self.second_arg_textfield = b
        self.sum_button.click()

    first_arg_textfield = "First_arg_textfield"


