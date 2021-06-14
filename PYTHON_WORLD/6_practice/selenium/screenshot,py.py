from selenium import webdriver
driver = webdriver.Chrome()
driver.get(r'D:\PYTHON_WORLD\3_SELENIUM\alert_2.html')
driver.save_screenshot('scr.png')
