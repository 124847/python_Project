# # -*- coding:utf-8 -*-
# # author:LeiLei
# import datetime
#
# import requests
# from lxml import etree
#
# headers = {
#         'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
#         }
#
# # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').split("-"))
# # print(datetime.datetime.now().strftime('%d'))
# #
# # def get_content(li):
# #     tp1  = li.xpath('./a/h3/text()')
# #     cont1 = ''
# #     if tp1:
# #         cont1 = tp1[0]
# #     tp2  = li.xpath('./a/p/text()')
# #     cont2 = tp2[0]
# #     return cont1 + cont2
#
# ht = requests.get(headers=headers,url = 'https://www.autohome.com.cn/all/1/#liststart').text
# print(ht)
# html = etree.HTML(ht)
# li_s = html.xpath('//div[@id="auto-channel-lazyload-article"]/ul/li')
# print(len(li_s))
# for li in li_s :
#     view = li.xpath('./a/div[@class="article-bar"]/span[@class="fn-right"]/em[1]/text()')[0]
#     print(view)
#     # content = get_content(li)
#     # print(content)
#

# print(float("8.9万".split("万")[0])*1000)
with open('news.txt',encoding = 'utf-8') as fp:
    for i in fp.readlines():
        print(i)
        print('---------------------------')