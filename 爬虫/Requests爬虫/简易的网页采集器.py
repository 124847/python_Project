import requests
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    url = 'https://www.sogou.com/web?'
    qt = input('请输入要查询的内容')
    params = {
        'query': qt
    }
    get = requests.get(url,params,headers = headers)
    text = get.text
    print(text)
    with open('../文件/简易网页采集器.html','w',encoding='utf-8') as fp:
        fp.write(text)
    print('爬取结束')
