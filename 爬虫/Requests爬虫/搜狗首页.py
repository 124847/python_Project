import requests
if __name__ == '__main__':
    url = 'https://www.sogou.com/'
    get = requests.get(url)
    text = get.text
    print(text)
    with open('../文件/搜狗.html','w',encoding='utf-8') as fp:
        fp.write(text)
    print('爬取完成')