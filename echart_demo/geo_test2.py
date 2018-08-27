from pyecharts import Geo

data = [("汕头市", 50), ("汕尾市", 60), ("揭阳市", 35), ("阳江市", 44), ("肇庆市", 72)]
geo = Geo(
    "广东城市空气质量",
    "data from pm2.5",
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color="#404a59",
)
attr, value = geo.cast(data)
geo.add(
    "",
    attr,
    value,
    maptype="广东",
    type="effectScatter",
    is_random=True,
    effect_scale=5,
    is_legend_show=False,
)
geo.render("geo_test.html")