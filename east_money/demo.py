import time
import csv
from selenium import webdriver

url = 'http://data.eastmoney.com/stock/lhb/300078.html'
# chromedriver='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome('chromedriver')
browser.get(url)
time.sleep(3)
#//*[@id="dt_1"]
# //*[@id="dt_1"]/tbody

tabs = browser.find_elements_by_xpath('//*[@id="main-wrap"]/div/div[2]/div/div[7]//table')
with open('300078.csv', 'a', newline='') as csv_file:
    csv_write=csv.writer(csv_file)
    for i in tabs:
        th_trs = i.find_elements_by_xpath('./thead//tr')
        tb_trs = i.find_elements_by_xpath('./tbody//tr')
        oneline=[]
        twoline=[]
        for j in th_trs:
            try:
                ths = j.find_elements_by_xpath('.//th')
                for k in ths:
                    text = k.text
            except Exception as e:
                text = '-'
            oneline.append(text)
        csv_write.writerow(oneline)
        print(oneline)

        for j in tb_trs:
            try:
                tds = j.find_elements_by_xpath('.//td')
                print(tds)
                print(len(tds))
                for k ,value in tds,range(len(tds)):
                    # if is_element_exit
                    if value!=1:
                        text = k.text
                    else:
                        text=k.find_element_by_xpath('./div[1]/a[2]').text
            except Exception as  e:
                text = '-'
            twoline.append(text)
        csv_write.writerow(twoline)
        print(twoline)
