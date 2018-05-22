# 下载图片
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

class DownloadImage():

    def __init__(self,imageurl,picurl):
        self.imageurl=imageurl
        self.picurl=picurl

    def getdown(self):
        response = requests.get(self.imageurl + '', headers=ua_headers)
        img = response.content
        with open(self.picurl, 'wb') as f:
            f.write(img)


class DownloadTorrent():

    def __init__(self,torrent,name):
        self.torrent=torrent
        self.name=name

    # def getdown(self):
    #     response = requests.get(self.torrent + '', headers=ua_headers)
    #     img = response.content
    #     with open(self.picurl, 'wb') as f:
    #         f.write(img)