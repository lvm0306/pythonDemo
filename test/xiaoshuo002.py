import csv
import re
import threading

import pymysql
import requests
from bs4 import BeautifulSoup


ua_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}
book_list = []
def getbooklist():
    respone = requests.get("https://www.4455pf.com/htm/novellist2/", headers=ua_headers)
    respone.encoding = 'UTF-8'
    soup = BeautifulSoup(respone.text, 'html.parser')
    # print(soup)
    xiaoshuolist=soup.find("div",class_="news_list")
    # xiaoshuobref=xiaoshuolist.find_all('a')
    print(xiaoshuolist)
    # print(xiaoshuobref)
    # for i in xiaoshuobref:
    #     temp=[]
    #     print(i.string)
    #     print(i["href"])
    #     temp.append(i.string)
    #     temp.append(i["href"])
    #     book_list.append(temp)
    #     print(book_list)
# def getbookneirong(title):
#     respone = requests.get("https://www.4455pf.com/htm/novel2/4477.htm", headers=ua_headers)
#     respone.encoding = 'gbk'
#     soup = BeautifulSoup(respone.text, 'html.parser')
#     neirong=soup.find("div",class_="new")
#     print(neirong.text)
#     with open('y1.txt', 'a') as f:
#         f.write(title)
#         f.write('\n)







getbooklist()
# getbookneirong("夕阳春情")