from gettext import find
from multiprocessing.connection import wait
from unicodedata import category
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os


chrome = webdriver.Chrome('/opt/homebrew/bin/chromedriver')
wait = WebDriverWait(chrome, 10)



def find_present(css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,css_selector)))

def finds_present(css_seletor):
    find_present(css_seletor)
    return chrome.find_elements(By.CSS_SELECTOR,css_seletor)

def find_visible(css_selector):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,css_selector)))

def finds_visible(css_seletor):
    find_present(css_seletor)
    return chrome.find_elements(By.CSS_SELECTOR,css_seletor)

category = {
    "cpu":"873",
    "mainboard": "875",
    "memory": "874",
    "graphic_card" : "876",
    'ssd':"32617",
    "case":"879",
    "power":"880"
}

chrome.get('http://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_lw_esti')


#메인보드 탭으로 이동
mainboard = find_visible(f"dd.category_{category['mainboard']} a" )
mainboard.click()

time.sleep(5)

chrome.quit()