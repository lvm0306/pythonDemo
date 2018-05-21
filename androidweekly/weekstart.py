import csv
import re
import threading

import requests
from bs4 import BeautifulSoup

baseurl='http://androidweekly.net/issues/issue-'
def getPage(num):
    respone = requests.get(baseurl+str(num))
    respone.encoding = 'gbk'
    soup = BeautifulSoup(respone.text, 'html.parser')
    a_all=soup.find_all('table',class_='wrapper')
    for a in a_all:
        print(a)

    return

getPage(198)