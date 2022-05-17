# -*- coding:utf-8 -*-
# author:LeiLei
import asyncio

import aiohttp

from lxml import etree

headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }

url_tmp = "https://www.qiushibaike.com/8hr/page/{}/"
hot_all_data = set()


async def get_all_data() :
    task = []
    for pa in range(2, 100) :
        task.append(get_detail(url_tmp.format(pa)))
    await asyncio.wait(task)


async def get_detail(url) :
    async with aiohttp.ClientSession() as session :
        async with await session.get(headers = headers, url = url) as response :
            wt = await response.text()
            await asyncio.get_running_loop().run_in_executor(None, do_text, wt)


def do_text(wt) :
    ht = etree.HTML(wt)
    li_s = ht.xpath('//div[@class="recommend-article"]//li')
    for li in li_s :
        text_ = li.xpath('./div[@class="recmd-right"]/a/text()')[0]
        hot_all_data.add(str(text_).replace("\xa0","").replace())




if __name__ == '__main__' :
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_all_data())
    print(len(hot_all_data))
    print(hot_all_data)