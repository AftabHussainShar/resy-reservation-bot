from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

driver = webdriver.Chrome()
driver.maximize_window()
url = 'https://resy.com/'
driver.get(url)

try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/resy-nav/header/div[2]/div[2]/resy-menu-container/div/button'))
    )
    login_button.click()
    print("Clicked on the Log in button")
    time.sleep(2)
except Exception as e:
    print(f"Error: {str(e)}")

try:
    email_password_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Use Email and Password instead"]'))
    )
    email_password_button.click()
    print("Clicked on the 'Use Email and Password instead' button")
    time.sleep(2)
except Exception as e:
    print(f"Error: {str(e)}")

try:
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'email'))
    )
    email_input.clear()
    email_input.send_keys('resytemp1124@gmail.com') 
    print("Entered email address successfully")
    time.sleep(2)

except Exception as e:
    print(f"Error: {str(e)}")

try:
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'password'))
    )
    email_input.clear()
    email_input.send_keys('R3syT3mp!') 
    print("Entered email address successfully")
    time.sleep(2)
except Exception as e:
    print(f"Error: {str(e)}")

try:
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='Button Button--primary Button--lg']"))
    )
    continue_button.click()
    print("Clicked on 'Continue' button successfully")
    time.sleep(2)
except Exception as e:
    print(f"Error: {str(e)}")
    
try:
    c = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//button[teXt()="No Thanks"]'))
    )
    c.click()
    print("Clicked ")
    time.sleep(2)
except Exception as e:
    print(f"Error: {str(e)}")
    
try:
    # input_element = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, "reactautosuggest__input"))
    # )
    # input_element.click()
    # input_element.send_keys("la Pecora Bianca - UES")
    # input_element.send_keys(Keys.ENTER)
    url = 'https://resy.com/cities/brisbane-qld/venues/bbq-tonight-restaurant?date=2024-07-20&seats=2&facet=cuisine:Pakistani'
    driver.get(url)
    time.sleep(2)
except:
    print(f"Error: ")
    
# try:
#     c = WebDriverWait(driver, 5).until(
#         EC.element_to_be_clickable((By.XPATH, '//button[text()="No Thanks"]'))
#     )
#     c.click()
#     print("Clicked ")
#     time.sleep(2)
# except Exception as e:
#     print(f"Error: {str(e)}")
try:
    order = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/div/venue-page/div/div[2]/div[1]/div[2]/div[3]/div/button[1]'))
    )
    order.click()
except Exception as e:
    print(f"Error: {str(e)}")
time.sleep(3)

try:
    time.sleep(3)
    pyautogui.click(x=678, y=253)
    pyautogui.press('pagedown')
    time.sleep(5)
    pyautogui.click(x=672, y=528)
    time.sleep(5)
    pyautogui.press('pagedown')
    pyautogui.click(x=672, y=528)

except Exception as e:
    print(f"Error: {str(e)}")

