#!/usr/bin/env python
import unittest
from lib.common_logic import *


class CashIncome(unittest.TestCase):
    """
    测试现金记账收入页面
    """
    def setUp(self):
        """开始打开谷歌浏览器"""
        self.driver = get_driver()
        logging.info("打开浏览器成功")

    def tearDown(self):
        """关闭谷歌浏览器"""
        self.driver.quit()
        logging.info("关闭浏览器成功")

    def test_cash_income(self):
        """现金记账收入测试用例
        执行步骤：
        1.打开管理页面，登录
        2.点击现金记账
        3.添加记收入
        4.判断结果 
        """
        logging.info("test_cash_income start....")
        driver = self.driver
        driver.get(ADMIN_PAGE)
        login_by_admin(driver)
        click_cash_account_btn(driver)
        add_income(driver)
        logging.info("test data is : {},{}".format('admin', '123456'))
        # 对浏览器截屏
        capture_screen(driver)
        # 用例要设置检查点
        self.assertIn('www/cash/trade-browse-in.html', driver.current_url)
        logging.info("test_cash_income end....")

if __name__ == '__main__':
    unittest.main()