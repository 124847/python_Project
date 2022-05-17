# -*- coding:utf-8 -*-
# author:LeiLei
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd=ip&rn=&fenlei=256&oq=&rsv_pq=dd3470a000003aec&rsv_t=9507xhPw9ajivFJ43bXxp%2BB8Yd1LzILl%2FxkVLQVhCE6QXAx0hNNwxd%2BnMNM&rqlang=cn&rsv_enter=1&rsv_btype=i&rsv_dl=ib&inputT=640'
    requests_get = requests.get(url, headers=headers,proxies={"https":"https://113.237.3.178:9999"}).text
    print(requests_get)
    with open('..//文件/知乎.html','w',encoding='utf-8') as fp:
        fp.write(requests_get)
        fp.close()
