import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.google.co.in/')

driver.set_window_size(700, 700)


driver.execute_script('document.body.style.zoom="300%"')
time.sleep(2)
driver.execute_script('document.body.style.zoom="50%"')
time.sleep(2)
driver.execute_script('document.body.style.zoom="100%"')

driver.close()
