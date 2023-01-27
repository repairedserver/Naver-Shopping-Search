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
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a#gnb_login_button'))).click()

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id")))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw")))

id = input("당신의 네이버 아이디를 입력해 주세요 : ")
input_id.send_keys(id)
pw = input("당신의 패스워드를 입력해 주세요 : ")
input_pw.send_keys(pw)
input_pw.send_keys("\n")

time.sleep(5)

chrome.close()