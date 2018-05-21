import requests
import re
from bs4 import BeautifulSoup

baseurl = 'https://www.gavbus516.com'


def geturlinfo(url):
    info_respone=requests.get(url)
    info_soup=BeautifulSoup(info_respone.text,'html.parser')
    info=info_soup.select('#magnet-table > tbody > tr:nth-of-type(2) > td:nth-of-type(1)')
    print(info)
    # manger=info_soup.find(id='magnet-table')
    # print(manger)
    # a=manger.find('a')
    # print(a)


respone = requests.get('https://www.gavbus516.com/')
soup = BeautifulSoup(respone.text, 'html.parser')
content = soup.find(id='waterfall');
con = content.findAll('a')
geturlinfo(baseurl+con[0]['href'])
# for c in con:
#     nexturl=baseurl+c['href']
#     geturlinfo(nexturl)
