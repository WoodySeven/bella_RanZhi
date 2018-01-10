#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import random

class CashAccount(unittest.TestCase):
    """
    演示的是RanZhi的登录和退出
    数据驱动，相同的逻辑使用不同的数据去运行。
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/ranzhi/www/sys/admin/"
        driver = self.driver

    def tearDown(self):
        self.driver.quit()

    def test_admin_login_test(self):
        """admin的登录的所有测试用例"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_id("submit").click()
        time.sleep(3)
        ##现金记账
        driver.find_element_by_xpath("//*[@id=\"s-menu-allapps\"]/button").click()
        time.sleep(3)
        driver.find_element_by_link_text('//*[@id="s-applist-4"]/a').click()
        time.sleep(5)
