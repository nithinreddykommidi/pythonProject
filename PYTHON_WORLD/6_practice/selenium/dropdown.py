import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
d = webdriver.Chrome()
d.get('http://testautomationpractice.blogspot.com/')
ele = d.find_element_by_id('files')
drp = Select(ele)
drp.select_by_value("4")
time.sleep(2)
