import re

import requests
def start_worker(*n):
    for index in n:
        params = {
            'cname': '',
            'pid': '',
            'keyword': city,
            'pageIndex': str(index) + '',
            'pageSize': '10',
        }
        url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
        post = requests.post(url, params, headers=headers)
        city_list = eval(post.text)
        for i in city_list['Table1']:
            print(i['provinceName'],i['storeName'],i['addressDetail'])

if __name__ == '__main__':
    city = input('城市')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    l = list(range(1, 5, 1))
    start_worker(*l)




