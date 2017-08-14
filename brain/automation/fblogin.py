from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# AUTO FACEBOOK LOGIN ...

import getpass

def fblogin():
	print 'Email:'
	EMAIL_ID = raw_input()
	PASSWORD = getpass.getpass()


	driver = webdriver.Chrome()
	# webpage = 'http://www.google.com'
	facebook_webpage = 'https://www.facebook.com'
	driver.get(facebook_webpage)


	email = driver.find_element_by_name('email')
	password = driver.find_element_by_name('pass')

	email.clear()
	email.send_keys(EMAIL_ID)
	password.clear()
	password.send_keys(PASSWORD)
	password.send_keys(Keys.RETURN)

