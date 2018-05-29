import csv
import re
import threading

import pymysql
import requests
from bs4 import BeautifulSoup

from util.constant import local_headers
from util.getEncoding import getEncoding

def bookInfo():
    print()
    respone=requests.get("https://www.qu.la/book/4140/2585313.html",headers=local_headers)
    respone.encoding=getEncoding("https://www.qu.la/book/4140/2585313.html").get_encode2()
    soup=BeautifulSoup(respone.text,"html.parser")
    text=soup.find(id="content").text.replace("&nbsp;", "").replace("<br />", "\n")
    print(text)


if __name__=="__main__":
    bookInfo()