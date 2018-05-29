import pymysql
import requests
from bs4 import BeautifulSoup

from util.constant import local_headers
from util.getEncoding import getEncoding

base_book = 'https://www.qu.la'
base = "https://www.qu.la/wanbenxiaoshuo/"
ids = ['con_o1g_1', 'con_o2g_1', 'con_o3g_1', 'con_o4g_1', 'con_o5g_1', 'con_o6g_1', 'con_o7g_1', 'con_hng_1']
types = ['玄幻奇幻排行', '武侠仙侠排行', '都市言情排行', '历史军事排行', '科幻灵异排行', '网游竞技排行', '女生频道排行', '完本小说总排行']


class BookName():
    def __init__(self):
        print()

    def startSpider(self):
        conn = pymysql.connect(host='localhost', user='root', password='',
                               db='biquge', charset='utf8')
        cursor = conn.cursor()
        respone = requests.get(base, headers=local_headers)
        respone.encoding = getEncoding(base).get_encode2()
        soup = BeautifulSoup(respone.text, 'html.parser')
        for i in ids:
            # 大分类
            print(types[ids.index(i)])
            title_type = types[ids.index(i)]
            lis = soup.find(id=i).find_all('li')
            for j in lis:
                # 小分类
                print(j.a['title'])
                print(j.a['href'])
                sql = "insert into bqg_list(id, type, name, book_link)values (null,'%s','%s','%s')" % (
                    title_type, j.a['title'], j.a['href'])
                cursor.execute(sql)
                conn.commit()

        cursor.close()
        conn.close()

    def titleSpider(self):

        conn = pymysql.connect(host='localhost', user='root', password='',
                               db='biquge', charset='utf8')
        cursor = conn.cursor()

        # sql = "select * from bqg_list"
        # cursor.execute(sql)
        # books = cursor.fetchall()
        # print(books)
        books=((99, '女生频道排行', '俏汉宠农妻：这个娘子好辣', '/book/42186/'), (100, '女生频道排行', '重生七十年代：军嫂，有点田', '/book/60629/'), (101, '女生频道排行', '绝宠妖妃：邪王，太闷骚！', '/book/28906/'), (102, '女生频道排行', '鬼帝狂妻：纨绔大小姐', '/book/40082/'), (103, '女生频道排行', '帝国总裁，宠翻天！', '/book/42973/'), (104, '女生频道排行', '萌宝来袭：总裁爹地，太给力！', '/book/45213/'), (105, '女生频道排行', '空间重生：盛宠神医商女', '/book/34335/'), (106, '完本小说总排行', '太古神王', '/book/4140/'), (107, '完本小说总排行', '大主宰', '/book/176/'), (108, '完本小说总排行', '雪鹰领主', '/book/5094/'), (109, '完本小说总排行', '择天记', '/book/168/'), (110, '完本小说总排行', '全职高手', '/book/32/'), (111, '完本小说总排行', '完美世界', '/book/14/'), (112, '完本小说总排行', '遮天', '/book/394/'), (113, '完本小说总排行', '逍遥小书生', '/book/23934/'), (114, '完本小说总排行', '绝世武神', '/book/322/'), (115, '完本小说总排行', '异世灵武天下', '/book/199/'), (116, '完本小说总排行', '不朽凡人', '/book/18049/'), (117, '完本小说总排行', '掠天记', '/book/4295/'), (118, '完本小说总排行', '最强兵王', '/book/4511/'), (119, '完本小说总排行', '都市无上仙医', '/book/3802/'), (120, '完本小说总排行', '斗破苍穹', '/book/390/'))

        for book in books:
            print("当前是：" + book[2])
            respone = requests.get(base_book + book[3], headers=local_headers)
            respone.encoding = getEncoding(base_book + book[3]).get_encode2()
            soup = BeautifulSoup(respone.text, "html.parser")
            dds = soup.find(id='list').find_all('dd')
            for i in dds:
                try:
                    zu = i.find('a')['href'].split('/')
                    if (len(zu) < 2):
                        print("排除" + i.a['href'])
                    else:
                        print("当前是第" + i.find('a').string)
                        title= i.find('a').string.replace('\\',"")
                        sql = "insert into bqg_chapter(chapterid ,id, name, chapter,chapter_link)values (null,%d,'%s','%s','%s')" % (
                            book[0], book[2],title, i.find('a')['href'])
                        cursor.execute(sql)
                        conn.commit()
                except Exception as e:
                    print(e)
        cursor.close()
        conn.close()
