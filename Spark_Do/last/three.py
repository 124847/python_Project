# -*- coding:utf-8 -*-
# author:LeiLei
import asyncio

import requests
from lxml import etree

import aiohttp

headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }

url_tmp = 'https://tieba.baidu.com/f?kw=%E7%94%B5%E5%BD%B1%E7%A5%A8%E6%88%BF&ie=utf-8&pn={}'

all_data=[]


async def get_all_data() :
    task = []
    for pa in range(0, 1000, 50) :
        task.append(get_detail(url_tmp.format(pa)))
    await asyncio.wait(task)


async def get_detail(url) :
    async with aiohttp.ClientSession() as session :
        async with await session.get(headers = headers, url = url) as response :
            wt = await response.text()
            await asyncio.get_running_loop().run_in_executor(None, do_text, wt)


def do_text(wt) :
    ht = etree.HTML(wt)
    li_s = ht.xpath('//ul[@class="threadlist_bright j_threadlist_bright"]/li')
    for li in li_s :
        text_ = li.xpath('.//div[@class="threadlist_title pull_left j_th_tit"]/a/text()')[0]
        all_data.append(str(text_))




if __name__ == '__main__' :
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_all_data())
    # print(len(all_data))
    # print(all_data)
    text = requests.get(
            headers = headers, url = 'https://tieba.baidu.com/f?kw=%E7%94%B5%E5%BD%B1%E7%A5%A8%E6%88%BF&ie=utf-8&pn=150'
            ).text
    html = etree.HTML(
        text
        )

    li_s = html.xpath('//ul[@class="threadlist_bright j_threadlist_bright"]/li')
    for li in li_s :
        text_ = li.xpath('.//div[@class="threadlist_title pull_left j_th_tit"]/a/text()')[0]
        print(text_)
    print(text)