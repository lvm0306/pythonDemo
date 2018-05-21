import requests
import re
from bs4 import BeautifulSoup

linkurl = []
baseurl = 'https://www.3344gu.com/'


def getBasePic(url):
    data = requests.get(url)
    data.encoding = "utf-8"
    if (data.status_code == 200):
        soup = BeautifulSoup(data.text, "html.parser")
        # print(soup.select('body > div:nth-child(6) > ul'))
        link = soup.find('ul', class_='news_list')
        all_a = link.find_all('a')
        for a in all_a:
            mylink = baseurl + a.get('href')
            print(mylink)
            linkurl.append('https://www.3344gu.com/' + a.get('href'))
            getPicList(mylink)


def getPicList(linkurl):
    data = requests.get(linkurl)
    data.encoding = "utf-8"
    if data.status_code == 200:
        soup = BeautifulSoup(data.text, 'html.parser')
        title = soup.find('h1', 'tit1')
        print(title.contents)
        print(type(title.contents))
        pic_div = soup.find('div', class_='news').find_all('img')

        f = open("F:/space/python2/getbug/yellow/yellow.txt", "a+")
        f.write(title.contents[0] + '\n')
        f.close()
        for pic in pic_div:
            print(pic.get('src'))
            print(type(pic.get('src')))
            f = open("F:/space/python2/getbug/yellow/yellow.txt", "a+")
            f.write(pic.get('src') + '  \n')  # 写入TXT
            f.close()


getBasePic('https://www.3344gu.com/tupianqu/yazhou/')
