from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver  = webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")
search1 = driver.find_element_by_id("username")
search2 = driver.find_element_by_id("password")
search3 = driver.find_element_by_id("valuepkg3")
push = driver.find_element_by_id("loginbtn")
login = input("Enter your kerberos ID:")
search1.send_keys(login)
str1 = input("Enter your kerberos password:")
search2.send_keys(str1)
main = driver.find_element_by_id("login")
str2 = main.text
search3.clear()
if "add" in str2:
	res = [int(i) for i in str2.split() if i.isdigit()]
	search3.send_keys(str(res[0]+res[1]))
elif "subtract" in str2:
	res = [int(i) for i in str2.split() if i.isdigit()]
	search3.send_keys(str(res[0]-res[1]))
elif "first" in str2:
	res = [int(i) for i in str2.split() if i.isdigit()]
	search3.send_keys(res[0])
else:
	res = [int(i) for i in str2.split() if i.isdigit()]
	search3.send_keys(res[1])
push.click()