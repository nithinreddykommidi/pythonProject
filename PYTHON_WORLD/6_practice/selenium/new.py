from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.google.com/')
driver.execute_script('window.open("https://mail.google.com/mail/u/0/?ogbl#inbox")')
