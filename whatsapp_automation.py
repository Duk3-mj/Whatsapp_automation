from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print('Please Scan the QR Code and press enter')
input()
f1 = open('chat','w')
time.sleep(10)

driver.find_element_by_css_selector("._2UaNq._2ko65").click()  # to select unread chat
time.sleep(10)
try:
    sachin = driver.find_elements_by_css_selector("._12pGw.EopGb")
except NoSuchElementException:
    pass
for i in range(17,len(sachin)):
    f1.writelines(sachin[i].text) # write chat in text file
    f1.write('\n')
f1.close()
f2 = open('chat','r')
print(f2.read())
f2.close()
