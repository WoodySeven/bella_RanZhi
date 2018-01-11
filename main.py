#!/usr/bin/env python
import unittest
import logging
from lib.Logger import Logger
import traceback
from lib import HTMLTestRunner
import time
from testcase.common_module.crm import Crm
from testcase.common_module.accounting import CashAccount

if __name__ == '__main__':
        logger = Logger('./log/logger.log', logging.INFO)
        logging.info("本次测试开始执行，以下是详细日志")
        try:
            suite = unittest.TestSuite()  # 新建一个suite，测试套件
            loader = unittest.TestLoader()  # 新建一个加载器，自定义的方式把测试用例加载到suite里
            suite.addTests(loader.loadTestsFromTestCase(Crm))# 把测试类所有的方法都加载到suite里
            suite.addTests(loader.loadTestsFromTestCase(CashAccount))
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
            traceback.print_exc()
            logging.error(traceback.format_exc())
            logging.error("测试异常终止")
        finally:
            if fp is not None:
                fp.close()