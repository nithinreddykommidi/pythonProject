from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(20)

driver.get("http://selenium-python.readthedocs.io")


driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul/li[5]/aaa').click()

driver.close()

