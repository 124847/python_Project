# -*- coding:utf-8 -*-
# author:LeiLei
import asyncio

import aiohttp
import requests
import random
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from lxml import etree


class get_ip():
    user_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    url = 'https://ip.ihuan.me/tqdl.html'
    da = {"num": "3000",
          "port": "",
          "kill_port": "",
          "address": "",
          "kill_address": "",
          "anonymity": "",
          "type": "",
          "post": "",
          "sort": "3",
          "key": "22c7aa6c1869a3d03555e7191dc68ba9",
          }

    def gets(self):
        headers = {
            "User-Agent": random.choice(self.user_list)
        }
        chrome_options = Options()

        chrome_options.add_argument("--headless")
        chrome_options.add_argument(
            f'user-agent={headers["User-Agent"]}')
        # driver = Chrome('./chromedriver', options=chrome_options)
        bro = Chrome(options=chrome_options)
        with open('D:/GitHub/stealth.min.js-main/stealth.min.js-main/stealth.min.js') as f:
            js = f.read()

        bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": js
        })
        bro.get(self.url)
        q = bro.find_element_by_name("num")
        w = bro.find_element_by_name("anonymity")
        w_ = Select(w)
        e = bro.find_element_by_name("post")
        e_ = Select(e)
        r = bro.find_element_by_name("type")
        r_ = Select(r)
        t = bro.find_element_by_name("sort")
        t_ = Select(t)
        q.clear()
        q.send_keys(1000)
        w_.select_by_value('2')
        e_.select_by_value('1')
        r_.select_by_value('1')
        t_.select_by_value('1')
        time.sleep(0.2)
        uy = bro.find_element_by_id("sub")
        uy.click()
        time.sleep(0.2)
        bro.switch_to.window(bro.window_handles[1])  # 注意移动界面
        bro.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # bro.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(0.2)
        tex = bro.page_source
        tree = etree.HTML(tex)
        # xww = bro.find_element_by_xpath('//div[@class="col-md-10"]/div/div[2]')
        # print(xww.text)
        alls = tree.xpath('//div[@class="col-md-10"]//text()')
        time.sleep(0.2)
        bro.quit()
        return alls


    def main(self):
        walls = self.gets()
        walls.pop(0)
        async def canuse(x, user_list):
            proxy = f'http://{x}'
            head = {
                'User-Agent': random.choice(user_list),
                'Connection': 'keep-alive'}
            '''http://icanhazip.com会返回当前的IP地址'''
            try:
                async with aiohttp.ClientSession() as session:
                    async with await session.get(url='http://icanhazip.com', headers=head, proxy=proxy,
                                                 timeout=3) as response:
                        await tyr.append(x)
            except:
                pass


        allsw = [canuse(x,self.user_list) for x in walls]
        tyr = []
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(asyncio.wait(allsw))
        except Exception as e:
            print(e)
        return tyr
if __name__ == '__main__':
    print(get_ip().main())