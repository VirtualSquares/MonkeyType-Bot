from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as pg
import time

driver = webdriver.Chrome()
driver.get("https://monkeytype.com")
time.sleep(2)

acceptButton = driver.find_element(By.CLASS_NAME, "acceptAll")
acceptButton.click()

def login():
    page = driver.find_element(By.CLASS_NAME, "view-login")
    page.click()

    email = driver.find_element(By.NAME, "current-email")
    email.send_keys("[YOUR EMAIL]")

    password = driver.find_element(By.NAME, "current-password")
    password.send_keys("[YOUR PASSWORD]")

    submit = driver.find_element(By.CLASS_NAME, "signIn")
    submit.click()

    start = driver.find_element(By.CLASS_NAME, "view-start")
    start.click()

login()

while True:

    try:

        word = driver.find_element(By.CSS_SELECTOR, ".word.active")
        string = ""
        
        letters = word.find_elements(By.TAG_NAME, "letter")
        
        for i in letters:
            string += i.text
            
        pg.write(string + " ")

    except:
        
        break

