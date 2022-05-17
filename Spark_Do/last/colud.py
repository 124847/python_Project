# -*- coding:utf-8 -*-
# author:LeiYiBo
import pyecharts.options as opts
from pyecharts.charts import WordCloud
data = []
with open('all_words.txt','r',encoding = 'utf-8') as fp:
    for it in fp.readlines():
        data.append((it.split("|")[0],it.split("|")[1]))
(
    WordCloud()
    .add(series_name="词云", data_pair=data, word_size_range=[2, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="词云", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("all_words.html")
)
