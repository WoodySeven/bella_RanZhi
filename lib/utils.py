#!/usr/bin/env python
"""
小工具的函数库
"""
import os
import shutil
import time
import logging
import random

def copy_file(src, dest):
    """拷贝文件到指定目录， src拷贝到dest"""
    if not os.path.exists(src):
        raise OSError
    shutil.copyfile(src, dest)


def capture_screen(driver, file_name=None):
    """对浏览器内部截图
    如果成功，返回路径，如果不成功，返回None
    : Return True 截图成功
    """
    pic_path = "./screenshots/mypic_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")
    if file_name is None:
        driver.get_screenshot_as_file(pic_path)
    else:
        driver.get_screenshot_as_file(file_name)
        pic_path = file_name
    if os.path.exists(pic_path):
        return True
    else:
        logging.error("截图失败，请查看原因")
        return False

def capture_full_screen():
    """对全屏进行截图, Python3 需要查一下"""
    # import PIL
    pass


def get_random_customer_name():
    """生成随机的客户名称"""
    name = "customer_{}".format(random.randint(1000, 9999))
    return name


def get_random_product_name():
    """生成随机的产品名称"""
    name = "cus{}".format(random.randint(1000, 9999))
    return name

def get_random_money():
    """生成随机的金额"""
    name = random.randint(1000, 9999)
    return name


def get_random_string(k=8):
    """生成随机的字符串，并返回"""
    population = 'abcdefghjklqwertyuiomnbvcxz0123456789'
    rand_list = random.choices(population, k=k)
    print(rand_list)
    return ''.join(rand_list)


def get_random_phone():
    """生成随机手机号码，并返回138、150、139、132、170、180、186、189"""
    phone_prefix = random.choice([138, 150, 139, 132, 170, 180, 186, 189])
    population = '0123456789'
    phone_suffix = ''.join(random.choices(population, k=8))
    return "{}{}".format(phone_prefix, phone_suffix)


if __name__ == "__main__":
    # print(get_random_phone())
    print(get_random_money())