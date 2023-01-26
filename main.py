from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

option = webdriver.ChromeOptions()
option.add_argument("window-size=1280,720")
option.add_argument("no-sandbox")

chrome = webdriver.Chrome(ChromeDriverManager().install(), options=option)
chrome.get("https://shopping.naver.com/")
wait = WebDriverWait(chrome, 10)


def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

search = find(wait, "input[class=_searchInput_search_text_fSuJ6]")
search.send_keys("RTX 4090")

time.sleep(3)
chrome.close()