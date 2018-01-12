#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import ddt
import logging
from lib.utils import capture_screen

test_data = [['', '123456', '登陆失败'],
             ['invalid', '123456', '登陆失败'],
             ['admin', '123456', '退出']]

@ddt.ddt
class Login(unittest.TestCase):
    """
    RanZhi 用户登陆
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/ranzhi/www/sys/admin/"
        driver = self.driver

    def tearDown(self):
        self.driver.quit()

    @ddt.unpack
    @ddt.data(*test_data)
    def test_user_login_test(self, admin, password, flag):
        """admin的登录的所有测试用例"""
        logging.info("test_admin_login_test start....")
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys(admin)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("submit").click()
        driver.find_element_by_id("submit").click()
        time.sleep(3)
        self.assertIn(flag, driver.page_source)
        logging.info("test data is : {}, {}, {}".format(admin, password, flag))
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.error("截图不成功")
        else:
            logging.info(pic_path)
        logging.info("test_user_login_test end....")

    if __name__ == '__main__':
        unittest.main()