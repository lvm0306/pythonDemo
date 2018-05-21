import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import chardet
import pymysql

base_url = 'https://github.com/lvm0306?page=18&tab=stars'
github_url = 'https://github.com'
base_bianma = ''
my_name = 'lvm0306'
my_friend = []
getSQL = []


class Libarty():

    def __init__(self, name, author, href, info, yuyan, star):
        self.name = name  # 库名字
        self.author = author  # 链接
        self.href = href  # 链接
        self.info = info  # 详情
        self.yuyan = yuyan  # 语言
        self.star = star  # 星星


def getTitle(num, name):
    if num == 1:
        respone = requests.get(github_url + name + '?&tab=stars')
    else:
        respone = requests.get(github_url + name + '?page=' + str(num) + '&tab=stars')
    base_bianma = chardet.detect(respone.content)
    # coding = chardet.detect(respone.content)
    # print(base_bianma)
    # print(respone.encoding)
    respone.encoding = chardet.detect(respone.content)
    soup = BeautifulSoup(respone.text, 'html.parser')
    divs = soup.find_all('div', class_='col-12 d-block width-full py-4 border-bottom')
    library = []
    for div in divs:
        # 名字
        name = div.find_all('h3')[0].find('a')['href'].split('/')[2]
        # 作者
        author = div.find_all('h3')[0].find('a')['href'].split('/')[1]
        # 链接
        href = github_url + div.find_all('h3')[0].find('a')['href']
        # 详情
        info = ' '
        yuyan = ' '
        try:
            info = div.find(class_='py-1').p.string.strip()
            # info = ''
            # 语言
            # yuyan = ''
            yuyan = div.find(class_='mr-3').string.strip()
        except Exception:
            continue
        # Star数
        star = div.find('a', class_='muted-link mr-3').text.strip()
        # 最后更新的日期
        updata = div.find('relative-time').text
        list = []
        list.append(name)
        list.append(author)
        list.append(href)
        list.append(info)
        list.append(yuyan)
        list.append(star)
        list.append(updata)
        library.append(list)
    # for i in library:
    #     print(i)
    return library


def writeThings(num, library, name):
    pagenum = '正在写入' + name + '的第' + str(num) + '页'
    print(pagenum)
    page = []
    page.append(pagenum)
    with open(name.replace('/', '') + ".csv", "a+", encoding='gbk', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(page)
        for i in library:
            try:
                writer.writerow(i)
            except Exception as e:
                print(e.args)


def saveOne(cursor, name, author, href, info, yuyan, star):
    # conn = pymysql.connect(host='localhost', user='root', password='',
    #                        db='tmp', charset='utf8')
    #
    # # conn = pymysql.connect("localhost","root","z55510535","test" )
    # # 创建游标
    # cursor = conn.cursor()

    # 执行SQL，并返回收影响行数
    # effect_row = cursor.execute("select * from tb7")

    # 执行SQL，并返回受影响行数
    # effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))

    # 执行SQL，并返回受影响行数,执行多次
    # effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])

    # cursor.execute(
    #     "insert into github values (null,'" + name + "','" + author + "','" + href + "','" + info + "','" + yuyan + "','" + star + "','" + updata + "')")
    star_ = star.replace(',', '')
    info_ = info.replace('\'', '。')
    name_ = name.replace('\'', '。')
    author_ = author.replace('\'', '。')
    sql = "insert into github(id,name,author,href,info,yuyan,star)values(null,'%s','%s','%s','%s','%s',%d)" % (
        name_, author_, href, info_, yuyan, int(star_))
    # sql = "insert into github(id,name,author,href,info,yuyan,star)values(null,{},{},{},{},{},{})".format(name,author,href,info,yuyan,star)
    print(sql)
    cursor.execute(sql)
    # # 提交，不然无法保存新建或者修改的数据
    # conn.commit()
    #
    # # 关闭游标
    # cursor.close()
    # # 关闭连接
    # conn.close()


def openSQL(library, name, page):
    print('正在录入' + name + '的第' + str(page) + '页')
    conn = pymysql.connect(host='localhost', user='root', password='',
                           db='github', charset='utf8')
    cursor = conn.cursor()
    for i in library:
        saveOne(cursor, i[0], i[1], i[2], i[3], i[4], i[5])

    conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    print('录入成功')


# 获取我的关注朋友 <30
def getMyFriend_list():
    respone = requests.get(github_url + '/' + my_name + '?tab=following')
    respone.encoding = 'gbk'
    soup = BeautifulSoup(respone.text, 'html.parser')
    all_a = soup.find_all('a', class_='d-inline-block no-underline mb-1')
    for a in all_a:
        my_friend.append(a['href'])

    print('我的关注好友已经获取\n')
    print('共' + str(len(my_friend)) + '个关注好友')


# 获取朋友的页码
def getMyFriend_library_page(name):
    respone = requests.get(github_url + '/' + name + '?tab=stars')
    respone.encoding = 'gbk'
    soup = BeautifulSoup(respone.text, 'html.parser')
    try:
        all_a = soup.find('div', class_='pagination').find_all('a')
        print(name + '已经关注了' + str(all_a[len(all_a) - 2].string) + '页库')
        return int(all_a[len(all_a) - 2].string)
    except Exception as e:
        print(e)
        return 1


# 获取我关注朋友的收藏库
def getMyFriend_library(name):
    # 1.获取朋友的收藏页数
    m_page = getMyFriend_library_page(name);
    for i in range(1, m_page + 1):
        # 2.获取库
        print('正在获取' + name + '第' + str(i) + '库')
        library = getTitle(i, name)
        writeThings(i, library, name)
        try:
            openSQL(library, name, i)
        except Exception as e:
            print(e)
            continue


# 读数据库
def readSQL():
    conn = pymysql.connect(host='localhost', user='root', password='',
                           db='github', charset='utf8')
    cursor = conn.cursor()
    sql = 'select name,info,href,star from github where yuyan=\'Java\''
    # sql = "insert into github(id,name,author,href,info,yuyan,star)values(null,{},{},{},{},{},{})".format(name,author,href,info,yuyan,star)
    print(sql)
    cursor.execute(sql)
    get = list(cursor.fetchall())
    conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    print('读取成功')
    return get


if __name__ == '__main__':
    # 获取我的好友
    # getMyFriend_list()
    # my_friend.pop(0)
    # my_friend.pop(0)
    # my_friend.pop(0)
    # for i in my_friend:
    #     getMyFriend_library(i)
    # getMyFriend_library(my_friend[2])

    # 将数据库文件写成md
    # getSQL = readSQL()
    # with open('library' + '.md', 'a', newline='') as f:
    #     for i in getSQL:
    #         f.write('[' + i[0] + ']' + '(' + i[2] + ')' + '\n' + i[1]+'\n')
    # f.close()

    print("")
