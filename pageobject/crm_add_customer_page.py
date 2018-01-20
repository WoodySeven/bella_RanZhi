#!/usr/bin/env python
from lib.common_logic import *


class CrmAddCustomerPage(object):
    """封装添加客户页面对象的管理"""

    def __init__(self, driver):
        # 打开新建客户的页面
        """
        0.登录然之
        1.打开所有应用，并且切换到客户管理页面
        2.点击新建客户按钮
        :param driver: 传入参数
        """
        self.driver = driver
        driver.get(ADMIN_PAGE)
        login_by_admin(driver)
        click_all_apps(driver)
        click_crm_btn(driver)

    def input_all_info(self):
        return add_customer(self.driver)