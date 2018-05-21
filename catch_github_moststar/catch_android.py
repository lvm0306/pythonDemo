import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import chardet
import pymysql

baseurl = 'https://github.com/search?l=&p=1&q=stars%3A%3E1000+updated%3A%3E2016-01-01+language%3AJava&ref=advsearch&type=Repositories&utf8=%E2%9C%93'
baseurl_1 = 'https://github.com/search?l=&p='
baseurl_2 = '&q=stars%3A%3E1000+updated%3A%3E2016-01-01+language%3AJava&ref=advsearch&type=Repositories&utf8=%E2%9C%93'
baseurl_3='&q=stars%3A>1000+updated%3A>2016-01-01+language%3AJava&ref=advsearch&type=Repositories&utf8=✓'
base_github = 'https://github.com/'


def getHtmlLibrary(num):
    respone = requests.get(baseurl_1 + str(num) + baseurl_3)
    soup = BeautifulSoup(respone.text, 'html.parser')
    divs = soup.find('div',class_='pl-2').find_all('div', class_='repo-list-item d-flex flex-justify-start py-4 public source')
    library = []
    for i in divs:
        _library = []
        page = i.h3.text
        name = page.replace('\n', '').strip()
        name1 = name.split('/')
        href = base_github + name
        star = i.find(class_='col-2 text-right pt-1 pr-3 pt-2').find('a', class_='muted-link').text.replace('\n','').strip()
        info='暂无详情'
        try:
            info = i.find('p', class_='col-9 d-inline-block text-gray mb-2 pr-4').text.replace('\n', '').strip()
        except Exception as e:
            print(e)
        # 测试代码块
        # print(name1)
        # print(name1[1] + '---' + href + '---' + star)
        finally:
            _library.append(name1[1])
            _library.append(name1[0])
            _library.append(href)
            _library.append(info)
            _library.append('Java')
            _library.append(star)
            print(_library)
            library.append(_library)

    print(library)
    return library


def writeThings(num, library):
    pagenum = '正在写入' + str(num) + '页'
    print(pagenum)
    with open('an' + ".csv", "a+", encoding='gbk', newline="") as f:
        writer = csv.writer(f)
        for i in library:
            try:
                writer.writerow(i)
            except Exception as e:
                print(e.args)


if __name__ == '__main__':
    print('开始')
    for i in range(1, 3):
        library_list = getHtmlLibrary(i)
        writeThings(i, library_list)

    # 测试代码
    # library_list = getHtmlLibrary(9)
    # print(library_list)
    # writeThings(9, library_list)
