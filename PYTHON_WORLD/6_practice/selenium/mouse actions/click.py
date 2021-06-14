from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('http://testautomationpractice.blogspot.com/')
ele = driver.find_element_by_name('speed')
drp = Select(ele)
drp.select_by_visible_text('Fast')
