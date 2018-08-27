# coding:utf-8
import csv
import email
import random
import re
import threading
import time

import pymysql
import requests
from bs4 import BeautifulSoup

from util.constant import local_headers
from util.getEncoding import getEncoding

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

# my_sender = '18545156106@163.com'
# my_user = ['842463468@qq.com']
# password='z55510535'

from_addr =  '18545156106@163.com'
password = 'shi123456'
password1 = 'vbvibmgsqmfxbdeg'
# 输入SMTP服务器地址:18545156106
smtp_server = 'smtp.163.com'
smtp_server1 = 'smtp.qq.com'
# 输入收件人地址:
to_addr = 'ivm0306@163.com'

msg = MIMEText('对不起 我爱你', 'plain', 'utf-8')
msg['From'] ="18545156106@163.com"
msg['To'] = "ivm0306@163.com"
msg['Subject'] = "this is my love for you "

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()