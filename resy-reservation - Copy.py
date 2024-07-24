#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import datetime
import time

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
today = datetime.date.today()
delta = datetime.timedelta(days=27)
future = today + delta
futureStr = future.isoformat()
print("Getting maydan for " + futureStr)
driver.get("https://resy.com/cities/dc/maydan?date=" + futureStr + "&seats=2")
# driver.get("https://resy.com/cities/dc/estadio?date=" + futureStr + "&seats=2")
driver.implicitly_wait(10)

print("Closing popup")
popup = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/button')
popup.click()

print("Clicking login")
login = driver.find_element_by_xpath('//*[@id="page-wrapper"]/resy-nav/header/div[1]/resy-menu-container/div/div/button')
login.click()

print("Click use password (instead of 2fa)")
usePass = driver.find_element_by_xpath('/html/body/div[1]/div/div/resy-auth/div/div[2]/div[6]/button')
usePass.click()

print("Enter email and password")
email = driver.find_element_by_xpath('/html/body/div[1]/div/div/resy-auth/div/div[2]/div[3]/div/form/div/input[1]')
password = driver.find_element_by_xpath('/html/body/div[1]/div/div/resy-auth/div/div[2]/div[3]/div/form/div/input[2]')
submit = driver.find_element_by_xpath('/html/body/div[1]/div/div/resy-auth/div/div[2]/div[3]/div/form/div/div/button')
email.send_keys('') # put email here
password.send_keys('') # put password here
submit.click()

loop = True
counter = 0
driver.implicitly_wait(1)
while loop and counter < 5:
    try:
        print("Click calendar button")
        calendarButton = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/article/section[1]/resy-inline-booking/div/div/div[1]/resy-button-group/ng-transclude/resy-button/button')
        calendarButton.click()
        print("Click reservation button")
        resyButton = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/article/section[1]/resy-inline-booking/div/div/div[2]/div/resy-reservation-button-list/resy-reservation-button[last()-1]')
        loop = False
        resyButton.click()
    except:
        print("Reload")
        driver.get("https://resy.com/cities/dc/maydan?date=" + futureStr + "&seats=2")
        # driver.get("https://resy.com/cities/dc/estadio?date=" + futureStr + "&seats=2")
        counter += 1
driver.implicitly_wait(10)
time.sleep(3)
print("Opening iframe")
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[3]/div[2]/iframe"))
driver.implicitly_wait(10)
confirm = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/button')
print("Clicking confirm button")