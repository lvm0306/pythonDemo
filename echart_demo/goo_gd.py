from pyecharts import Geo

data = [("下城区", 10), ("西湖区", 35), ("江干区", 72),
        ("拱墅区", 72), ("上城区", 500), ("滨江区", 72),
        ("余杭区", 72), ("萧山区", 100)]
geo = Geo(
    "杭州城市空气质量",
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
    maptype="杭州",
    type="effectScatter",
    is_random=True,
    effect_scale=5,
    is_legend_show=False,
    visual_range=[0, 1000],
    visual_text_color="#fff",
    symbol_size=15,
    is_visualmap=True,
)
geo.render("geo_gd.html")