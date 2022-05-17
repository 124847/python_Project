# -*- coding:utf-8 -*-
# author:LeiLei
import os

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    url_root = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    text_root = requests.get(url_root, headers=headers)
    text_root.encoding = 'utf-8'  # 使用utf-8编码
    text_root = text_root.text
    soup = BeautifulSoup(text_root, 'lxml')
    all_lists = soup.select('.book-mulu > ul a')
    count = 0
    if not os.path.exists('../文件/三国演义'):
        os.mkdir('../文件/三国演义')
    for detail in all_lists:
        detail_url = 'https://www.shicimingju.com/' + detail['href']
        title = detail.string
        content_all = requests.get(detail_url, headers=headers)
        content_all.encoding = 'utf-8'
        content_all = content_all.text
        content_soup = BeautifulSoup(content_all, 'lxml')
        content_detail = content_soup.find_all('div', class_='card bookmark-list')[0].text.replace("\u00a0", "")
        # 将空格去掉  或者用 replace(" ","" )
        with open(f'../文件/三国演义/{title}.txt', 'w', encoding='utf-8') as fp:
            fp.write(content_detail)
            fp.close()
        print(f'{title}爬取完成!')
        count += 1
    print(f'爬取完成!一共爬取{count}章!')
