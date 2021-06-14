from selenium import webdriver


driver = webdriver.Chrome()
driver.get(r'D:\PYTHON_WORLD\3_SELENIUM\alert_2.html')
driver.execute_script("window.scrollTo(0, 200)")
driver.close()
