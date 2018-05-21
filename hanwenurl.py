# -*-coding:utf-8-*-
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

baseurl = 'https://www.gavbus516.com'


class Fan():
    def __init__(self, movie_name, movie_douban_fen,
                 movie_url, movie_time):
        self.name = movie_name  # 电影名称
        self.fen = movie_douban_fen  # 电影评分
        self.url = movie_url  # 电影类型
        self.time = movie_time  # 电影地区


def getHtml(url, loadmore=True, waittime=1):
    browser = webdriver.Chrome('chromedriver')
    browser.get(url)
    # time.sleep(waittime)
    # if loadmore:
    #     while True:
    #         try:
    #             next_button = browser.find_element_by_class_name("more")
    #             next_button.click()
    #             time.sleep(waittime)
    #         except:
    #             break
    html = browser.page_source
    browser.quit()
    return html


def geturlinfo(url):
    try:
        info_respone = getHtml(url, False, 1)
        info_soup = BeautifulSoup(info_respone, 'html.parser')
        title = info_soup.find(class_='container').h3.string
        fanhao = info_soup.select('#magnet-table > tbody > tr:nth-of-type(2) > td:nth-of-type(1) > a')
        size = info_soup.select('#magnet-table > tbody > tr:nth-of-type(2) > td:nth-of-type(2) > a')
        time = info_soup.select('#magnet-table > tbody > tr:nth-of-type(2) > td:nth-of-type(3) > a')
        print(fanhao)
        print(size[0].string)
        print(time)
        fan = (title, size[0].string, fanhao[0]['href'], time[0].string)

    except Exception as e:
        fan = ('','', '', '')
        print(e)

    return fan
    # print(title)
    # manger=info_soup.find(id='magnet-table')
    # manger.find('tr')
    # a=manger.find_all('a')
    # for i in a :
    #     try:
    #         print(i['href'])
    #         print(i)
    #         print(i.string)
    #     except Exception as e:
    #         print(e)
    #         break


def getm(num):
    for i in range(5, num):
        output_list = []
        request=requests.get('https://www.gavbus516.com/page/' + str(i));
        request.encoding='utf-8'
        respone = requests.get('https://www.gavbus516.com/page/' + str(i))
        soup = BeautifulSoup(respone.text, 'html.parser')
        content = soup.find(id='waterfall');
        con = content.findAll('a')
        # geturlinfo(baseurl+con[0]['href'])
        for c in con:
            nexturl = baseurl + c['href']
            yuanzu=geturlinfo(nexturl)
            # print(yuanzu[0])
            # print(yuanzu[1])
            # print(yuanzu[2])
            # output_list.append(geturlinfo(nexturl))
            try:
                with open("fan.csv", 'a', encoding='utf-8',newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    # for movie in info:
                    # writein_list = [yuanzu[0], yuanzu[1], yuanzu[2], yuanzu[3]]
                    # writein_list=list(yuanzu)
                    writer.writerow(yuanzu)
                    csvfile.close()
            except Exception as e:
                print(e)



getm(500)
