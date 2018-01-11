#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import random
import ddt
import logging
from lib.utils import capture_screen

test_data = [['', '123456', '用户名不存在'],
             ['invalid', '123456', '用户名不存在'],
             ['admin', '123456', '退出']]

@ddt.ddt
class Crm(unittest.TestCase):
    """
    演示的是RanZhi新建客户、新建产品
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
        """admin的登录的所有测试用例,新建客户、新建产品"""
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
        ##新建客户
        driver.find_element_by_xpath("//*[@id=\"s-menu-allapps\"]/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id=\"s-applist-1\"]/a/img").click()
        time.sleep(3)
        driver.switch_to.frame('iframe-1')
        time.sleep(5)
        #driver.find_element_by_xpath('//*[@id="mainNavbar"]/div[2]/ul/li[4]/a').click()
        #data1 = driver.find_element_by_link_text("客户").text
        #print(data1)
        ##新增客户
        driver.find_element_by_link_text("客户").click()
        driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()
        driver.find_element_by_id("name").send_keys(random.randint(1000,9999))
        driver.find_element_by_id("contact").send_keys("bella")
        driver.find_element_by_id("phone").send_keys(random.randint(10000000000,99999999999))
        driver.find_element_by_id("email").send_keys("{}@qq.com".format(random.randint(1000,9999)))
        driver.find_element_by_id("qq").send_keys(random.randint(1000,9999))
        driver.find_element_by_id("type").click()
        driver.find_element_by_xpath('//*[@id="type"]/option[2]').click()
        time.sleep(5)
        driver.find_element_by_id("size").click()
        driver.find_element_by_xpath('//*[@id="size"]/option[2]').click()
        driver.find_element_by_id("level").click()
        driver.find_element_by_xpath('//*[@id="level"]/option[2]').click()
        driver.find_element_by_id('intension').send_keys("客户意向非常大")
        driver.find_element_by_id("submit").click()
        time.sleep(5)
        ##新增产品
        driver.find_element_by_link_text("产品").click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()
        driver.find_element_by_id("name").send_keys(random.randint(1000,9999))
        time.sleep(3)
        driver.find_element_by_id("code").send_keys("{0}{1}".format(random.choice('abcdefghjklqwertyuiomnbvcxz'),random.randint(1000,9999)))
        time.sleep(3)
        driver.find_element_by_id("line").click()
        time.sleep(3)
        driver.find_element_by_id("type").click()
        driver.find_element_by_xpath('//*[@id="type"]/option[2]').click()
        driver.find_element_by_id("status").click()
        driver.find_element_by_xpath('//*[@id="status"]/option[2]').click()
        driver.find_element_by_id('submit').click()
        time.sleep(3)
        ##新增订单
        driver.find_element_by_link_text("订单").click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()
        driver.find_element_by_xpath('//*[@id="customer_chosen"]/a').click()
        driver.find_element_by_xpath('//*[@id="customer_chosen"]/div/ul/li[3]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="product_chosen"]/ul').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="product_chosen"]/div/ul/li[3]').click()
        driver.find_element_by_id('plan').send_keys(random.randint(2123,6454))
        time.sleep(5)
        driver.find_element_by_id('submit').click()
        time.sleep(5)
        self.assertIn(flag, driver.page_source)
        logging.info("test data is : {}, {}, {}".format(admin, password, flag))
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.error("截图不成功")
        else:
            logging.info(pic_path)
        logging.info("test_admin_login_test end....")


if __name__ == '__main__':
    unittest.main()