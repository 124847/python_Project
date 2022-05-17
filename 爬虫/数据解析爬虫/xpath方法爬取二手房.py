# -*- coding:utf-8 -*-
# author:LeiLei
import requests
from lxml import etree
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    # url_root = 'https://luoyang.58.com/ershoufang/?PGTID=0d100000-0022-c390-df17-a7479bc23cf2&ClickID=1'
    # get_root = requests.get(url_root, headers=headers).text
    # print(get_root)
    # etree_root = etree.HTML(get_root)
    # text_all = etree_root.xpath('//section[@class = "list"]/div')
    # print(text_all)
    parse = etree.parse('../文件/test.html')
    xpath = parse.xpath('//div[1]/text()')
    print(xpath)

