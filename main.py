#!/usr/bin/env python
import os
import unittest
import logging
from lib.Logger import Logger
import traceback
from lib import HTMLTestRunner
import time
from testcase.common_module.login_logout import Login
from testcase.common_module.create_new_clients import CreateNewClients
from testcase.common_module.create_new_product import CreateNewProduct
from testcase.common_module.create_new_order import CreateNewOrder
from testcase.common_module.create_member import CreateMember
from testcase.common_module.disable_activation import DisableActivation
from testcase.common_module.cash_expenditure import CashExpenditure
from testcase.common_module.cash_income import CashIncome
from testcase.pageobject_demo.test_add_customer import CreateNewClients as PO


if __name__ == '__main__':
        logger = Logger('./log/logger.log', logging.INFO) 
        logging.info("本次测试开始执行，以下是详细日志")
        if not os.path.exists("reports/"):
            os.makedirs("reports")
        if not os.path.exists("screenshots/"):
            os.makedirs("screenshots")
        try:
            suite = unittest.TestSuite()  # 新建一个suite，测试套件
            loader = unittest.TestLoader()  # 新建一个加载器，自定义的方式把测试用例加载到suite里
            #suite.addTests(loader.loadTestsFromTestCase(Login))#把测试类登陆方法加载到suite里
            #suite.addTests(loader.loadTestsFromTestCase(CreateNewClients))#把测试类新增客户方法加载到suite里
            #suite.addTests(loader.loadTestsFromTestCase(CreateNewProduct))#把测试类新增产品方法加载到suite里
            #suite.addTests(loader.loadTestsFromTestCase(CreateNewOrder))#把测试类新增订单方法加载到suite里
            # suite.addTests(loader.loadTestsFromTestCase(CreateMember))#把测试类新加成员方法加载到suite里
            suite.addTests(loader.loadTestsFromTestCase(DisableActivation))# 把测试类禁用、激活成员方法加载到suite里
            # suite.addTests(loader.loadTestsFromTestCase(CashExpenditure))#把测试类现金记账支出方法加载到suite里
            # suite.addTests(loader.loadTestsFromTestCase(CashIncome))#把测试类现金记账收入方法加载到suite里
            # unittest.TextTestRunner(verbosity=2).run(suite) # unittest运行suite

            fp = open('reports/ranzhi{0}.html'.format(time.strftime("%Y-%m-%d %H-%M-%S")), 'wb')
            runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='ranzhi的测试报告',
                description='ranzhi的所有测试用例执行细节'
            )
            runner.run(suite)
            logging.info("测试顺利结束^_^ ")
        except Exception:
            """print_exc() 把异常输出到屏幕上，而format_exc() 把异常返回成字符串"""
            # traceback.print_exc()
            logging.error(traceback.format_exc())
            logging.error("测试异常终止")
        finally:
            # 发邮件、或者是发短信
            if fp is not None:
                fp.close()