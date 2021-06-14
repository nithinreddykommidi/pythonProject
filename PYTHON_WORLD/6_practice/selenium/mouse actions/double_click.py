import time

from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.set_window_size(700, 700)
driver.get('http://testautomationpractice.blogspot.com/')
ele = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')
action = ActionChains(driver)
action.move_to_element(ele)
action.double_click()
action.perform()
time.sleep(2)
txt = driver.find_element_by_id('field2').text
assert txt == "Hello World!", 'not same'
