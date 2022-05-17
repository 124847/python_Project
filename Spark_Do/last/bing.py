# -*- coding:utf-8 -*-
# author:LeiYiBo
import pyecharts.options as opts
from pyecharts.charts import Pie
x_data = []
y_data = []
with open('top_10_words.txt','r',encoding = 'utf-8') as fp:
    for it in fp.readlines():
        for k,itm in enumerate(it.split("|"),0):
            if k == 0:
                x_data.append(str(itm))
            else:
                y_data.append(int(itm))
data_pair = [list(z) for z in zip(x_data, y_data)]
data_pair.sort(key=lambda x: x[1])
(
    Pie(init_opts=opts.InitOpts(width="1600px", height="800px", bg_color="#2c343c"))
    .add(
        series_name="Top10关键词",
        data_pair=data_pair,
        rosetype="radius",
        radius="55%",
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Customized Pie",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    .render("top_10_words.html")
)
