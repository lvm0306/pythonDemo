# 下载图片
import csv
import random
import re
import threading

import pymysql
import requests
from bs4 import BeautifulSoup
from util.getEncoding import getEncoding
from util.DownLoadUtils import DownloadImage
ua_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}

def downloadImage(url):
    # response = requests.get(url + '', headers=ua_headers)
    # img = response.content
    # with open('./a.jpg', 'wb') as f:
    #     f.write(img)
    respone=requests.get(url)
    respone.encoding=getEncoding(url).get_encode2()
    soup=BeautifulSoup(respone.text,'html.parser')
    print(soup)


if(__name__=='__main__'):
    # imageurl='http://t1.mmonly.cc/uploads/tu/201805/9999/60ecd968a6.jpg'
    # picurl='./a.jpg'
    # # downloadImage('http://t1.mmonly.cc/uploads/tu/201805/9999/60ecd968a6.jpg')
    # du=DownloadImage(imageurl,picurl)
    # du.getdown()
    downloadImage('http://www.qyl74.com/68646/漂亮情趣黑丝露脸女神发骚勾引男友-直接穿着衣服给操了-1/')