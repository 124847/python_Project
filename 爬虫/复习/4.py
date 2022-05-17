# -*- coding:utf-8 -*-
# author:LeiLei
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data = {
        "cname": "",
        "pid": "",
        "keyword": "北京",
        "pageIndex": "1",
        "pageSize": "10"
    }
    json = requests.post(url, data=data,headers=headers).text
    with open('4.html', 'w',encoding='utf-8') as f:
        f.write(json)

