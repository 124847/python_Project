    # -*- coding:utf-8 -*-
# author:LeiLei
import os
import re

import requests
from lxml import etree

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    url_root = 'https://pic.netbian.com/e/search/result/index.php?'
    count = 0
    if not os.path.exists('../文件/彼岸图片'):
        os.mkdir('../文件/彼岸图片')
    for page in range(187):
        params_page = {
            'page': str(page),
            'searchid': '16'
        }
        text_page = requests.get(url_root, params=params_page, headers=headers)
        text_page.encoding = 'gbk'
        text_page = text_page.text
        etree_html = etree.HTML(text_page)
        etree_list = etree_html.xpath('//ul[@class = "clearfix"]/li')
        print(f'爬取第{page+1}页！')
        for detail in etree_list:
            detail_image = 'https://pic.netbian.com' + detail.xpath('./a/img/@src')[0]
            detail_title = ''.join(re.findall('(.*?)<.*$', detail.
                                              xpath('./a/img/@alt')[0], re.S)).replace(" ", "")
            detail_content = requests.get(detail_image, headers=headers).content
            count += 1
            with open(f'../文件/彼岸图片/{detail_title if detail_title != "" else count}.jpg', 'wb') as fp:
                fp.write(detail_content)
                fp.close()
                print(f'{detail_title}爬取完成！已经爬取{count}张')
    print(f'爬取完成!一共爬取{count}张！')
