import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('http://testautomationpractice.blogspot.com/')
ele = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')
actions = ActionChains(driver)
actions.move_to_element(ele)
actions.double_click()
actions.perform()
time.sleep(2)
driver.close()
