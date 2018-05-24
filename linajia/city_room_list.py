import csv
import random
import re
import threading

import pymysql
import requests
from bs4 import BeautifulSoup

from util.constant import local_headers
from util.getEncoding import getEncoding

base = 'https://hz.lianjia.com/'
# 租金 1000元以下，1000-2000，2000-3000，3000-5000，5000以上
zujin = ['rp1', 'rp2', 'rp3', 'rp4', 'rp5']


#

def getRoomList(cursor, conn, url, city_name):
    qu = []
    qu_name = []
    newurl = ''
    if (url.find('zufang') == -1):
        newurl = url + 'zufang/'
    else:
        newurl=url
    print(newurl)
    respone = requests.get(newurl, headers=local_headers)
    respone.encoding = getEncoding(newurl).get_encode2()
    soup = BeautifulSoup(respone.text, 'html.parser')
    areas = soup.find('div', id='filter-options').find_all('dl')[0].find_all('a')
    areas = areas[1:]
    for i in areas:
        qu_name.append(i.string)
        if (i['href'].find('https:') == -1):
            qu.append(url + i['href'])
        else:
            qu.append(i['href'])
    # print(qu)
    print(qu_name)

    for i in qu:
        try:
            saveInfo(cursor, conn, i, 1, qu, city_name, qu_name)
            # print(qu.index(i))

        except Exception as  e:
            print(e)


def saveInfo(cursor, conn, url, num, qu, city_name, qu_name):
    if num > 1:
        newurl = url + 'pg' + str(num) + '/'
    else:
        newurl = url
    print(newurl + '当前是第' + str(num) + '页')

    respone = requests.get(newurl, headers=local_headers)
    respone.encoding = getEncoding(newurl).get_encode2()
    soup = BeautifulSoup(respone.text, 'html.parser')
    try:
        page = int(soup.find('div', class_='page-box house-lst-page-box')['page-data'].split(',')[0].split(':')[1])
        print('共' + str(page) + '页')
    except Exception as e:
        page = 1

    lis = soup.find(id='house-lst').find_all('li')
    for i in lis:
        div_ = i.find('div', class_='info-panel')
        # 租房子的价格
        price = int(i.find('div', class_='price').span.string)
        info = i.find('div', class_='con').text
        size = int(i.find('span', class_='meters').text.replace('平米', '').strip())
        style = i.find('span', class_='zone').text.strip()
        adress = i.find('span', class_='region').text.strip()
        sql = "INSERT INTO city_room_list(id,city_name,city_area,adress,style,size,price,info) VALUES (null,'%s','%s','%s','%s',%d,%d,'%s')" % (
            city_name, qu_name[qu.index(url)], adress, style, size, price, info)
        print(sql)
        cursor.execute(sql)
        conn.commit()
        # print(adress)
    if page == num:
        return

    num += 1
    if num <= page:
        saveInfo(cursor, conn, url, num, qu, city_name, qu_name)

def getRoomList2(url):
    qu = []
    qu_name = []
    newurl = ''
    if (url.find('zufang') == -1):
        newurl = url + 'zufang/'
    else:
        newurl=url
    print(newurl)
    respone = requests.get(newurl, headers=local_headers)
    respone.encoding = getEncoding(newurl).get_encode2()
    soup = BeautifulSoup(respone.text, 'html.parser')
    areas = soup.find('div', id='filter-options').find_all('dl')[0].find_all('a')
    areas = areas[1:]
    for i in areas:
        qu_name.append(i.string)
        if (i['href'].find('https:') == -1):
            qu.append(url + i['href'])
        else:
            qu.append(i['href'])
    # print(qu)
    print(qu_name)



if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', user='root', password='',
                           db='lianjia', charset='utf8')
    cursor = conn.cursor()
    sql = 'select * from city_list'
    cursor.execute(sql)
    citys = cursor.fetchall()
    for i in citys:
        # print(i[2],i[1])
        if (i[2].split('/')[3] == ''):
            if i[2].split('/')[2].split('.')[1] == 'lianjia':
                try:
                    getRoomList(cursor, conn, i[2], i[1])
                except Exception as e:
                    print(e)
        else:
            print(i[2] + '呗筛选掉了')

    # getRoomList2('https://zz.lianjia.com//zufang/huiji/')
