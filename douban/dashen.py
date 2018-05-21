# coding=utf-8
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv


# 定义电影类*************************************************
class Movie():
    """
    描述电影类
    包含以下成员变量
    电影名称 电影评分 电影类型 电影地区 电影页面链接 电影海报图片链接
    """

    def __init__(self, movie_name, movie_douban_rate,
                 movie_location, movie_category,
                 movie_douban_info_link, movie_douban_cover_link):
        self.name = movie_name  # 电影名称
        self.rate = movie_douban_rate  # 电影评分
        self.location = movie_location  # 电影类型
        self.category = movie_category  # 电影地区
        self.info_link = movie_douban_info_link  # 电影页面链接
        self.cover_link = movie_douban_cover_link  # 电影海报图片链接


# 定义电影类-结束****************************************************

# 扩展豆瓣页面程序段***********************************
"""
url: the douban page we will get html from
loadmore: whether or not click load more on the bottom 
waittime: seconds the broswer will wait after intial load and 
"""


def getHtml(url, loadmore=True, waittime=2):
    browser = webdriver.Chrome('chromedriver')
    browser.get(url)
    time.sleep(waittime)
    if loadmore:
        while True:
            try:
                next_button = browser.find_element_by_class_name("more")
                next_button.click()
                time.sleep(waittime)
            except:
                break
    html = browser.page_source
    browser.quit()
    return html


# 扩展豆瓣页面程序段-结束***********************************

# 获得地区列表(来自审阅者的建议)*******************************************
def get_Location(url):
    douban_html = getHtml(url, False, waittime=20)
    soup = BeautifulSoup(douban_html, 'html.parser')
    locationList = []
    for child in soup.find(class_='tags').find(class_='category').next_sibling.next_sibling:
        location = child.find(class_='tag').get_text()
        if location != '全部地区':
            locationList.append(location)
    return locationList


# 获得地区列表-结束*******************************************

# 获得指定category和location的豆瓣url页面*****************************
def getMovieUrl(category, location):
    """
    input the category and location with chinese
    ouput the complete url of that category and location
    """
    doubanUrl = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"
    url = doubanUrl + ',' + category + ',' + location
    return url


# 获得指定category和location的豆瓣url页面-结束***********************

# 获得豆瓣电影信息***************************************************
def getMovies(category, location):
    """
    通过输入的category与location，获得指定页面
    将页面上所有电影用Movie class标准化，获得目标列表
    """
    # 1 获得指定页面，Soup化
    douban_url_cl = getMovieUrl(category, location)
    douban_html = getHtml(douban_url_cl, waittime=20)
    douban_soup = BeautifulSoup(douban_html, 'html.parser')
    # 2 提取每一部电影
    content_div = douban_soup.find(class_="list-wp")
    output_list = []  # 当没有电影时，返回空列表
    for movie in content_div.find_all('a', recursive=False):
        name = movie.find(class_='title').string
        rate = movie.find(class_='rate').string
        info_link = movie['href']
        cover_link = movie.find(class_='pic').img['src']
        movie_class = Movie(name, rate, location, category, info_link, cover_link)
        output_list.append(movie_class)

    return output_list


# 获得豆瓣电影信息-结束***************************************************

# 生成movie.csv*********************************************************
def ouput_movie_csv(category_list, location_list):
    for category in category_list:
        for location in location_list:
            list_movie = getMovies(category, location)
            with open("movies.csv", 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for movie in list_movie:
                    writein_list = [movie.name, movie.rate, location, category,
                                    movie.info_link, movie.cover_link]
                    writer.writerow(writein_list)
                csvfile.close()
    return


# 生成movie.csv-结束*********************************************************

# 读入csv文件，输出output.txt******************************************
def make_output_txt(csv_name):
    """读入csv文件，输出output.txt"""
    # 0.读取csv文件
    with open('movies.csv', 'r') as f:
        reader = csv.reader(f)
        movies = list(reader)
    # 1.生成二级字典：{类型：{国家：次数}}
    movie_dic = {}
    for item in movies:
        if item[3] not in movie_dic:
            movie_dic[item[3]] = {item[2]: 1}
        else:
            if item[2] in movie_dic[item[3]]:
                movie_dic[item[3]][item[2]] += 1
            else:
                movie_dic[item[3]][item[2]] = 1

    # 2.汇总为一个列表
    # 列表格式：
    # [(类型1)[[占比1，[占比1国家列表]],[占比2,[占比2国家列表]],[占比3,[占比3国家列表]]],
    # (类型2)[[占比1，[占比1国家列表]],[占比2,[占比2国家列表]],[占比3,[占比3国家列表]]],
    # (类型3)[[占比1，[占比1国家列表]],[占比2,[占比2国家列表]],[占比3,[占比3国家列表]]]]

    cate = list(movie_dic.keys())
    num_and_con = list(movie_dic.values())
    con_and_per = []
    for small_dic in num_and_con:
        """列表第一级，每个类型的总表"""
        con = list(small_dic.keys())
        num = list(small_dic.values())

        # 形成[(国家，数量)]列表，并以数目从大到小排序
        zip_Con_and_Num = zip(con, num)
        sort_Con_Num = sorted(zip_Con_and_Num, key=lambda ConNum: ConNum[1], reverse=True)

        total_num = sum(num)
        cate_list = []

        while (len(cate_list) < 3 and len(sort_Con_Num) > 0):
            """列表第二级，[占比*，[国家列表]"""
            small_per_con = []  # [数量，[国家列表]]
            con_list = []  # [国家列表]
            small_per_con.append(sort_Con_Num[0][1])  # 填入数量
            con_list.append(sort_Con_Num[0][0])  # 填入第一个国家
            sort_Con_Num.pop(0)  # 将已经填入(国家，数量)的从排序表中踢出
            for con_num in sort_Con_Num:
                """列表第三级，[国家列表]"""
                if con_num[1] == small_per_con[0]:
                    # 数量相等，国家填入[国家列表],这一项踢出
                    con_list.append(con_num[0])
                    sort_Con_Num.remove(con_num)
                else:
                    # 数量不等，退出循环，找下一项
                    break
            small_per_con.append(con_list)  # 填入[国家列表]
            small_per_con[0] /= 1.0 * total_num  # 数量化为占比
            cate_list.append(small_per_con)

        con_and_per.append(cate_list)

        # 3.输出为output.txt，格式为
    """
    当类型为 ** 时：
    第*名：国家是*，百分比是*...
    """
    str1 = "当类型为 *{}* 时：\n"
    str2 = "第{}名："
    str3 = "国家是{}，百分比是{:.2%}\n"
    str4 = "没有第{}名的国家\n"
    with open('output.txt', 'w', encoding='utf-8') as f:
        for i in range(len(cate)):
            f.write(str1.format(cate[i]))  # 写类型
            num = len(con_and_per[i])
            for j in range(num):  # 写排名，占比，国家
                f.write(str2.format(j + 1) +
                        str3.format(con_and_per[i][j][1], con_and_per[i][j][0]))
            if num < 3:
                for j in range(3 - num):
                    f.write(str4.format(j + 1 + num))
            f.write('\n')
    return


# 读入csv文件，输出output.txt-结束******************************************


# ***********************主程序部分**************************************
# 类型列表
category_list = ["黑色幽默", '情色', '恐怖']
# 地区列表
doubanUrl = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"
location_list = get_Location(doubanUrl)

# 生成movie.csv
ouput_movie_csv(category_list, location_list)
# 导入movie.csv，生成对应的output.txt
make_output_txt('movies.csv')

# **********************主程序部分-结束**************************************