from selenium import webdriver
import time


options = webdriver.ChromeOptions()
options.add_argument('--window-size=100,100')  # 공백주의!
options.add_argument('no-sandbox') # 샌드박스란? 
# options.add_argument('headless') # 크롬창을 안보이게 함.
chrome = webdriver.Chrome("/opt/homebrew/bin/chromedriver",options = options)
chrome.get("https://naver.com") # 사이트 접속, get 은 '이동한다' 는 의미.
chrome.get('https://shopping.naver.com')
chrome.back()
chrome.forward()
time.sleep(5)
chrome.close()
