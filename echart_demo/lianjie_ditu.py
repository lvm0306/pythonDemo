import pymysql

conn = pymysql.connect(host='localhost', user='root', password='',
                       db='lianjia', charset='utf8')
cursor = conn.cursor()

# sql = "insert into city_list(id, city_name, city_link)values (null,'%s','%s')"
# sql = "select * from city_room_list where city_name = '杭州'"
sql = "select distinct city_area from city_room_list where city_name = '杭州'"
# print(sql)
cursor.execute(sql)
conn.commit()
list=cursor.fetchall()
for i in list:
    print(i)
cursor.close()
conn.close()