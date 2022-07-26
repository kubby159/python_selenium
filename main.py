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
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a[class^='basicList_link__']")))
titles = chrome.find_elements(By.CSS_SELECTOR,"a[class^='basicList_link__']")

for title in titles:
    print(title.text)

chrome.close()