# -*- coding:utf-8 -*-
# author:LeiLei
import requests
from lxml import etree

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    url_root = 'https://www.aqistudy.cn/historydata/'
    text_root = requests.get(url_root, headers=headers).text
    etree_html = etree.HTML(text_root)
    xpath_lists = etree_html.xpath('//div[@class="col-lg-9 col-md-8 col-sm-8 col-xs-12"]/div')
    for lists in xpath_lists:
        title = ''.join(lists.xpath('./div[1]/text()')).strip()
        city_lists = lists.xpath('.//ul[@class="unstyled"]//li')
        city_titles_urls = []
        for detail_city in city_lists:
            city_titles_urls.append((''.join(detail_city.xpath('./a/text()'))
                                    ,'https://www.aqistudy.cn/historydata/'+''.join(detail_city.xpath('./a/@href'))))
        print(title)
        print(city_titles_urls)
