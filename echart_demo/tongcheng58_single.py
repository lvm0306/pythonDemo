from pymongo import MongoClient
from pyecharts import Bar

conn = MongoClient('localhost', 27017)
db = conn.tongcheng58  # 连接mydb数据库，没有则自动创建
collection = db.tongcheng58

area_dict = dict()
area_dict['南岗'] = 0
area_dict['道里'] = 0
area_dict['道外'] = 0
area_dict['香坊'] = 0
area_dict['江北'] = 0
area_dict['开发区'] = 0
area_dict['依兰'] = 0
area_dict['方正'] = 0
area_dict['宾县'] = 0
area_dict['巴彦'] = 0
area_dict['木兰'] = 0
area_dict['通河'] = 0
area_dict['哈尔滨周边'] = 0

flag = 'unit_price'

ng = 0
ng_s = 0
dl = 0
dl_s = 0
dw = 0
dw_s = 0
xf = 0
xf_s = 0
jb = 0
jb_s = 0
kfq = 0
kfq_s = 0
yl = 0
yl_s = 0
fz = 0
fz_s = 0
bx = 0
bx_s = 0
by = 0
by_s = 0
ml = 0
ml_s = 0
th = 0
th_s = 0
zb = 0
zb_s = 0

for item in collection.find():
    print(item)

for item in collection.find():
    if item['area'] == '南岗':
        ng += round(float(item[flag]), 2)
        ng_s += 1
    elif item['area'] == '道里':
        dl += round(float(item[flag]), 2)
        dl_s += 1
    elif item['area'] == '道外':
        dw += round(float(item[flag]), 2)
        dw_s += 1
    elif item['area'] == '香坊':
        xf += round(float(item[flag]), 2)
        xf_s += 1
    elif item['area'] == '江北':
        jb += round(float(item[flag]), 2)
        jb_s += 1
    elif item['area'] == '开发区':
        kfq += round(float(item[flag]), 2)
        kfq_s += 1
    elif item['area'] == '依兰':
        yl += round(float(item[flag]), 2)
        yl_s += 1
    elif item['area'] == '方正':
        fz += round(float(item[flag]), 2)
        fz_s += 1
    elif item['area'] == '宾县':
        bx += round(float(item[flag]), 2)
        bx_s += 1
    elif item['area'] == '巴彦':
        by += round(float(item[flag]), 2)
        by_s += 1
    elif item['area'] == '木兰':
        ml += round(float(item[flag]), 2)
        ml_s += 1
    elif item['area'] == '通河':
        th += round(float(item[flag]), 2)
        th_s += 1
    elif item['area'] == '哈尔滨周边':
        zb += round(float(item[flag]), 2)
        zb_s += 1

attr = ["南岗", "道里", "道外", "香坊", "江北", "开发区", "依兰", "方正", "宾县", "巴彦", "木兰", "通河", "哈尔滨周边"]
if ng_s == 0:
    ng_s = 1
if dl_s == 0:
    dl_s = 1
if dw_s == 0:
    dw_s = 1
if xf_s == 0:
    xf_s = 1
if jb_s == 0:
    jb_s = 1
if kfq_s == 0:
    kfq_s = 1
if yl_s == 0:
    yl_s = 1
if fz_s == 0:
    fz_s = 1
if bx_s == 0:
    bx_s = 1
if by_s == 0:
    by_s = 1
if ml_s == 0:
    ml_s = 1
if th_s == 0:
    th_s = 1
if zb_s == 0:
    zb_s = 1

v1 = [round(ng / ng_s, 2),
      round(dl / dl_s, 2),
      round(dw / dw_s, 2),
      round(xf / xf_s, 2),
      round(jb / jb_s, 2),
      round(kfq / kfq_s, 2),
      round(yl / yl_s, 2),
      round(fz / fz_s, 2),
      round(bx / bx_s, 2),
      round(by / by_s, 2),
      round(ml / ml_s, 2),
      round(th / th_s, 2),
      round(zb / zb_s,2)]

bar = Bar("哈尔滨各区每平价格")
bar.add("哈尔滨", attr, v1, is_label_show=True, is_datazoom_show=True,is_more_utils=True)
bar.render("hrb_unit_price.html")
