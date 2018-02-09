#!/usr/bin/env python
import unittest
from lib.common_logic import *



class CreateNewProduct(unittest.TestCase):
    """
    测试新增产品页面
    """
    def setUp(self):
        """开始打开谷歌浏览器"""
        self.driver = get_driver()
        logging.info("打开浏览器成功")

    def tearDown(self):
        """关闭谷歌浏览器"""
        self.driver.quit()
        logging.info("关闭浏览器成功")

    def test_create_new_products(self):
        """新建产品测试用例
            执行步骤：
        1.打开管理页面，登录
        2.点击所有应用管理、产品
        3.添加新产品
        4.判断结果
        """
        logging.info("test_create_new_products start....")
        driver = self.driver
        driver.get(ADMIN_PAGE)
        login_by_admin(driver)
        click_all_apps(driver)
        click_crm_btn(driver)
        add_product(driver)
        logging.info("test data is : {},{}".format('admin', '123456'))
        # 对浏览器截屏
        capture_screen(driver)
        # 用例要设置检查点
        self.assertIn('www/crm/product-browse.html', driver.current_url)
        logging.info("test_create_new_products end....")

if __name__ == '__main__':
    unittest.main()
