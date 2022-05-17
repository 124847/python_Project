# -*- coding:utf-8 -*-
# author:LeiLei

import pyecharts.options as opts
from pyecharts.charts import WordCloud



data = []


(
    WordCloud()
    .add(series_name="热点分析", data_pair=data, word_size_range=[1, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="热点分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("{}.html".format())
)
