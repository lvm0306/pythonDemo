import random

from pyecharts import Bar

attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - inside 示例")
bar.add(
    "",
    attr,
    v1,
    is_datazoom_show=True,
    datazoom_type="both",
    datazoom_range=[10, 25],
)
bar.render("silde_in.html")
