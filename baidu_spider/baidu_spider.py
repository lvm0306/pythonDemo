
from bs4 import BeautifulSoup
import urllib
import requests
import re
import csv
import random
import re
import threading

import logging
import pymysql
import requests
from bs4 import BeautifulSoup

from util.constant import local_headers
from util.getEncoding import getEncoding

adr =[]

''''对搜素资源名字进行url编码'''
# search_text =raw_input('请输入搜索资源名：')
#
# search_text = search_text.decode('gbk')
# search_text = search_text.encode('utf-8')
# search_text ="变形金刚"
# search_text = urllib.quote(search_text)


''''获取文件地址'''
# home = urllib.urlopen('http://www.panduoduo.net/s/name/'+"变形金刚")


'''获取百度云地址'''
def getbaidu(adr):
  for i in adr:
    respone = requests.get('http://www.panduoduo.net'+i, headers=local_headers)
    respone.encoding = getEncoding('http://www.panduoduo.net'+i).get_encode2()
    # url = urllib.urlopen('http://www.panduoduo.net'+i)
    bs = BeautifulSoup(respone.text,'html.parser')
    bs1 = bs.select('.dbutton2')
    href = re.compile('http\%(\%|\d|\w|\/\/|\/|\.)*')
    b = href.search(str(bs1))
    name = str(bs.select('.center')).decode('utf-8')
    text1 = re.compile('\<h1\sclass\=\"center"\>[\d|\w|\D|\W]*\</h1\>')
    text2 = text1.search(name)
    rag1 = re.compile('\>[\d|\w|\D|\W]*\<')
    if text2:
      text3 = rag1.search(text2.group())
      if text3:
        print (text3.group())
    if b:
      text = urllib.unquote(str(b.group())).decode('utf-8')
      print (text)

'''初始化'''
def init(adr):
  test_url='http://www.panduoduo.net/s/name/'+"变形金刚"
  respone = requests.get(test_url, headers=local_headers)
  respone.encoding = getEncoding(test_url).get_encode2()
  soup = BeautifulSoup(respone.text,'html.parser')
  soup = soup.select('.row')
  pattern = re.compile('\/r\/\d+')
  for i in soup:
    i = str(i)
    adress = pattern.search(i)
    adress = adress.group()
    adr.append(adress)


print ('running---------'    )
init(adr)
getbaidu(adr)