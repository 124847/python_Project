# -*- coding:utf-8 -*-
# author:LeiLei
import os

import requests
from lxml import etree

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    if not os.path.exists('../文件/站长素材音乐'):
        os.mkdir('../文件/站长素材音乐')
    count = 0
    for page in range(1, 501):
        url_root = f'https://sc.chinaz.com/yinxiao/index_{page}.html'
        text_all = requests.get(url_root, headers=headers).text
        etree_html = etree.HTML(text_all)
        all_term = etree_html.xpath('//div[@id="AudioList"]/div[@class="container"]/div')
        print(f'爬取第{page}页!')
        for term in all_term:
            title = ''.join(term.xpath('.//div[@class="right-head"]//text()')). \
                replace('\n', '').replace('\r', '').replace(" ", "")
            detail_url = ''.join(term.xpath('./audio/@src'))

            if 'https:' not in detail_url:
                detail_url = 'https:' + detail_url
            content_detail = requests.get(detail_url, headers=headers).content
            with open(f'../文件/站长素材音乐/{title}.{detail_url.split(".").pop()}', 'wb') as fp:
                fp.write(content_detail)
                fp.close()
                count += 1
            print(f'{title}已经爬取完成,已经爬取{count}首!')
        print(f'第{page}页爬取完成!')
    print(f'爬取完成！共爬取{count}首')