from biquge.BookName import BookName
import csv
import random
import re
import threading

import pymysql
import requests
from bs4 import BeautifulSoup

from util.constant import local_headers
from util.getEncoding import getEncoding

base = "https://www.qu.la/wanbenxiaoshuo/"


def bookSpider():
    BookName().titleSpider()


if __name__=="__main__":
    bookSpider()