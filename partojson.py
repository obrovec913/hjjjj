from bs4 import BeautifulSoup
import pyautogui
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



re = open('Japanese Diapers Shop _ Lowest Prices in Europe + Free Shipping.html', encoding="utf-8").read()


soup = BeautifulSoup(re, 'lxml')
quotes = soup.find_all('div', class_='product-element-top')

for pr in quotes:
    pp = pr.find('a').get('href')
    print(pp)
    nam = pp.split('/')
    s = Service(executable_path='chromedriver_win32 (3)\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    try:
        driver.maximize_window()
        driver.get(pp)
        time.sleep(12)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(11)
        pyautogui.typewrite(nam[-2] + '.html')
        pyautogui.hotkey('enter')
        time.sleep(70)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
print()