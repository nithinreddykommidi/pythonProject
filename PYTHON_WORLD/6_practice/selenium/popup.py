from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'D:\PYTHON_WORLD\3_SELENIUM\alert_2.html')
driver.find_element_by_xpath('/html/body/button').click()
time.sleep(2)
#driver.switch_to_alert.accept()

driver.switch_to_alert().dismiss()
driver.close()