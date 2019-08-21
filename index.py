# -*- coding: utf-8 -*-
__author__ = '任秀龙'

from selenium import webdriver
import time

chrome_driver = 'C:\chromeDriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_driver)
time.sleep(5)

url = "https://www.jianshu.com/p/111d5fd45487"
browser.get(url);
file = open('biaobai.json', 'w+', encoding="utf-8")
file.write(browser.page_source)

browser.quit();