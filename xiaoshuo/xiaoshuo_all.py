import csv
import re
import threading

import pymysql
import requests
from bs4 import BeautifulSoup

base = 'https://www.cangqionglongqi.com'
baseurl = 'https://www.cangqionglongqi.com/quanbuxiaoshuo/'
local = '/Users/lovesosoi/Documents/python3_space/xiaoshuo/xiaoshuo/book1/'
taglist = []
booklist = []

ua_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}


class mythread(threading.Thread):
    def __init__(self, name, url):
        threading.Thread.__init__(self, name=name)
        self.url = url

    def run(self):
        getBookTitle(self.name, self.url)


# 获取小说的名字
def getBookNameList():
    respone = requests.get(baseurl, headers=ua_headers)
    respone.encoding = 'gbk'
    soup = BeautifulSoup(respone.text, 'html.parser')
    booktaglist = soup.find_all('div', 'novellist')
    # print(booktaglist[0])
    for i in booktaglist:
        type = i.find('h2').string
        type = type[:len(type) - 6]
        print(type)
        # 获取全部标签
        taglist.append(i.find('h2').string[:len(i.find('h2').string) - 6])
        conn = pymysql.connect(host='47.93.222.245', user='aqa', password='mysql',
                               db='book', charset='utf8')
        cursor = conn.cursor()
        for j in i.find_all('a'):
            sql = "insert into book_list(id,type,name,name_en)values (null,'%s','%s','%s')" % (
                type, j.string, j['href'].replace('/', ''))
            print(sql)
            cursor.execute(sql)
            conn.commit()
            # 关闭游标

            # print(j['href'].replace('/', ''))
            # print(j.string)
            # mythread(j.string, j['href']).start()
            # getBookTitle(j.string, j['href'])
        cursor.close()
        # 关闭连接
        conn.close()


# 获取小说的章节
def getBookTitle(id,name, url):
    respone = requests.get(base + url)
    respone.encoding = 'gbk'
    soup = BeautifulSoup(respone.text, 'html.parser')
    all_title = soup.find(id='list').find_all('a')
    print('正在获取' + name)
    print('共' + str(len(all_title)) + '章节')
    conn = pymysql.connect(host='47.93.222.245', user='aqa', password='mysql',
                           db='book', charset='utf8')
    cursor = conn.cursor()
    for i in all_title:
        # print(i['href'])  # 章节链接
        # print(name+''+i.string)  # 章节名字
        try:
            getBookText(cursor,conn,id,name, url ,i.string, i['href'])
        except Exception as e:
            print(e)
    # print(all_title)


# bookname book名 ,titelname 章节名,titleurl 小说名英文  url 章节链接
# 获取小说的正文
def getBookText(cursor,conn,id,bookname,titleurl, titlename, url):
    # print(base + '---' + titleurl + '---' + url)
    respone = requests.get(base + titleurl + url)
    respone.encoding = 'gbk'
    soup = BeautifulSoup(respone.text, 'html.parser')
    content = soup.find('div', class_='content_read').find('div', id='content').text.replace("&nbsp;", "").replace(
        "<br />", "\n")
    openSQL(cursor,conn,bookname, titlename, content, id)
    # 写入txt
    # with open(local + bookname + ".txt", 'a', newline='') as f:
    #     f.write(titlename + '\n')
    #     f.write(content)


def openSQL(cursor,conn,bookname, chapter, info, id):
    sql = "insert into book_info(infoid,id,chapter,info)values (null,%d,'%s','%s')" % (int(id), str(chapter), str(info))
    print(sql)
    cursor.execute(sql)
    conn.commit()



def savebookinfo(type):
    print('读取'+str(type)+'列表')
    conn = pymysql.connect(host='localhost', user='aqa', password='mysql',
                           db='book', charset='utf8')
    cursor = conn.cursor()
    sql = "select * from book_list where type ='%s'"%(type)
    cursor.execute(sql)
    booklist = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    for i in booklist:
        getBookTitle(i[0],i[2],'/'+i[3]+'/')
    # getBookTitle(booklist[0][0],booklist[0][2],'/'+booklist[0][3]+'/')


# 正式
# 小说书名入库
# getBookNameList()
# 小说上传
# 从服务器获取小说列表
typelist=['奇幻、玄幻','武侠、仙侠、修真','言情、都市','历史、军事、穿越','游戏、竞技、网游','异灵、科幻','恐怖、悬疑']
for i in typelist:
    savebookinfo(i)

# mythread('战气凌霄', '/zhanqilingxiao/').start()
# getBookTitle('平天策', '/pingtiance/')
# getBookText()
# 测试 章节
# getBookTitle('幽灵机械', '/youlingjixie/')

# 测试 正文
# getBookText('316章 重启', '/guaiwuleyuan/', '4692488.html')
