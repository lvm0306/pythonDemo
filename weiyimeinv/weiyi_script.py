import csv
import random
import re
import threading

import pymysql
import requests
from bs4 import BeautifulSoup
import util
from util.getEncoding import getEncoding

ua_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}

headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
           'Accept - Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
           'Connection': 'Keep-Alive',
           'Host': 'zhannei.baidu.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
# user_agent = random.choice(ua_list)
head = ''
base = 'http://www.mmonly.cc/'
tag = 'tag/'
# 动态获取
tag_title = []
tag_info = []
tag_dic = {}


# 获取网站的tag
def catchTag():
    respone = requests.get(base + tag, headers=ua_headers)
    respone.encoding = getEncoding(base + tag).get_encode2()
    soup = BeautifulSoup(respone.text, 'html.parser')
    # 获取纵列
    lists_tag = soup.find_all('h2')
    for i in lists_tag:
        tag_title.append(i.string)

    lists = soup.find_all('div', class_='TagList')
    for i in lists:
        if i != '':
            links = i.find_all('a')
            tag_list = []
            for j in links:
                temp_ = []
                temp_.append(j['href'])
                temp_.append(j['title'])
                tag_list.append(temp_)

            tag_dic[tag_title[lists.index(i)]] = tag_list


# 执行sql语句
def getConn(conn, cursor, type, name, url):
    sql = "insert into weiyi_list(id, type, name, url)values (null,'%s','%s','%s')" % (type, name, url)
    print(sql)
    cursor.execute(sql)
    conn.commit()


# 将tag 分类保存至 本地数据库
def savelocalsql():
    conn = pymysql.connect(host='localhost', user='root', password='',
                           db='weiyi', charset='utf8')
    cursor = conn.cursor()
    for key, item in tag_dic.items():
        for i in item:
            getConn(conn, cursor, key, i[1], i[0])

    cursor.close()
    conn.close()


def getinfo(num):
    if num == 1:
        respone = requests.get("http://www.mmonly.cc/tag/cs/", headers=ua_headers)
    else:
        respone = requests.get("http://www.mmonly.cc/tag/cs/" + str(num) + ".html", headers=ua_headers)
    respone.encoding = getEncoding(base + tag).get_encode2()
    soup = BeautifulSoup(respone.text, 'html.parser')
    # 获取页码 和第一页入库
    pages = soup.find_all('div', class_='pages')[0].find_all('li')
    if (len(pages) == 1):
        page = 1
    else:
        page = len(pages) - 2
    print(page)
    divs = soup.find_all('div', class_='item masonry_brick masonry-brick')
    for i in divs:
        a = i.find('a', class_='img_album_btn')
        print(a['href'])
        print(i.find_all('img')[0]['src'])
        getpiclist()

    # 判断是否有第二页，没有的话入下一个tag
    if page == 1:
        return
    else:
        num += 1
        if num <= page:
            getinfo(num)


def getpiclist(num):
    if num == 1:
        respone = requests.get("http://www.mmonly.cc/mmtp/xgmn/243865.html", headers=ua_headers)
    else:
        respone = requests.get("http://www.mmonly.cc/mmtp/xgmn/243865_" + str(num) + ".html", headers=ua_headers)
    respone.encoding = getEncoding(base + tag).get_encode2()
    soup = BeautifulSoup(respone.text, 'html.parser')
    # 获取页码 和第一页入库
    bottom_pages = soup.find_all('div', class_='pages')[0].find_all('li')
    # print(pages[0].a.string[2])
    bg=bottom_pages[0].a.string
    page=int(bg.replace('共','').replace('页:',''))
    if page == 1:
        page=1

    pic = soup.find('div', id='big-pic').find('img')['src']
    print(pic)

    # 判断是否有第二页，没有的话入下一个tag
    if page == 1:
        return
    else:
        num+=1
        if num <= page:
            getpiclist(num)
        else:
            return


# main
if __name__ == '__main__':
    # 获取tag 至 本地数据库
    # catchTag()
    # savelocalsql()
    # 获取每个Tag 的详情
    getinfo()
    getpiclist(1)
