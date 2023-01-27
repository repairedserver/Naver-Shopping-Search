from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip

chrome = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get("https://shopping.naver.com/")
login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a#gnb_login_button')))
print(login.text)
login.click()

time.sleep(5)

chrome.close()