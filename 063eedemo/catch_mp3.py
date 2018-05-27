import csv
import random
import re
import threading

import pymysql
import requests
from bs4 import BeautifulSoup

from util.constant import local_headers
from util.getEncoding import getEncoding

base1 = "https://www.063ee.com/htm/index.htm"


# 获取连接
def getMp3Link():
    respone = requests.get(base1, headers=local_headers)
    respone.encoding=getEncoding.get_encode2()


if __name__ == "__main__":
    getMp3Link()
