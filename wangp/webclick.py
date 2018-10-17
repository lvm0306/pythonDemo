from selenium import webdriver
import time
url = 'https://cookie.riimu.net/speed/'
browser = webdriver.Chrome('chromedriver')
browser.get(url)
time.sleep(3)
for i in range(1000):
    time.sleep(0.0001)
    next_button = browser.find_element_by_id("virtualCookie")
    next_button.click()
