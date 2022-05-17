# -*- coding:utf-8 -*-
# author:LeiYiBo
import asyncio
import datetime
import re
import time

from lxml import etree

import aiohttp

headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }

url_tmp = 'https://www.autohome.com.cn/all/{}/#liststart'

all_data=[]


async def get_all_data() :
    task = []
    for pa in range(2,500) :
        task.append(get_detail(url_tmp.format(pa)))
    await asyncio.wait(task)


async def get_detail(url) :
    async with aiohttp.ClientSession() as session :
        async with await session.get(headers = headers, url = url) as response :
            wt = await response.text(encoding='gbk')
            await asyncio.get_running_loop().run_in_executor(None, do_text, wt)


def do_text(wt) :
    ht = etree.HTML(wt)
    li_s = ht.xpath('//div[@id="auto-channel-lazyload-article"]/ul/li')
    for li in li_s :
        time = get_time(li)
        content = get_content(li)
        view = get_view(li)
        all_data.append(time+','+content+','+view)

def get_time(li):
    time = li.xpath('.//span[@class="fn-left"]/span/text()')
    time = time[0] if time else li.xpath('.//span[@class="fn-left"]/text()')[0]
    if "-" in time:
        time = time
    elif '天' in time:
        time = datetime.datetime.now().strftime('%Y-%m-') + str(
            int(datetime.datetime.now().strftime('%d')) -
            int(time.split("天")[0])
            ) + datetime.datetime.now().strftime(' %H:%M:%S')
    else:
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return  time



def get_content(li):
    tp1  = li.xpath('./a/h3/text()')
    cont1 = ''
    cont2 = ''
    if tp1:
        cont1 = tp1[0]
        cont1 = ''.join(list(filter(lambda x : not re.match("\W",x),cont1)))
    tp2  = li.xpath('./a/p/text()')
    if tp2:
        cont2 = tp2[0]
        cont2 = ''.join(list(filter(lambda x : not re.match("\W", x), cont2)))
    return cont1 + cont2

def get_view(li):
    view = li.xpath('.//span[@class="fn-right"]/em[1]/text()')[0]
    if '万' in view:
        view = str(int(float(view.split('万')[0])*10000))
    return view

def save_all():
    with open ('newstmp.txt', 'w' ,encoding = 'utf-8') as fp:
            for i in all_data:
                fp.write(i)
                fp.write('\n')


if __name__ == '__main__' :
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_all_data())
    print(len(all_data))
    save_all()
    print("保存成功")
    print("用时"+str(time.time() - start_time))