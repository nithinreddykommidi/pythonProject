from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://the-internet.herokuapp.com/upload')
time.sleep(2)
driver.find_element_by_name('file').send_keys(r'D:\PYTHON_WORLD\3_SELENIUM\RRR.png')
driver.find_element_by_id('file-submit').click()

