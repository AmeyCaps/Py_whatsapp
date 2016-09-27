from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

message ="Hello !!"  # your message 
n = 5                # Send n number of times

def initiate():
	global driver  
	driver = webdriver.Chrome()
	driver.get("https://web.whatsapp.com")
	print "Lets begin !!"

def stop():
	print "Done !!"
	driver.quit()

def send_message():
	
	group= ""  # enter name of person or group to send message 
	search = driver.find_element_by_xpath("//*[@data-tab=2]")  
	search.send_keys(group)
	time.sleep(10)
	active = driver.find_element_by_xpath("//div[@contextmenu='false']")
	active.click()
	time.sleep(3)
	msg = driver.find_element_by_xpath("//div[@contenteditable='true']")
	for i in range(0,n):
		msg.send_keys(message)
		msg.send_keys(Keys.RETURN)
		time.sleep(1)

if __name__ == '__main__' : 
	initiate() 
	time.sleep(10)
	send_message()
	time.sleep(5)
	stop()
