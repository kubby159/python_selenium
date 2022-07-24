from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.add_argument('--window-size=500,500')  # 공백주의!
options.add_argument('no-sandbox') # 샌드박스란? 
# options.add_argument('headless') # 크롬창을 안보이게 함.
chrome = webdriver.Chrome("/opt/homebrew/bin/chromedriver",options = options)
chrome.get('https://shopping.naver.com')
wait = WebDriverWait(chrome,10)

def find(wait,css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,css_selector)))



search = find(wait,'input[title="검색어 입력"]')
# \n: new line => 엔터치는 행위를 하게 됨.
search.send_keys('아이폰 케이스\n') # 검색창에 아이폰 케이스가 입력됨.
time.sleep(5)


# 엘리먼트를 클릭하는 로직
# btn =find(wait,'button._searchInput_button_search_1n1aw')
# btn.click() # 해당 엘리먼트를 클릭한다.
# time.sleep(5)
chrome.close()