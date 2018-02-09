#!/usr/bin/env python
import unittest
from lib.common_logic import *


class DisableActivation(unittest.TestCase):
    """
    测试禁用、激活成员页面
    """

    def setUp(self):
        """开始打开谷歌浏览器"""
        self.driver = get_driver()
        logging.info("打开浏览器成功")

    def tearDown(self):
        """关闭谷歌浏览器"""
        self.driver.quit()
        logging.info("关闭浏览器成功")

    def test_disable_activation(self):
        """禁用成员、激活成员测试用例
        执行步骤：
        1.打开管理页面，登录
        2.点击后台管理
        3.添加成员、点击部门、禁用激活成员
        4.判断结果 
        """
        logging.info("test_create_member start....")
        driver = self.driver
        driver.get(ADMIN_PAGE)
        login_by_admin(driver)
        click_backend_management(driver)
        click_member_btn(driver)
        click_division_btn(driver)
        member(driver)
        logging.info("test data is : {},{}".format('admin', '123456'))
        # 对浏览器截屏
        capture_screen(driver)
        # 用例要设置检查点
        self.assertIn('www/sys/user-admin-5.html', driver.current_url)
        logging.info("test_MemberConfiguration_test end....")


if __name__ == '__main__':
    unittest.main()