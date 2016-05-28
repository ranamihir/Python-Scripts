# Checks price of an item on Amazon.in

from selenium import webdriver
import smtplib

url = "http://goo.gl/0nxy4l"
threshold_value = 4000

driver = webdriver.Chrome("C:/Python34/chromedriver.exe")
driver.get(url)
name = driver.find_element_by_id('productTitle').text
try:
    price = driver.find_element_by_id('priceblock_ourprice').text.strip(' ').replace(',', '')
except:
    price = driver.find_element_by_id('priceblock_saleprice').text.strip(' ').replace(',', '')

print 'Price of ' + name + ' is: Rs.' + price
driver.close()

if int(price[:price.index('.')]) <= threshold_value:
        # Send mail
        sender_address = 'abc@gmail.com'
        receiver_address = 'xyz@gmail.com'
        message = 'The price for ' + name + ' -- Rs.' + price + ' is below your threshold value of Rs.' + str(threshold_value) + '.'

        # Credentials
        username = 'abc@gmail.com'
        password = '<password>'

        # The actual mail send
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(username, password)
            server.sendmail(sender_address, receiver_address, message)
            server.quit()
            print "Message sent successfully."
        except Exception as e:
            error = e.args[1]
            error = error[(error.index(' ')+1):]
            end = error.index('.')+1
            print "Falied to send message: " + error[:end] + '(' + str(e.args[0]) + ')'