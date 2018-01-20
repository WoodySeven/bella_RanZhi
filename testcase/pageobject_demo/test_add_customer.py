#!/usr/bin/env python
import unittest
from lib.common_logic import *
from pageobject.crm_add_customer_page import CrmAddCustomerPage
from config import *


class CreateNewClients(unittest.TestCase):
    """
    测试新增客户页面, 使用Page Object的设计模式来编写用例
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
        """新建客户测试用例
        执行步骤：
        1.访问admin管理员页面，并登录
        2.点击所有应用，点击客户管理应用
        3.添加客户信息（自动生成客户信息）
        4.判断结果
        """
        page = CrmAddCustomerPage(self.driver)
        ret_val = page.input_all_info()
        self.assertIn(ret_val['name'], self.driver.page_source)
        self.assertIn('www/sys/user-admin.html', self.driver.current_url)
        logging.info("test_create_member end....")

if __name__ == '__main__':
    unittest.main()