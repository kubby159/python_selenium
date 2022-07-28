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
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a[class^='basicList_link__']"))).click()

time.sleep(2)
chrome.switch_to.window(chrome.window_handles[1]) # 탭이동


print(chrome.title)

chrome.quit() # 크롬자체를 끄는 행위.