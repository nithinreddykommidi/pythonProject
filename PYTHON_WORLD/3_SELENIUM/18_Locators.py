from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com/')
time.sleep(5)

tit = driver.title
print(tit)

#e = driver.find_element_by_link_text('Gmail')
#print('\n\n LINK TEXT : ', e.text)

#elem = driver.find_element_by_partial_link_text("Gma")
#print('\n\n Partial LINK TEXT : ', elem.text)

#el2 = driver.find_element_by_tag_name('a')
#print('\n\n  TAG : ', el2.text)

#e = driver.find_element_by_class_name('gb_g')
#print('\n\n CLASS : ',e.text)

#e = driver.find_element_by_css_selector('.gb_g')
#print('\n\n  CSS : ',e.text)

time.sleep(3)
driver.close()


