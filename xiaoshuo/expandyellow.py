from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import  ActionChains

"""
url: the douban page we will get html from
loadmore: whether or not click load more on the bottom 
waittime: seconds the broswer will wait after intial load and 
""" 
def getHtml(url, waittime = 1):
    browser = webdriver.Chrome('chromedriver')
    browser.get(url)
    # browser.find_element_by_xpath("./body/form/table[1]/tbody/tr[0]/td[1]").click()
    browser.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[2]/input").click()
    # right_click = browser.find_element_by_link_text('点击下载')

    # browser.find_elements_by_xpath("//*/input[@type='submit']")[0].click()
    # ActionChains(browser).click(right_click)
    # next_button = browser.find_element_by_class_name("more")
    # browser.
    # next_button.click()
    time.sleep(waittime)
    browser.quit()


# for test
# url = "http://www.jandown.com/link.php?ref=kAHxeQVoPD"
# html = getHtml(url)
# print(html)
