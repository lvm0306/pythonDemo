import csv
import random
import re
import threading

import pymysql
import requests
from bs4 import BeautifulSoup
import time
import datetime

from util.constant import local_headers
from util.getEncoding import getEncoding

vage_='黄瓜,茄子,柿子,尖椒,菠菜,韭菜,香菜,芹菜,白菜,头菜,土豆,干豆腐,大葱,油麦菜,生菜,香葱,鲜蘑,肥羊粉,内酯豆腐,金针磨,杏鲍菇,白玉菇,香菇,蚕蛹,娃娃菜,蚕蛹,娃娃菜,西兰花,圆葱,小白菜,紫圆葱,胡萝卜,去皮蒜,西葫芦,青椒,甘蓝,有机菜花,鹌鹑蛋,西生菜,油菜,豆角,泰椒,冬瓜,鲜姜,心里美,红尖椒,豇豆角,豆青,菜心,老黄瓜,蒜苔,绿萝卜,红萝卜,白萝卜,水晶粉,海带根,芥菜丝,苦苣,地瓜,蒜苗,青笋,芥兰,山药,紫甘蓝,绿窝瓜,花生,毛豆,茴香'
vage=['黄瓜', '茄子', '柿子', '尖椒', '菠菜', '韭菜', '香菜', '芹菜', '白菜', '头菜', '土豆', '干豆腐','干豆腐丝','大豆腐','拉皮', '松花蛋','鸡蛋','大葱', '油麦菜', '生菜', '香葱', '鲜蘑', '肥羊粉', '内酯豆腐', '金针磨', '杏鲍菇', '白玉菇', '香菇', '蚕蛹', '娃娃菜', '西兰花', '圆葱', '小白菜', '紫圆葱', '胡萝卜', '去皮蒜','带皮蒜', '西葫芦', '青椒', '甘蓝', '有机菜花', '鹌鹑蛋', '西生菜', '油菜', '豆角', '泰椒', '冬瓜', '鲜姜', '心里美', '红尖椒', '豇豆角','架豆王','油豆角', '豆青','菜心', '老黄瓜', '蒜苔', '绿萝卜', '红萝卜', '白萝卜', '水晶粉丝','龙口粉丝', '绿豆芽','黄长芽','海带根', '海带丝','芥菜丝', '苦苣', '地瓜', '蒜苗', '青笋', '苦菊','芥兰', '山药', '紫甘蓝', '黄窝瓜', '绿窝瓜', '花生','花生米', '毛豆', '茴香','里脊肉']
fruit_='西瓜,橙子,油桃,蜜桔,巨丰,荔枝,富士苹果,小蜜蜂,草莓,花牛苹果,猕猴桃,桃子,水晶梨,柚子,火龙果,香蕉,樱桃,南果梨,沙白瓜,小柿子,芦橘,香瓜,葡萄,砂糖桔,哈密瓜,山竹'
fruit=['西瓜', '橙子', '油桃', '蜜桔', '巨丰', '荔枝', '富士苹果', '小蜜蜂', '草莓', '花牛苹果', '猕猴桃', '桃子', '水晶梨', '柚子', '火龙果', '香蕉', '樱桃', '南果梨', '沙白瓜', '小柿子', '芦橘', '香瓜', '葡萄', '砂糖桔', '哈密瓜', '山竹']
def saveVT(vt):
    conn = pymysql.connect(host='localhost', user='root', password='',db='biquge', charset='utf8')
    cursor = conn.cursor()
    sql="INSERT INTO `fruit_shop`.`vegetables`(`vid`,`vname`,`fruit`,`seasonal`,`mlt`,`sk`,`bz`) VALUES (null,'%s',1,1,0,0,0)"%(vt)
    cursor.execute(sql)
    conn.commit()
def savefruit(vt):
    conn = pymysql.connect(host='localhost', user='root', password='',db='biquge', charset='utf8')
    cursor = conn.cursor()
    sql="INSERT INTO `fruit_shop`.`vegetables`(`vid`,`vname`,`fruit`,`seasonal`,`mlt`,`sk`,`bz`) VALUES (null,'%s',0,1,0,0,0)"%(vt)
    cursor.execute(sql)
    conn.commit()
def alterString(s):
    return s;

# save()
# print(int(time.time()))
# for i in fruit:
#     savefruit(i)


list_v=[]
for i in vage:
    list_v.append("INSERT INTO `fruit_shop`.`vegetables`(`vid`,`vname`,`fruit`,`seasonal`,`mlt`,`sk`,`bz`,`kr`,`cb`) VALUES (null,'%s',0,1,0,0,0,0,0)"%i)

for i in list_v:
    print(i)
