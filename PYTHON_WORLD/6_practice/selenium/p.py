import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get('http://www.demo.guru99.com/V4/')
driver.find_element_by_name('uid').send_keys('mngr334114')
driver.find_element_by_name('password').send_keys('ugArEty')
driver.find_element_by_name('btnLogin').click()

time.sleep(10)