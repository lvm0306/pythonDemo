import requests
import re
from bs4 import BeautifulSoup
from struct import *

linkurl = []
baseurl = 'https://www.3344gu.com/'
basetext = 'F:/space/python2/getbug/yellow/yellow_video.txt'


def getmovelist(url):
    data = requests.get(url)
    data.encoding = "utf-8"
    if (data.status_code == 200):
        soup = BeautifulSoup(data.text, "html.parser")
        link = soup.find('ul', class_='news_list')
        all_a = link.find_all('a')
        for a in all_a:
            mylink = baseurl + a.get('href')
            linkurl.append('https://www.3344gu.com/' + a.get('href'))
            try:
                gettorrent(mylink)
            except Exception as e:
                print(e)


def gettorrent(mylink):
    data = requests.get(mylink)
    data.encoding = "utf-8"
    if (data.status_code == 200):
        soup = BeautifulSoup(data.text, "html.parser")
        torrent = soup.find('div', 'news').a.get('href')
        title = soup.find('h1', 'tit1').contents
        print(title)
        print(torrent[36:])

        # url = 'http://www.jandown.com/fetch.php'
        # d = {'code': torrent[36:]}
        # r = requests.post(url, data=d)
        # print(r.content)
        # f = open("F:/space/python2/getbug/yellow/"+torrent[36:39]+".torrent", "wb")
        # # b=bytes.decode(r.content,'gbk')
        # f.write(r.)
        # f.close()
        f = open("F:/space/python2/getbug/yellow/yellow_video.txt", "a+")
        f.write(title[0].string + '\n')
        f.write(torrent + '\n')
        f.close()
        # expandyellow.getHtml(torrent)


getmovelist('https://www.3344gu.com/xiazaiqu/btyazhou/')
for i in range(2, 100):
    print(i)
    getmovelist('https://www.3344gu.com/xiazaiqu/btyazhou/index_' + str(i) + '.html')