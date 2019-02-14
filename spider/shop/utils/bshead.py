# -*- coding:utf-8 -*-
__author__ = "zhou"
__date__ = "2018/12/19 16:05"

"""
web浏览器配置文件
走 有头  无头 浏览器
"""

from selenium import webdriver


def create_bs_driver(type="firefox", headless=False):
    """

    :param type:
    :param headless:  是否为无头浏览器 True  无  False 有
    :return:
    """
    if type == 'firefox':
        firefox_opt = webdriver.FirefoxOptions()
        firefox_opt.add_argument("--headless") if headless else ''
        driver = webdriver.Firefox(firefox_options=firefox_opt)
    elif type == 'chrome':
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_argument("--headless") if headless else ''
        driver = webdriver.Chrome(chrome_options=chrome_opt)
    else:
        pass
    return driver
