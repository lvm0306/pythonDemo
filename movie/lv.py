# coding=utf-8
import chardet as chardet
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import csv
import re
# 6v电影小试身手
baseurl = 'http://www.6vhao.tv/dy2/index_'


def get6vtext(url):
    respone = requests.get('http://www.6vhao.tv/')
    soup = BeautifulSoup(respone.text, 'html.parser')
    # print(soup)
    result = soup.select('body > div:nth-of-type(4) > div.tjlist > ul > li:nth-of-type(1) > a')
    # print(result[0]['href'])
    infohtml = requests.get('http://www.6vhao.tv/dy6/2018-03-16/33676.html')
    info_soup = BeautifulSoup(infohtml.text, 'html.parser')

    info_soup.encoding = "gbk"
    # print(info_soup)
    text = info_soup.find(id='text').find_all('a')
    for t in text:
        print(t['href'])


def get6vmovie_url(pagenum):
    respone = requests.get(baseurl + str(pagenum) + '.html')
    url_soup = BeautifulSoup(respone.text, 'html.parser')

    # url_soup.decode("GB2312").encode("UTF-8")
    movie_div = url_soup.find_all(class_='listBox')[0].ul
    list_a = movie_div.find_all(class_='listimg')
    import chardet
    # print(movie_div.find_all(class_='listimg'))
    for i in list_a:
        movie_url = i.a['href']
        print(movie_url)
        getmovie_info(movie_url)


def getmovie_info(url):
    moview = []
    infohtml = requests.get(url)
    # code=get_encodings_from_content(infohtml.text)
    # print(code)
    info_soup = BeautifulSoup(infohtml.text, 'html.parser')
    info_soup.encode('gb2312')
    info_title_div = info_soup.find(class_='contentinfo')
    into_title = info_title_div.h1.a
    title = into_title.string
    print(title)
    moview.append(title)
    text = info_soup.find(id='text').find_all('a')
    for t in text:
        print(t['href'])
        moview.append(t['href'])

        with open("movies.csv", "w", encoding='utf-8-sig', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(moview)
            f.close()


def get_encodings_from_content(content):
    charset_re = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
    pragma_re = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
    xml_re = re.compile(r'^<\?xml.*?encoding=["\']*(.+?)["\'>]')

    return (charset_re.findall(content) +
            pragma_re.findall(content) +
            xml_re.findall(content))


for i in range(2, 10):
    get6vmovie_url(i)
    print(i)
