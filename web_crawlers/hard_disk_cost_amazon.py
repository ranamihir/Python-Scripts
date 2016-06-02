# Checks price of WD Elements (1TB USB 3.0 Portable External Hard Drive (Black)) hard disk on Amazon.in

from selenium import webdriver

driver = webdriver.Chrome("C:/Python34/chromedriver.exe")
driver.get("http://goo.gl/0nxy4l")
try:
    element = driver.find_element_by_id('priceblock_ourprice')
except:
    element = driver.find_element_by_id('priceblock_saleprice')
print element.text.strip(' ')

driver.close()