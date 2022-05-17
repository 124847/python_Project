# -*- coding:utf-8 -*-
# author:LeiLei
import re
import os
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor
# 也可以这样
from multiprocessing.dummy import Pool
import requests
#  map()方法
# 除了submit，Exectuor还为我们提供了map方法，这个方法返回一个map(func, *iterables)迭代器，迭代器中的回调执行返回的结果有序的
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    url_root = 'https://www.qiushibaike.com/imgrank/page/{}/'
    ex1 = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    ex2 = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
    ex3 = '<div class="author clearfix">.*?<h2>(.*?)</h2>.*?</div>'
    count = 0
    def save(al):
        with open('../文件/糗事图片/作者{}内容{}.jpg'.format(al[0], al[1]),
                  'wb') as fp:
            print('https:' + al[2])
            fp.write(requests.get('https:' + al[2], headers=headers).content)
            fp.close()
            print(str(al[0]).strip() + '的作品打印完成', '已经爬取' + str(count) + '张')
    if not os.path.exists('../文件/糗事图片'):
        os.mkdir('../文件/糗事图片')

    pool = ThreadPoolExecutor()
    for page in range(1, 14):
        url = url_root.format(page)
        list_text = requests.get(url, headers=headers).text
        image_list = re.findall(ex1, list_text, re.S)
        content_list = re.findall(ex2, list_text, re.S)
        author_list = re.findall(ex3, list_text, re.S)
        for i in range(len(image_list)):
            author_detail = ''.join(re.findall('[\u4e00-\u9fa5a-zA-Z0-9]+', author_list[i], re.S))
            # ''.join(可迭代对象)返回字符串用''连接
            content_detail = ''.join(re.findall('[\u4e00-\u9fa5a-zA-Z0-9]+', content_list[i], re.S))
            pool.submit(save,(author_detail,content_detail,image_list[i]))
    print(f'爬取完成，共爬取{count}张')


