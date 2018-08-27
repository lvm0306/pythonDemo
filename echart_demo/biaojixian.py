from pyecharts import Bar

bar = Bar("标记线和标记点示例")
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
# bar.add("商家A", attr, v1, mark_point=["average"])
# bar.add("商家B", attr, v2, mark_line=["min", "max"])
bar.add("商家B", attr, v2,  is_convert=True)
bar.render()