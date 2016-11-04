#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element
from time import sleep

class DengluPage(PageObject):
    """
    登录页面的相关元素及操作
    """
    guanbi_btn = page_element(accessibility_id = '关闭')
    username_text = page_element(accessibility_id = "登录账号")
    password_text = page_element(accessibility_id = "密码")
    denglu_btn = page_element(xpath = "//UIAApplication[1]/UIAWindow[1]/UIAButton[4]")
    expend_btn = page_element(accessibility_id = "login expand")

    def sign_in(self, username, password):
        """
        在登录页面登录
        :param username: 登录用户名
        :param password: 登录密码
        :return:
        """
        if self.expend_btn:
            self.username_text.clear()
        try:
            self.username_text.send_keys(username)
            self.password_text.send_keys(password)
            self.denglu_btn.click()
            sleep(1)
        except:
            print '登录失败'
