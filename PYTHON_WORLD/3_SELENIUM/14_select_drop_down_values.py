from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

###  IF driver in current path ###
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r'C:\INSTITUTE_COURSES\INST\2_ONLINE_CLASS\3_SELENIUM/Drop_down.html')
time.sleep(5)

drop_element = driver.find_element_by_id('MONTHS')

months = Select(drop_element)
time.sleep(5)

## To select a value based on visable text
#months.select_by_visible_text('April')
#time.sleep(5)

## To select a value based on value
#months.select_by_value('Feb')
#time.sleep(5)

## To select a value based on index
months.select_by_index(4)

time.sleep(10)
driver.close()





