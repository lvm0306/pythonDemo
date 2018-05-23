import csv
import random
import re
import threading

import pymysql
import requests
from bs4 import BeautifulSoup

from util.constant import local_headers
from util.getEncoding import getEncoding


class Citys():
    def __init__(self, url):
        self.url = url

    def getCityList(self):
        print('获取城市列表')
        respone = requests.get(self.url, headers=local_headers)
        respone.encoding = getEncoding(self.url).get_encode2()
        soup = BeautifulSoup(respone.text, 'html.parser')
        divs = soup.find('div', class_='all').find_all('ul', class_='clear')
        print('获取成功')
        print('开始入库')
        conn = pymysql.connect(host='localhost', user='root', password='',
                               db='lianjia', charset='utf8')
        cursor = conn.cursor()
        for i in divs:
            lis = i.find_all('li')
            for j in lis:
                print(j.a['href'])
                print(j.a.string)
                sql = "insert into city_list(id, city_name, city_link)values (null,'%s','%s')" % (
                j.a.string, j.a['href'])
                # print(sql)
                cursor.execute(sql)
                conn.commit()
        cursor.close()
        conn.close()
        print('入库成功')
