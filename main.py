from selenium import webdriver
import time
chrome = webdriver.Chrome("/opt/homebrew/bin/chromedriver")
chrome.get("http://blog.naver.com/lynn1128") # 사이트 접속
time.sleep(2)
chrome.close()
