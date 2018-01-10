#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import random


class MemberConfiguration(unittest.TestCase):
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
        ##添加成员信息
        driver.find_element_by_xpath('//*[@id="s-menu-superadmin"]/button').click()
        time.sleep(3)
        driver.switch_to.frame('iframe-superadmin')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="shortcutBox"]/div/div[1]/div/a/h3').click()
        driver.find_element_by_id('account').send_keys("{0}{1}".format(random.choice('abcdefghjklqwertyuiomnbvcxz'),random.randint(1000,9999)))
        driver.find_element_by_id('realname').send_keys(random.choice('abcdefghjklqwertyuiomnbvcxz'))
        driver.find_element_by_id('gender2').click()
        driver.find_element_by_id('dept').click()
        driver.find_element_by_xpath('//*[@id="dept"]/option[2]').click()
        driver.find_element_by_id('role').click()
        driver.find_element_by_xpath('//*[@id="role"]/option[3]').click()
        driver.find_element_by_id('password1').send_keys('123456')
        driver.find_element_by_id('password2').send_keys('123456')
        driver.find_element_by_id('email').send_keys("{}@qq.com".format(random.randint(1000,9999)))
        driver.find_element_by_id('submit').click()
        time.sleep(6)
        ##删除成员信息
        # driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[11]/a[3]').click()
        # time.sleep(2)
        # alert = self.driver.switch_to.alert
        # alert.accept()
        # time.sleep(3)
        ###禁用成员
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[2]').click()
        time.sleep(2)
        ###激活成员
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[2]').click()
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()