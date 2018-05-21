from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://www.taobao.com/")

# 通过id等查找
input_first = browser.find_element(By.ID,"gwd_price_tip")
# 使用script
browser.execute_script('alert("To Bottom")')
time.sleep(1)

browser.quit()