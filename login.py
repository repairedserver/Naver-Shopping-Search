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
wait = WebDriverWait(chrome, 100)

chrome.get("https://shopping.naver.com/")
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a#gnb_login_button'))).click()

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id")))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw")))

pyperclip.copy("dnjfdid14")
# input_id.send_keys(Keys.CONTROL, "v") # 윈도우 전용
input_id.send_keys(Keys.COMMAND, "v") # 맥 전용

pyperclip.copy("@dnddk1052")
input_pw.send_keys(Keys.COMMAND, "v")
input_pw.send_keys("\n")

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_logout_button")))

chrome.close()