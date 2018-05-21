import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import csv

# 完成任务1	实现函数getMovieUrl
# 完成任务2	通过 URL 获得豆瓣电影页面的 HTML
# 完成任务3	定义电影类，并实现其构造函数
# 完成任务4	通过类型和地区构造URL，并获取对应的HTML。解析 HTML 中的每个电影元素，并构造电影对象列表
# 完成任务5	将电影信息输出到 movies.csv。 包含类别、地区以及对应的电影信息
# 完成任务6	将电影的统计结果输出到 output.txt。包含你选取的每个电影类别中，数量排名前三的地区有哪些，分别占此类别电影总数的百分比为多少。

# 完成任务1	实现函数getMovieUrl
def getMovieUrl(category, location):
    """
    return a string corresponding to the URL of douban movie lists given category and location.
    """
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{},{}".format(category, location)
    return url


# 任务2	通过 URL 获得豆瓣电影页面的 HTML
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


# 任务3	定义电影类，并实现其构造函数
class Movie:
    """docstring for Movie."""

    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link

    def print_data(self):
        return "{},{},{},{},{},{}".format(self.name, self.rate, self.location, self.category, self.info_link,
                                          self.cover_link)


# 任务4	通过类型和地区构造URL，并获取对应的HTML。解析 HTML 中的每个电影元素，并构造电影对象列表
def getMovies(category, location):
    """
    return a list of Movie objects with the given category and location.
    """
    movies = []
    html = getHtml(getMovieUrl(category, location), True)
    # html = getMovieHtml(category, location)
    soup = BeautifulSoup(html, 'html.parser')
    content_a = soup.find(id='content').find(class_='list-wp').find_all('a', recursive=False)
    for element in content_a:
        M_name = element.find(class_='title').string
        M_rate = element.find(class_='rate').string
        M_location = location
        M_category = category
        M_info_link = element.get('href')
        M_cover_link = element.find('img').get('src')
        movies.append(Movie(M_name, M_rate, M_location, M_category, M_info_link, M_cover_link).print_data())
    return movies

# 任务5	将电影信息输出到 movies.csv。 包含类别、地区以及对应的电影信息
category_collection = ['黑色幽默', '悬疑', '传记']
location_collection = ['中国大陆','美国','香港','台湾','日本','韩国','英国','法国','德国','意大利','西班牙','印度','泰国','俄罗斯','伊朗','加拿大','澳大利亚','爱尔兰','瑞典','巴西','丹麦']
for location in location_collection:
    for category in category_collection:
        favorite_list1 = getMovies(category, location)
        with open("movies.csv", "w", encoding='utf-8-sig', newline="") as f:
            writer = csv.writer(f)
            for i in favorite_list1:
                writer.writerow(i)

# 完成任务6	将电影的统计结果输出到 output.txt。包含你选取的每个电影类别中，数量排名前三的地区有哪些，分别占此类别电影总数的百分比为多少。
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