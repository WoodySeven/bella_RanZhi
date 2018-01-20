#!/usr/bin/env python
import unittest
from lib.common_logic import *
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
        """新建客户测试用例
        执行步骤：
        1.访问admin管理员页面，并登录
        2.点击所有应用，点击客户管理应用
        3.添加客户信息（自动生成客户信息）
        4.判断结果
        """
        logging.info("test_create_new_clients start....")
        driver = self.driver
        driver.get(ADMIN_PAGE)
        login_by_admin(driver)
        click_all_apps(driver)
        click_crm_btn(driver)
        ret_val = add_customer(driver)
        capture_screen(driver)
        # 用例要设置检查点
        self.assertIn(ret_val['name'], driver.page_source)
        self.assertIn('www/crm/customer-browse.html', driver.current_url)

if __name__ == '__main__':
    unittest.main()