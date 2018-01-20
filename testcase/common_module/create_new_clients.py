#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import random
import ddt
import logging
from lib.utils import capture_screen
from lib.common_logic import get_driver, login_by_admin
from config import *


class CreateNewClients(unittest.TestCase):
    """
    测试新增客户页面
    """
    def setUp(self):
        """开始打开谷歌浏览器"""
        self.driver = get_driver()
        logging.info("打开浏览器成功")

    def tearDown(self):
        """关闭谷歌浏览器"""
        self.driver.quit()
        logging.info("关闭浏览器成功")

    def test_create_new_clients(self):
        """新建客户测试用例"""
        logging.info("test_create_new_clients start....")
        driver = self.driver
        driver.get(ADMIN_PAGE)
        login_by_admin(driver)
        time.sleep(3)
        ##点击所有应用，点击客户管理
        driver.find_element_by_xpath("//*[@id=\"s-menu-allapps\"]/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id=\"s-applist-1\"]/a/img").click()
        time.sleep(3)
        ##进入ifarme
        driver.switch_to.frame('iframe-1')
        time.sleep(5)
        ##新增客户
        driver.find_element_by_link_text("客户").click()
        driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()##点击添加客户
        driver.find_element_by_id("name").send_keys(random.randint(1000,9999))##输入名称
        driver.find_element_by_id("contact").send_keys(random.choice('abcdefghjklqwertyuiomnbvcxz'))##输入联系人
        driver.find_element_by_id("phone").send_keys(random.randint(10000000000,99999999999))##输入电话
        driver.find_element_by_id("email").send_keys("{}@qq.com".format(random.randint(1000,9999)))##输入邮箱
        driver.find_element_by_id("qq").send_keys(random.randint(1000,9999))##输入qq
        driver.find_element_by_id("type").click()##选择类型
        driver.find_element_by_xpath('//*[@id="type"]/option[2]').click()
        time.sleep(5)
        driver.find_element_by_id("size").click()##选择规模
        driver.find_element_by_xpath('//*[@id="size"]/option[2]').click()
        driver.find_element_by_id("level").click()##选择级别
        driver.find_element_by_xpath('//*[@id="level"]/option[2]').click()
        driver.find_element_by_id('intension').send_keys("客户意向非常大")##购买意向输入
        driver.find_element_by_id("submit").click()##点击保存
        time.sleep(5)
        logging.info("test data is : {},{}".format('admin', '123456'))
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.error("截图不成功")
        else:
            logging.info(pic_path)
        logging.info("test_create_new_clients end....")

if __name__ == '__main__':
    unittest.main()