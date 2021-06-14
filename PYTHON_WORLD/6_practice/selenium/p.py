import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get('http://testautomationpractice.blogspot.com/')

ele = driver.find_element(By.ID, 'speed')
drp = Select(ele)
drp.select_by_visible_text('Slow')
time.sleep(4)
driver.close()

