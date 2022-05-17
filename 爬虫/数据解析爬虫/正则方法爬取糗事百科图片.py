# -*- coding:utf-8 -*-
# author:LeiLei
import re
import os
from concurrent.futures.thread import ThreadPoolExecutor

import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    url_root = 'https://www.qiushibaike.com/imgrank/page/{}/'
    ex1 = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    ex2 = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
    ex3 = '<div class="author clearfix">.*?<h2>(.*?)</h2>.*?</div>'
    if not os.path.exists('../文件/糗事图片'):
        os.mkdir('../文件/糗事图片')
    count = 0
    pool = ThreadPoolExecutor()
    for page in range(1, 14):
        url = url_root.format(page)
        list_text = requests.get(url, headers=headers).text
        image_list = re.findall(ex1, list_text, re.S)
        content_list = re.findall(ex2, list_text, re.S)
        author_list = re.findall(ex3, list_text, re.S)
        for i in range(len(image_list)):
            author_detail = ''.join(re.findall('[\u4e00-\u9fa5a-zA-Z0-9]+', author_list[i], re.S))
            #''.join(可迭代对象)返回字符串用''连接
            content_detail = ''.join(re.findall('[\u4e00-\u9fa5a-zA-Z0-9]+', content_list[i], re.S))
            with open('../文件/糗事图片/作者{}内容{}.jpg'.format(author_detail,content_detail),
                      'wb') as fp:
                print('https:' + image_list[i])
                fp.write(requests.get('https:' + image_list[i], headers=headers).content)
                fp.close()
                count = count + 1
                print(str(author_list[i]).strip() + '的作品打印完成', '已经爬取' + str(count) + '张')
        print(f'第{page}页爬取完成')
    print(f'爬取完成，共爬取{count}张')
