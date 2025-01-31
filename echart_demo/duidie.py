from pyecharts import Bar

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1)
bar.add("商家B", attr, v2, is_stack=True)
bar.add("商家c", attr, v2, is_stack=True)
bar.add("商家d", attr, v2, is_stack=True)
bar.add("商家e", attr, v2, is_stack=True)
bar.render()