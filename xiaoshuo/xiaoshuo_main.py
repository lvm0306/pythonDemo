import requests
from bs4 import BeautifulSoup
mbaseurl = 'http://zhannei.baidu.com/cse/search?q='
mbody = '&click=1&s=3505380840816237522'


def inputName():
    str = input("请输入想看小说的名字：\n");
    url = mbaseurl + str + mbody
    print(url)
    return url


def getList(url):
    data = requests.get(url)
    data.encoding = "utf-8"
    if(data.status_code==200):
        xiaoshuolist=BeautifulSoup(data.text,'html.parser').find('div',class_='result-list').find_all('div')
        for xiaoshuo in xiaoshuolist:
            name=xiaoshuo.find('a',class_='result-game-item-title-link')
            xiaoshuo.find()
            # title=name.get('href')
            print(name)


getList(inputName())
