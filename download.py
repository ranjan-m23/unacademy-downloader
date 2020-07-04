#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# driver
driver = webdriver.Chrome("./chromedriver")

# url
driver.get("https://www.unacademy.com/")

# login buttton xpath
xpath = '//*[@id="__next"]/header/div/button'

timeout = 15

# wait for login button
try:
    login_present = EC.presence_of_element_located((By.XPATH,xpath))
    WebDriverWait(driver, timeout).until(login_present)
except TimeoutException:
    print("timout")

print("element found")
login = driver.find_element_by_xpath(xpath)
print(login)
login.click()

# send number and wait for otp

# xpath for number input box
input_xpath = '//*[@id="DrawerPaper"]/div[2]/div[1]/div[2]/div/input'
# xpath for otp input box
otp_xpath = '//*[@id="DrawerPaper"]/div[2]/div[1]/form/div/input'


time.sleep(3)

# set number_input
input_elem = driver.find_element_by_xpath(input_xpath)

# send number
key = input("enter login number: ")
input_elem.send_keys()
input_elem.send_keys(Keys.RETURN)

time.sleep(3)

# get otp input checkbox
otp_elem = driver.find_element_by_xpath(otp_xpath)

# ask for otp
otp = input("Enter sent otp: ")

# send otp
otp_elem.send_keys(otp)
otp_elem.send_keys(Keys.RETURN)

time.sleep(2)

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

course_url = input("enter course url: ")
driver.get(course_url)



classname_menu_button = "ItemCard__MenuButton-xrh60s-2"

# check fo menuicon's presence 
try:
    classname_exists = EC.presence_of_element_located((By.CLASS_NAME,classname_menu_button))
    WebDriverWait(driver,timeout).until(classname_exists)
except TimeoutException:
    print("timeout")


time.sleep(2)
links = driver.execute_script("""
let x = document.getElementsByClassName("ItemCard__MenuButton-xrh60s-2 wkXCK menuButton")
a = []
for(let i=0;i<x.length;i++){
x[i].click()
a.push(document.getElementsByClassName("slides")[0].getAttribute("data-href"))
}
return a
 """)

# write all links to file
with open("links2.txt",'a') as f:
    for link in links:
        f.write(link + '\n')
    




