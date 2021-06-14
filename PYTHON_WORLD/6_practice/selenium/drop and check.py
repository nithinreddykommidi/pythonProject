import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('D:/PYTHON_WORLD/3_SELENIUM/Drop_down.html')
driver.find_element_by_id('age2').click()
time.sleep(2)
driver.find_element_by_id('age3').click()
driver.find_element_by_id('vehicle1').click()
time.sleep(2)
driver.find_element_by_id('vehicle2').click()
driver.close()
