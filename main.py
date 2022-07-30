
from calendar import c
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
import pyperclip
chrome = webdriver.Chrome("/opt/homebrew/bin/chromedriver")


uid = '#'
upw = '#!'

wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get('https://shopping.naver.com')

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'a[class="gnb_btn_login"]')))


# 로그인 시도
chrome.find_element(By.CSS_SELECTOR,'a[class="gnb_btn_login"]').click()

time.sleep(3)

tag_id = chrome.find_element(By.CSS_SELECTOR,'input[id="id"]')
pyperclip.copy(uid)
tag_id.send_keys(Keys.COMMAND,'v')
time.sleep(3)

tag_pw = chrome.find_element(By.CSS_SELECTOR,'input[id="pw"]')
pyperclip.copy(upw)
tag_pw.send_keys(Keys.COMMAND,'v')
time.sleep(3)


chrome.find_element(By.CSS_SELECTOR, 'button[class="btn_login"]').click()

time.sleep(5)

chrome.find_element(By.CSS_SELECTOR,'a[id="new.save"]').click()


search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input._searchInput_search_input_QXUFf')))

search.send_keys('아이폰 케이스\n')
time.sleep(2)
iPhones = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"a[class^='basicList_link__']")))
iPhones[2].click()
time.sleep(2)
chrome.switch_to.window(chrome.window_handles[1]) # 탭이동


# 상품 상세페이지
# 옵션 고른 뒤에
# 구매버튼 클릭

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[aria-haspopup="listbox"]')))
options = chrome.find_elements(By.CSS_SELECTOR,'a[aria-haspopup="listbox"]')

options[0].click()

#첫 번째 옵션 클릭
time.sleep(2)
chrome.find_elements(By.CSS_SELECTOR,'ul[role="listbox"] a[role="option"]')[0].click()


#두 번째 옵션 클릭
options[1].click()
chrome.find_elements(By.CSS_SELECTOR,'ul[role="listbox"] a[role="option"]')[0].click()


time.sleep(2)

#결제하기 버튼 누르기

chrome.find_elements(By.CSS_SELECTOR,"div[class*='N=a:pcs.buy'] a")[0].click()

time.sleep(5)


chrome.quit() # 크롬자체를 끄는 행위.
