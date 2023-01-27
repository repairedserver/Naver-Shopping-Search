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
short_wait = WebDriverWait(chrome, 5)

chrome.get("https://shopping.naver.com/")
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a#gnb_login_button'))).click()

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id")))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw")))

# 로그인 기능 --------------------------------------------
pyperclip.copy("dnjfdid14")
# input_id.send_keys(Keys.CONTROL, "v") # 윈도우 전용
input_id.send_keys(Keys.COMMAND, "v") # 맥 전용

pyperclip.copy("Your Password")
input_pw.send_keys(Keys.COMMAND, "v")
input_pw.send_keys("\n")
# -----------------------------------------------------

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_logout_button")))

search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[class=_searchInput_search_text_fSuJ6]")))
search.send_keys("RTX 4090\n")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^=basicList_info_area__]")))

# 스크롤
for i in range(8):
    chrome.execute_script("window.scrollBy(0, " + str((i + 1) * 1000) + ")")
    time.sleep(1)

items = chrome.find_elements_by_css_selector("div[class^=basicList_info_area__]")
for i in items:
    # 광고 제외
    try:
        i.parent.parent.find_element_by_css_selector("button[class^=ad_")
        continue
    except:
        pass
    print(i.find_element_by_css_selector("a[class^=basicList_link__]").text)

chrome.close()