#!/usr/bin/env python
from config import *
from selenium import webdriver


def get_driver():
    """获取driver对象"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    return driver


def login_by_admin(driver):
    """管理员登录"""
    driver.find_element_by_id("account").clear()
    driver.find_element_by_id("account").send_keys(ADMIN_ACCOUNT['account'])
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(ADMIN_ACCOUNT['password'])
    driver.find_element_by_id("submit").click()