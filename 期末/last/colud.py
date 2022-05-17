# -*- coding:utf-8 -*-
# author:LeiYiBo
# date: 2021-12-28
import pyecharts.options as opts
from pyecharts.charts import WordCloud


# 根据词和次数绘制一个词云
def get_word_cloud() :
    # 创建一个列表
    data = []

    # 将spark分析得到的词和词频读取到data列表中
    with open('all_words.txt', 'r', encoding = 'utf-8') as fp :
        for it in fp.readlines() :
            data.append((it.split("|")[0], it.split("|")[1]))

    # 进行绘制 生成一个all_words.html网页进行查看
    (
            WordCloud()
                .add(series_name = "词云", data_pair = data, word_size_range = [2, 66])
                .set_global_opts(
                    title_opts = opts.TitleOpts(
                            title = "词云", title_textstyle_opts = opts.TextStyleOpts(font_size = 23)
                            ),
                    tooltip_opts = opts.TooltipOpts(is_show = True),
                    )
                .render("all_words.html")
    )


# main函数启动程序
if __name__ == '__main__' :
    get_word_cloud()
