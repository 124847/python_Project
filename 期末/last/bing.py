# -*- coding:utf-8 -*-
# author:LeiYiBo
# date: 2021-12-28
import pyecharts.options as opts
from pyecharts.charts import Pie


#将top10的关键字作为数据集进行可视化
def get_bing_picture() :

    #定义一个列表作为绘制饼图的列表
    data_pair=[]
    #将spark分析得到的top10关键字的关键字和次数读取到data_pair列表中
    with open('top_10_words.txt', 'r', encoding = 'utf-8') as fp :
        for it in fp.readlines() :
            data_pair.append(it.split("|"))

    #将列表data_pair中得到数据进行绘制 生成一个top_10_words.html网页进行查看
    data_pair.sort(key = lambda x : x[1])
    (
            Pie(init_opts = opts.InitOpts(width = "1280px", height = "800px", bg_color = "#2c343c"))
                .add(
                    series_name = "热搜词",
                    data_pair = data_pair,
                    rosetype = "radius",
                    radius = "55%",
                    center = ["50%", "50%"],
                    label_opts = opts.LabelOpts(is_show = False, position = "center"),
                    )
                .set_global_opts(
                    title_opts = opts.TitleOpts(
                            title = "Top10 words",
                            pos_left = "center",
                            pos_top = "20",
                            title_textstyle_opts = opts.TextStyleOpts(color = "#fff"),
                            ),
                    legend_opts = opts.LegendOpts(is_show = False),
                    )
                .set_series_opts(
                    tooltip_opts = opts.TooltipOpts(
                            trigger = "item", formatter = "{a} <br/>{b}: {c} ({d}%)"
                            ),
                    label_opts = opts.LabelOpts(color = "rgba(255, 255, 255, 0.3)"),
                    )
                .render("top_10_words.html")
    )


#main函数启动程序
if __name__ == '__main__' :
    get_bing_picture()
