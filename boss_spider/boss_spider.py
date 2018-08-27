import csv
import random
import re
import threading
import time

import pymysql
import requests
from bs4 import BeautifulSoup

from util.constant import local_headers
from util.getEncoding import getEncoding

base = 'https://www.zhipin.com/'
test_url = 'https://www.zhipin.com/c101210100-p100202/?ka=sel-city-101210100';
pages_num = []


def test():
    respone = requests.get(test_url, headers=local_headers)
    respone.encoding = getEncoding(test_url).get_encode2()
    soup = BeautifulSoup(respone.text, 'html.parser')
    dls = soup.find(class_='condition-district show-condition-district').find_all('a')
    for d in dls[1:]:
        print(d.string)
        print(base + d['href'] + '?' + d['ka'])
        # print(d)

    lis = soup.find('div', class_='job-list').find_all('li')
    i_ = lis[0]
    # 工作名字 job_name
    job_name = i_.find(class_='job-title').string
    # 公司名字 job_company
    job_company = i_.find(class_='company-text').find('a').string
    # 工作要求 job_require
    job_require = i_.find('div', class_='info-primary').p.text
    # 公司信息 job_company_info
    job_company_info = i_.find('div', class_='company-text').p.text
    # 公司招聘人 job_people
    job_people = i_.find('div', class_='info-publis').h3.text
    # 公司详细网址
    job_link = i_.find('div', class_='info-primary').h3.a['href']
    # 工资
    job_money = i_.find('div', class_='info-primary').h3.find(class_='red').string
    # 工资_下限
    job_min_money = job_money.split('-')[0]
    # 工资_上限
    job_max_money = job_money.split('-')[1]

    # print('工作名字-' + job_name)
    # print('公司名字-' + job_company)
    # print('公司名字-' + job_require)
    # print('公司名字-' + job_company_info)
    # print('公司招聘人-' + job_people)
    # print('公司详细网址-' + job_link)
    # print('工资-' + job_money)
    # print('工资_下限-' + job_min_money)
    # print('工资_上限-' + job_max_money)


# 获取杭州所有地区的地址
# 如果想获取其他地区的地址，更改test_url
def getSpiderUrl():
    respone = requests.get(test_url, headers=local_headers)
    respone.encoding = getEncoding(test_url).get_encode2()
    soup = BeautifulSoup(respone.text, 'html.parser')
    dls = soup.find(class_='condition-district show-condition-district').find_all('a')
    areas = []
    for d in dls[1:]:
        area = []
        area.append(d.string)
        area.append(base + d['href'] + '?' + d['ka'])
        area.append(base + d['href'])
        # print(d.string)
        # print(base+d['href']+'?'+d['ka'])
        areas.append(area)
    return areas


# base=''
# page_url='/c101210100-p100202/b_%E8%A5%BF%E6%B9%96%E5%8C%BA/?page=3'
def getJobInfo(page_url, pages_num, isFirst):
    if pages_num.count(page_url) != 0:
        # 列表中已经含有此列表
        return False

    if isFirst == 1:
        pages_num = []
        url = page_url
    else:
        url = base + page_url + '&ka=page-next'
        pages_num.append(page_url)

    respone = requests.get(url, headers=local_headers)
    respone.encoding = getEncoding(test_url).get_encode2()
    soup = BeautifulSoup(respone.text, 'html.parser')
    # dls = soup.find(class_='condition-district show-condition-district').find_all('a')
    # for d in dls[1:]:
    #     print(d.string)
    #     print(base + d['href'] + '?' + d['ka'])
    #     # print(d)

    lis = soup.find('div', class_='job-list').find_all('li')
    for i_ in lis:
        # i_ = lis[0]
        # 工作名字 job_name
        job_name = i_.find(class_='job-title').string
        # 公司名字 job_company
        job_company = i_.find(class_='company-text').find('a').string
        # 工作要求 job_require
        job_require = i_.find('div', class_='info-primary').p.text
        # 公司信息 job_company_info
        job_company_info = i_.find('div', class_='company-text').p.text
        # 公司招聘人 job_people
        job_people = i_.find('div', class_='info-publis').h3.text
        # 公司详细网址
        job_link = i_.find('div', class_='info-primary').h3.a['href']
        # 工资
        job_money = i_.find('div', class_='info-primary').h3.find(class_='red').string
        # 工资_下限
        job_min_money = job_money.split('-')[0]
        # 工资_上限
        job_max_money = job_money.split('-')[1]

        # print('工作名字-' + job_name)
        # print('公司名字-' + job_company)
        # print('公司名字-' + job_require)
        # print('公司名字-' + job_company_info)
        # print('公司招聘人-' + job_people)
        # print('公司详细网址-' + job_link)
        # print('工资-' + job_money)
        # print('工资_下限-' + job_min_money)
        # print('工资_上限-' + job_max_money)
        print(job_name + page_url)
    # if soup.find('div', class_='page').find_all('a')[-1]['href'] == 'javascript:;':
    #     getJobInfo("",pages_num,3)
    # else:
    getJobInfo(soup.find('div', class_='page').find_all('a')[-1]['href'], pages_num, 2)


if __name__ == '__main__':
    # 第一步获取所有 area 的名字和链接 如 西湖区 https://xxxxx
    # 第二步根据地区地址 获取该地区的招聘信息

    # 第一步
    areas = getSpiderUrl()
    print(areas)
    # 第二步
    for a in areas:
        time.sleep(30)
        try:
            print(a[0])
            getJobInfo(a[1], pages_num, 1)
        except Exception as e:
            print(e)
