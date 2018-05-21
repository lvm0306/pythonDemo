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
    list = openSQL(num)
    # 测试

    for i in list:
        try:
            respone = requests.get(base + i[3], headers=ua_headers)
            respone.encoding = 'utf-8'
            soup = BeautifulSoup(respone.text, 'html.parser')
            imgs = soup.find('div', class_='news').find_all('img')
            for j in imgs:
                conn = pymysql.connect(host='47.93.222.245', user='aqa', password='mysql',
                                       db='yellow', charset='utf8')
                cursor = conn.cursor()
                try:
                    saveimg(cursor, i[2], j['src'], num)
                except Exception as e:
                    print(e)

                    conn.commit()
                    cursor.close()
                    conn.close()
                    continue
                conn.commit()
                # 关闭游标
                cursor.close()
                # 关闭连接
                conn.close()
        except Exception as e:
            print(e)

    # for i in list:
    #     if (num == 1):
    #         respone = requests.get(base_url, headers=ua_headers)
    #     else:
    #         respone = requests.get(base_url1+str(num)+'.html', headers=ua_headers)
    #     respone.encoding = 'utf-8'
    #     soup = BeautifulSoup(respone.text, 'html.parser')
    #     soup.find('ul', class_='news_list').find_all('a')
    #     # test
    #     # for i in list:
    #     #     print(i['href']+'---'+i['title'])
    #     # for i in list:
    #     #     print(i)


def saveimg(cursor, name, img, num):
    sql = "insert into meinv_pics(infoid,name,pic)values(null,'%s','%s')" % (name, img)
    # sql = "insert into github(id,name,author,href,info,yuyan,star)values(null,{},{},{},{},{},{})".format(name,author,href,info,yuyan,star)
    print(sql)
    cursor.execute(sql)


def openSQL(num):
    print('正在读取第' + str(num) + '页')
    conn = pymysql.connect(host='47.93.222.245', user='aqa', password='mysql',
                           db='yellow', charset='utf8')
    cursor = conn.cursor()

    sql = "select * from meinv_list where page=" + str(num)
    # sql = "insert into github(id,name,author,href,info,yuyan,star)values(null,{},{},{},{},{},{})".format(name,author,href,info,yuyan,star)
    print(sql)
    cursor.execute(sql)
    list = cursor.fetchall()
    print(list)
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    print('读取成功')
    return list


if __name__ == '__main__':
    # getPageList(1)
    for i in range(2, 11):
        getPageList(i)
    # getPageList(2)
