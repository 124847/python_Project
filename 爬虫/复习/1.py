# -*- coding:utf-8 -*-
# author:LeiLei
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
url = 'https://www.sogou.com/web'
kw = input('enter a word')

param = {
    "query": kw
}

text = requests.get(url, headers = headers,params=param).text
with open('1.html','w') as w:
    w.write(text)
w.close()