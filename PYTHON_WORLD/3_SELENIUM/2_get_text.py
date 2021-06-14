from selenium import webdriver
import time

# Open Chrome Browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org")
time.sleep(4)

## Get text based on xpath
text = driver.find_element_by_xpath('//*[@id="downloads"]/a').text

print('\n Text is :', text)

assert text == 'Downloads1', ' TEXT IS NOT EXPECTED '

time.sleep(4)
driver.close()


