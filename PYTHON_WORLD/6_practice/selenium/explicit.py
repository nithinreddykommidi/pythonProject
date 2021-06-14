from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.find_element(By.NAME, 'q').send_keys('nithin reddy kommidi')
wait = WebDriverWait(driver, 10)
wait.until(ec.element_to_be_clickable((By.NAME, 'btnK'))).click()
