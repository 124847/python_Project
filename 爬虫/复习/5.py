# -*- coding:utf-8 -*-
# author:LeiLei
import re

import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    url = 'https://www.qiushibaike.com/imgrank/'

    text = requests.get(url, headers=headers).text
    findall = re.findall('<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>', text, re.S)
    for i in findall:
        print(i)
