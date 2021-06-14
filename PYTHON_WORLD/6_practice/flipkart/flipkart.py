import selenium
from selenium import webdriver
import time


d = webdriver.Chrome()

d.get("https://www.flipkart.com/")
d.maximize_window()

phn = d.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input')
phn.send_keys('8686290707')

pas = d.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input')
pas.send_keys('maheshnit@5')

log = d.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button')
log.click()
time.sleep(2)


d.find_element_by_name('q').send_keys('realme narzo 3oa')
search = d.find_element_by_class_name('_34RNph')
search.click()
time.sleep(5)
item = find_element_by_xpath("//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/section[4]/div[2]/div/div[3]/div/label/div[1]").click()
