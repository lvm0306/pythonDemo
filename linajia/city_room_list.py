import csv
import random
import re
import threading

import pymysql
import requests
from bs4 import BeautifulSoup

from util.constant import local_headers
from util.getEncoding import getEncoding

base ='https://hz.lianjia.com/zufang/xiasha/'

def getRoomList():
    respone=requests.get(base,headers=local_headers)
    respone.encoding=getEncoding(base).get_encode2()
    soup=BeautifulSoup(respone.text,'html.parser')
    lis=soup.find(id='house-lst').find_all('li')
    for i in lis:
        div_=i.find('div',class_='info-panel')
        #租房子的价格
        price=i.find('div',class_='price').span.string
        info=i.find('div',class_='con').text
        size=i.find('span',class_='meters').text.replace('平米','').strip()
        style=i.find('span',class_='zone').text.strip()
        adress=i.find('span',class_='region').text.strip()
        print(adress)




if __name__=='__main__':
    getRoomList()

