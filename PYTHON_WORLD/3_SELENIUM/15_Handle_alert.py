from selenium import webdriver
from time import sleep

d = webdriver.Chrome()
d.maximize_window()
d.get(r'C:\Users\smellamput001\Documents\ON-LINE\3_SELENIUM/alert_2.html')
sleep(5)

d.find_element_by_xpath('/html/body/button').click()

alert = d.switch_to.alert

#  To get alert message
print(' \n\n ALERT TEXT :: ' , alert.text)
sleep(5)

## To accept alert
alert.accept()


#alert.dismiss()

# alert.accept()  – used to accept the Alert
# alert.dismiss() – used to cancel the Alert
# alert.send_keys(' sriram ') – used to enter a value in the Alert text box.

sleep(10)
d.close()

