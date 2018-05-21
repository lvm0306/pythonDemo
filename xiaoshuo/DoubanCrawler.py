import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re

# f = open("F:\space\python2\getbug\lwcs.txt", "a+")
list = []
baseurl = 'F:/space/python2/getbug/artical/'


def getTag(url):
    data = requests.get(url)
    data.encoding = "gbk"

    if (data.status_code == 200):
        soup = BeautifulSoup(data.text, "html.parser")
        for link in soup.find(id='list').find_all('a'):
            tempurl = link.get('href')
            texturl = 'http://www.5200xs.org' + tempurl
            list.append('http://www.5200xs.org' + tempurl)
            getInfo(texturl)


def getInfo(texturl):
    data = requests.get(texturl)
    data.encoding = 'gbk'
    if (data.status_code == 200):
        soup = BeautifulSoup(data.text, "html.parser")
        title = soup.select("#wrapper > div.content_read > div > div.bookname > h1")[0].string
        title1 = ''
        for zi in title:
            if (zi != '?'):
                title1 += zi

        title2=title1.replace("斗罗大陆3龙王传说","")
        print(title2)
        f = open(baseurl + title2 + ".txt", "w")
        content = re.findall('<div id="content">(.*?)</div>', data.text, re.S)
        # content = soup.select("#content")
        if content.__len__() > 0 and content.__len__() > 0:
            str = title[0] + "\n\n" + content[0].replace("&nbsp;&nbsp;&nbsp;&nbsp;", "").replace("<br />", "").replace("<br>", "")  # 标题和内容拼在一起
            f.write(str)  # 写入TXT
            f.close()


getTag('http://www.5200xs.org/52002847/')

# print(soup.contents)
# var = soup.find(id='wrapper').find(class_='content_read').find(class_='box_con').find(_class='bookname')
# var=soup.select("#wrapper > div.content_read > div > div.bookname > h1")
# content = re.findall('<div id="content">(.*?)</div>', data.text, re.S)
# war=soup.find(id='wrapper')
# var=soup.select("#content")
# if content.__len__() > 0 and content.__len__() > 0:
#     str = content[0] + "\n\n" + content[0].replace("&nbsp;&nbsp;&nbsp;&nbsp;", "").replace("<br />", "")  # 标题和内容拼在一起
#     f.write(str)  # 写入TXT
# print(content)
# title = re.findall('<h1>(.*?)</h1>', data.text, re.S)
# print(title)
