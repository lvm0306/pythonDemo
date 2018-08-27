from pyecharts import Gauge

gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 66.66)


gauge = Gauge("仪表盘示例")
gauge.add(
    "业务指标",
    "完成率",
    166.66,
    angle_range=[180, 0],
    scale_range=[0, 200],
    is_legend_show=False,
)

gauge.render("gauge.html")