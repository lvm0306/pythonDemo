import csv
import random
import re
import threading

import pymysql
import requests
from bs4 import BeautifulSoup

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
base_url1 = 'https://www.3344gu.com/tupianqu/siwa/index_'
base_url = 'https://www.3344gu.com/tupianqu/siwa/index.html'
head = ''
base = 'https://www.3344gu.com/'


def getPageList(num):
    if (num == 1):
        respone = requests.get(base_url, headers=ua_headers)
    else:
        respone = requests.get(base_url1+str(num)+'.html', headers=ua_headers)
    respone.encoding = 'utf-8'
    soup = BeautifulSoup(respone.text, 'html.parser')
    list = soup.find('ul', class_='news_list').find_all('a')
    openSQL(list,num)
    # test
    # for i in list:
    #     print(i['href']+'---'+i['title'])
    # for i in list:
    #     print(i)


def openSQL(list,num):
    print('正在录入第'+str(num)+'页')
    info='正在录入第'+str(num)+'页'
    conn = pymysql.connect(host='localhost', user='aqa', password='mysql',
                           db='yellow', charset='utf8')
    cursor = conn.cursor()

    for i in list:
        info=i['title'].replace('\'','。')
        sql = "insert into meinv_list(id,page,name,href)values(null,%d,'%s','%s')" % (num,info,i['href'])
        # sql = "insert into github(id,name,author,href,info,yuyan,star)values(null,{},{},{},{},{},{})".format(name,author,href,info,yuyan,star)
        print(info+sql)
        cursor.execute(sql)


    conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    print('录入成功')

if __name__ == '__main__':
    for i in range(483, 2000):
        getPageList(i)
    # getPageList(2)
