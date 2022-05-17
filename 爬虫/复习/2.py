# -*- coding:utf-8 -*-
# author:LeiLei
import json

import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    wd = input('enter a word')
    data = {
        'kw':wd
    }
url = 'https://fanyi.baidu.com/sug'
jso = requests.post(url, data=data, headers=headers).json()
with open('2.json', 'w',encoding='utf-8') as w:
    json.dump(jso,w,ensure_ascii=False)
load = json.load(open('2.json',encoding='utf-8'))
print(load)


