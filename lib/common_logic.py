#!/usr/bin/env python
"""小工具的函数"""
from config import *
from selenium import webdriver
import time
from lib.utils import *


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
    time.sleep(3)


def click_backend_management(driver):
    """点击后台管理"""
    driver.find_element_by_xpath('//*[@id="s-menu-superadmin"]/button').click()
    time.sleep(2)


def click_all_apps(driver):
    """点击所有应用"""
    driver.find_element_by_xpath("//*[@id=\"s-menu-allapps\"]/button").click()
    time.sleep(3)


def click_crm_btn(driver):
    """点击客户管理"""
    driver.find_element_by_xpath("//*[@id=\"s-applist-1\"]/a/img").click()
    time.sleep(3)


def click_member_btn(driver):
    """点击添加成员"""
    switch_to_frame(driver, 'iframe-superadmin')
    driver.find_element_by_xpath('//*[@id="shortcutBox"]/div/div[1]/div/a/h3').click()


def click_division_btn(driver):
    """选择研发部门"""
    driver.find_element_by_xpath('//*[@id="category5"]').click()


def member(driver):
    """禁用成员、激活成员"""
    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[2]').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[2]').click()
    time.sleep(3)


def click_cash_account_btn(driver):
    """点击现金记账"""
    driver.find_element_by_xpath('//*[@id="s-menu-3"]/button').click()
    time.sleep(3)


def switch_to_frame(driver, frame_name='iframe-1'):
    ##进入ifarme
    driver.switch_to.frame(frame_name)
    time.sleep(5)


def add_customer(driver):
    """新增客户"""
    name = get_random_customer_name()
    contact = get_random_string()
    phone = get_random_phone()
    email = "{}@qq.com".format(name)
    qq = phone
    logging.info("test data is : name {0},phone {1}, email {2}".format(name, phone, email))

    switch_to_frame(driver, 'iframe-1')
    driver.find_element_by_link_text("客户").click()
    driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()  ##点击添加客户
    driver.find_element_by_id("name").send_keys(name)  ##输入名称
    driver.find_element_by_id("contact").send_keys(contact)  ##输入联系人
    driver.find_element_by_id("phone").send_keys(phone)  ##输入电话
    driver.find_element_by_id("email").send_keys(email)  ##输入邮箱
    driver.find_element_by_id("qq").send_keys(qq)  ##输入qq
    driver.find_element_by_id("type").click()  ##选择类型
    driver.find_element_by_xpath('//*[@id="type"]/option[2]').click()
    time.sleep(3)
    driver.find_element_by_id("size").click()  ##选择规模
    driver.find_element_by_xpath('//*[@id="size"]/option[2]').click()
    driver.find_element_by_id("level").click()  ##选择级别
    driver.find_element_by_xpath('//*[@id="level"]/option[2]').click()
    driver.find_element_by_id('intension').send_keys("客户意向非常大")  ##购买意向输入
    driver.find_element_by_id("submit").click()  ##点击保存
    time.sleep(3)
    return {"name": name, "phone": phone}


def add_member(driver):
    """添加成员"""
    ##进入ifarme
    switch_to_frame(driver, 'iframe-superadmin')
    #点击添加成员按钮
    driver.find_element_by_xpath('//*[@id="shortcutBox"]/div/div[1]/div/a/h3').click()

    name = get_random_customer_name()
    email = "{}@qq.com".format(name)

    ##用户名
    driver.find_element_by_id('account').send_keys(name)
    ##真实姓名
    driver.find_element_by_id('realname').send_keys(name)
    driver.find_element_by_id('gender2').click()  ##选择性别
    driver.find_element_by_id('dept').click()  ##选择部门
    driver.find_element_by_xpath('//*[@id="dept"]/option[2]').click()
    driver.find_element_by_id('role').click()  ##选择角色
    driver.find_element_by_xpath('//*[@id="role"]/option[3]').click()
    driver.find_element_by_id('password1').send_keys('123456')  ##输入密码
    driver.find_element_by_id('password2').send_keys('123456')  ##再一次输入密码
    ##输入邮箱
    driver.find_element_by_id('email').send_keys(email)
    driver.find_element_by_id('submit').click()  ##点击保存
    time.sleep(6)
    return {"name": name, "email": email}


def add_expenditure(driver):
    """添加记支出"""
    money = get_random_money()
    #进入ifarme
    switch_to_frame(driver, 'iframe-3')
    #点击支出按钮
    driver.find_element_by_xpath('//*[@id="mainNavbar"]/div[2]/ul/li[4]/a').click()
    #点击记支出按钮
    driver.find_element_by_xpath('//*[@id="menuActions"]/a[2]').click()
    ##选择账号
    driver.find_element_by_id('depositor').click()
    driver.find_element_by_xpath('//*[@id="depositor"]/option[2]').click()
    ##选择科目
    driver.find_element_by_id('category').click()
    driver.find_element_by_xpath('//*[@id="category"]/option[2]').click()
    ##选择订单支出
    driver.find_element_by_id('objectType2').click()
    time.sleep(2)
    ##选择订单
    driver.find_element_by_xpath('//*[@id="order_chosen"]/a').click()
    driver.find_element_by_xpath('//*[@id="order_chosen"]/div/ul/li[1]').click()
    time.sleep(2)
    ##清空金额
    driver.find_element_by_id('money').clear()
    ##输入金额
    driver.find_element_by_id('money').send_keys(money)
    ##选择经手人
    driver.find_element_by_xpath('//*[@id="handlers_chosen"]/ul').click()
    driver.find_element_by_xpath('//*[@id="handlers_chosen"]/div/ul/li[1]').click()
    ##输入说明
    driver.find_element_by_id('desc').send_keys('我们我们啊哈哈')
    ##点击保存按钮
    driver.find_element_by_id('submit').click()
    time.sleep(3)
    return {"money": money}


def add_income(driver):
    """添加记收入"""
    money = get_random_money()
    ##进入ifarme
    switch_to_frame(driver, 'iframe-3')
    time.sleep(5)
    ##点击收入
    driver.find_element_by_xpath('//*[@id="mainNavbar"]/div[2]/ul/li[3]/a').click()
    time.sleep(5)
    ##点击记收入
    driver.find_element_by_xpath('//*[@id="menuActions"]/a[2]').click()
    driver.find_element_by_id('depositor').click()  ##选择账号
    driver.find_element_by_xpath('//*[@id="depositor"]/option[2]').click()
    driver.find_element_by_id('category').click()  ##选择科目
    driver.find_element_by_xpath('//*[@id="category"]/option[2]').click()  ##选择客户
    driver.find_element_by_xpath('//*[@id="trader_chosen"]/a').click()
    driver.find_element_by_xpath('//*[@id="trader_chosen"]/div/ul/li[1]').click()  ##选择合同
    time.sleep(2)
    driver.find_element_by_id('money').send_keys(money)  ##输入金额
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="handlers_chosen"]/ul').click()  ##选择经手人
    driver.find_element_by_xpath('//*[@id="handlers_chosen"]/div/ul/li[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="product_chosen"]/a').click()  ##选择产品
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="product_chosen"]/div/ul/li[1]').click()
    time.sleep(5)
    driver.find_element_by_id('date').click()  ##选择时间
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/table/thead/tr[1]/th[2]').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[4]/table/thead/tr/th[1]/i').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[4]/table/tbody/tr/td/span[5]').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/table/tbody/tr[3]/td[4]').click()
    time.sleep(5)
    driver.find_element_by_id('desc').send_keys('白日依山尽，黄河入海流')  ##输入说明
    time.sleep(2)
    driver.find_element_by_id('submit').click()  ##保存
    return {"money": money}

def add_order(driver):
    """新增订单"""
    money = get_random_money()
    ##进入iframe
    switch_to_frame(driver, 'iframe-1')
    time.sleep(5)
    ##新增订单
    driver.find_element_by_link_text("订单").click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()  ##创建订单
    driver.find_element_by_xpath('//*[@id="customer_chosen"]/a').click()  ##选择客户
    driver.find_element_by_xpath('//*[@id="customer_chosen"]/div/ul/li[3]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="product_chosen"]/ul').click()  ##选择产品
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="product_chosen"]/div/ul/li[3]').click()
    driver.find_element_by_id('plan').send_keys(money)  ##输入计划金额
    time.sleep(5)
    driver.find_element_by_id('submit').click()  ##点击保存
    time.sleep(5)
    return {"money": money}


def add_product(driver):
    """新增产品"""
    name = get_random_money()
    name1 = get_random_product_name()

    ##进入ifarme
    switch_to_frame(driver, 'iframe-1')
    time.sleep(5)
    ##新增产品
    driver.find_element_by_link_text("产品").click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()  ##点击新增产品
    driver.find_element_by_id("name").send_keys(name)  ##输入名称
    time.sleep(3)
    ##输入产品
    driver.find_element_by_id("code").send_keys(name1)
    time.sleep(3)
    driver.find_element_by_id("line").click()  ##选择产品线
    time.sleep(3)
    driver.find_element_by_id("type").click()  ##选择类型
    driver.find_element_by_xpath('//*[@id="type"]/option[2]').click()
    driver.find_element_by_id("status").click()  ##选择状态
    driver.find_element_by_xpath('//*[@id="status"]/option[2]').click()
    driver.find_element_by_id('submit').click()  ##点击保存
    time.sleep(3)