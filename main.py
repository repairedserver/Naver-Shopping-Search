from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

option = webdriver.ChromeOptions()
option.add_argument("window-size=1280,720")
option.add_argument("no-sandbox")
# option.add_argument("headless")

browser = webdriver.Chrome(ChromeDriverManager().install(), options=option)
browser.get("https://shopping.naver.com/")
time.sleep(3)
browser.close()