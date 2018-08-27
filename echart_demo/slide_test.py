import random

from pyecharts import Bar

attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - slider 示例")
bar.add("", attr, v1, is_label_show=True, is_datazoom_show=True)
bar.render("slide.html")