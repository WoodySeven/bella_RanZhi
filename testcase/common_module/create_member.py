#!/usr/bin/env python
import unittest
from lib.common_logic import *

class CreateMember(unittest.TestCase):
    """
    测试新增成员页面
    """

    def setUp(self):
        """开始打开谷歌浏览器"""
        self.driver = get_driver()
        logging.info("打开浏览器成功")

    def tearDown(self):
        """关闭谷歌浏览器"""
        self.driver.quit()
        logging.info("关闭浏览器成功")

    def test_create_member(self):
        """添加成员测试用例
        执行步骤：
        1.打开管理页面，登录
        2.点击后台管理
        3.添加成员
        4.判断结果
        """
        logging.info("test_create_member start....")
        driver = self.driver
        driver.get(ADMIN_PAGE)
        login_by_admin(driver)
        click_backend_management(driver)
        ret_val = add_member(driver)
        logging.info("test data is : {},{}".format('admin', '123456'))
        capture_screen(driver)
        self.assertIn(ret_val['name'], driver.page_source)
        self.assertIn('www/sys/user-admin.html', driver.current_url)
        logging.info("test_create_member end....")


if __name__ == '__main__':
    unittest.main()
