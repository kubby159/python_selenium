from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
import pyperclip
chrome = webdriver.Chrome("/opt/homebrew/bin/chromedriver")


wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get('https://shopping.naver.com')

search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input._searchInput_search_input_QXUFf')))

search.send_keys('아이폰 케이스\n')
time.sleep(2)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[class^='basicList_info_area__']")))



#스크롤
#셀레니움이 자바스크립트를 실행시킬 수 있음.
for i in range(20):
    chrome.execute_script('window.scrollBy(0,10000)')

time.sleep(3)
items = chrome.find_elements(By.CSS_SELECTOR,"div[class^='basicList_info_area__']")
for item in items:
    #광고 빼기
    try:
        item.parent.parent.find_element(By.CSS_SELECTOR,'button[class^="ad_"]')
        continue
    except:
        pass
    print(item.find_element(By.CSS_SELECTOR,'a[class^="basicList_link__"]').text)

chrome.close()