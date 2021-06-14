import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
print(driver.current_url)

driver.find_element_by_name('q').send_keys('goo')
time.sleep(2)
driver.find_element_by_css_selector('input.gNO89b').click()
print(driver.title)
time.sleep(2)

driver.close()
