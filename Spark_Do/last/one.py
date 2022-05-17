# -*- coding:utf-8 -*-
# author:LeiLei

# -*- coding:utf-8 -*-
# author:LeiLei
import asyncio
import datetime
import json
import logging
import random
import time
import pyppeteer
import requests
from pyppeteer import launch

headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }


class One(object) :

    def __init__(self):
        # 日志的基本配置
        logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s: %(message)s')
        self.all_id = set()
        self.all_page = set()
        self.done_page = set()
        self.not_done_page = set()
        self.limit = 20
        self.conunt = []
        self.proxys = set()


    async def scrap_id_all(self):
        browser = await launch(
                headless = False, dumpio = True, autoClose = False,
                args = ['--no-sandbox', '--disable-infobars',f'--proxy-server=89.218.11.2:8080']
                )  # 进入有头模式
        page = await browser.newPage()  # 打开新的标签页
        # await page.setViewport({'width' : 1920, 'height' : 1080})  # 页面大小一致 js为设置webdriver的值，防止网站检测 在 pyppeteer
        # 中提供了一个方法：evaluateOnNewDocument()，该方法是将一段 js 代码加载到页面文档中，当发生页面导航、页面内嵌框架导航的时候加载的 js 代码会自动执行，那么当页面刷新的时候该 js
        # 也会执行，这样就保证了修改网站的属性持久化的目的。

        await page.evaluateOnNewDocument(
                '() =>{ Object.defineProperties(navigator,'
                '{ webdriver:{ get: () => false } }) }'
                )



if __name__ == '__main__' :
    print(requests.get('https://www.qiushibaike.com/').text)