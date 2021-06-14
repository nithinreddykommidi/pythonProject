import selenium
from selenium import webdriver
import time

d = webdriver.Chrome()
d.get('https://accounts.lambdatest.com/login')

d.execute_script('window.open('fb.com')

d.close(