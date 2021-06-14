import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.set_window_size(800, 800)
driver.get('https://www.google.com/')
time.sleep(2)
driver.execute_script('window.open("https://www.google.com/")')
time.sleep(2)
driver.execute_script('window.open("https://www.facebook.com/","_current")')
driver.close()
time.sleep(2)
driver.quit()
