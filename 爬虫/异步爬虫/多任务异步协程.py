# -*- coding:utf-8 -*-
# author:LeiLei

# 在异步协程中出现了同步相关的代码就无法实现异步 当在asyncio中遇到阻塞操作需要手动挂起
import re
import os
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
import asyncio  # text() 返回字符串形式的响应数据 read() 返回的二进制形式的响应数据 json() 返回的就是json对象
import requests
import aiohttp
import aiofiles

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    url_root = 'https://www.qiushibaike.com/imgrank/page/{}/'
    ex1 = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    ex2 = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
    ex3 = '<div class="author clearfix">.*?<h2>(.*?)</h2>.*?</div>'
    count = 0


    async def save(*al):
        async with aiofiles.open('../文件/糗事图片/作者{}内容{}.jpg'.format(al[0], al[1]),
                                 'wb') as fp:
            print('https:' + str(al[2]))
            async with aiohttp.ClientSession() as session:
                async with await session.get('https:' + str(al[2]), headers=headers) as response:
                    message = await response.read()
                    await fp.write(message)
                    await fp.close()
                    print(str(al[0]).strip() + '的作品打印完成', '已经爬取' + str(count) + '张')


    if not os.path.exists('../文件/糗事图片'):
        os.mkdir('../文件/糗事图片')
    all_s = []
    for page in range(1, 14):
        url = url_root.format(page)
        list_text = requests.get(url, headers=headers).text
        image_list = re.findall(ex1, list_text, re.S)
        content_list = re.findall(ex2, list_text, re.S)
        author_list = re.findall(ex3, list_text, re.S)
        for i in range(len(image_list)):
            author_detail = ''.join(re.findall('[\u4e00-\u9fa5a-zA-Z0-9]+', author_list[i], re.S))
            # ''.join(可迭代对象)返回字符串用''连接
            content_detail = ''.join(re.findall('[\u4e00-\u9fa5a-zA-Z0-9]+', content_list[i], re.S))
            all_s.append(save(author_detail, content_detail, image_list[i]))
    print(f'爬取完成，共爬取{count}张')

    # asyncio.run(asyncio.wait(all_s)) #会报错 但能执行成功
    # 改成下面这种不会报错
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(all_s))
    except Exception as e:
        print(e)
