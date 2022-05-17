# -*- coding:utf-8 -*-
# author:LeiLei
import json
import copyheaders
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }


    url = 'https://movie.douban.com/j/search_subjects'
    param = {
    "type": "movie",
    "tag": "热门",
    "page_limit": "2",
    "page_start": "0"
    }
    jso = requests.get(url, headers=headers, params=param).json()
    print(jso['subjects'])
