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
        ##现金记账,记收入
        driver.find_element_by_xpath("//*[@id=\"s-menu-allapps\"]/button").click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="s-applist-3"]/a').click()
        time.sleep(5)
        driver.switch_to.frame("iframe-3")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="mainNavbar"]/div[2]/ul/li[3]/a').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="menuActions"]/a[2]').click()
        driver.find_element_by_id('depositor').click()
        driver.find_element_by_xpath('//*[@id="depositor"]/option[2]').click()
        driver.find_element_by_id('category').click()
        driver.find_element_by_xpath('//*[@id="category"]/option[2]').click()
        driver.find_element_by_xpath('//*[@id="trader_chosen"]/a').click()
        driver.find_element_by_xpath('//*[@id="trader_chosen"]/div/ul/li[1]').click()
        time.sleep(2)
        #driver.find_element_by_id('contract').click()
        driver.find_element_by_id('money').send_keys(random.randint(3213,4455))
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="handlers_chosen"]/ul').click()
        driver.find_element_by_xpath('//*[@id="handlers_chosen"]/div/ul/li[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="product_chosen"]/a').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="product_chosen"]/div/ul/li[1]').click()
        time.sleep(5)
        driver.find_element_by_id('date').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[3]/table/thead/tr[1]/th[2]').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/table/thead/tr/th[1]/i').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/table/tbody/tr/td/span[5]').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[3]/table/tbody/tr[3]/td[4]').click()
        time.sleep(5)
        driver.find_element_by_id('desc').send_keys('白日依山尽，黄河入海流')
        time.sleep(2)
        #driver.find_element_by_name('files[]').click()
        driver.find_element_by_id('submit').click()
        ##记支出
        driver.find_element_by_xpath('//*[@id="mainNavbar"]/div[2]/ul/li[4]/a').click()
        driver.find_element_by_xpath('//*[@id="menuActions"]/a[2]').click()
        time.sleep(3)
        driver.find_element_by_id('depositor').click()
        driver.find_element_by_xpath('//*[@id="depositor"]/option[2]').click()
        driver.find_element_by_id('category').click()
        driver.find_element_by_xpath('//*[@id="category"]/option[2]').click()
        driver.find_element_by_id('objectType2').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="order_chosen"]/a').click()
        driver.find_element_by_xpath('//*[@id="order_chosen"]/div/ul/li[1]').click()
        time.sleep(2)
        driver.find_element_by_id('money').clear()
        driver.find_element_by_id('money').send_keys(random.randint(3211,5462))
        driver.find_element_by_xpath('//*[@id="handlers_chosen"]/ul').click()
        driver.find_element_by_xpath('//*[@id="handlers_chosen"]/div/ul/li[1]').click()
        driver.find_element_by_id('desc').click()
        driver.find_element_by_id('desc').send_keys('我们我们啊哈哈')
        driver.find_element_by_id('submit').click()

        time.sleep(5)

