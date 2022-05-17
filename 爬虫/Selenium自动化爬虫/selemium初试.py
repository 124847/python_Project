# -*- coding:utf-8 -*-
# author:LeiLei
from concurrent.futures.thread import ThreadPoolExecutor
import time
from multiprocessing.dummy import Pool
from selenium import webdriver
from lxml import etree

bro = webdriver.Chrome()
bro.get('https://www.taobao.com/')
text_content = bro.find_element_by_id('q')
text_content.send_keys('你好')
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)
button = bro.find_element_by_css_selector('.btn-search')
bro_page_source = bro.page_source
etree_html = etree.HTML(bro_page_source)
li_lists = etree_html.xpath('//ul[@id="gzlist"]/li')
for li in li_lists:
    print(li.xpath('./dl/a/@href')[0])
button.click()
time.sleep(5)
bro.get('https://baidu.com')
print(bro.page_source)
time.sleep(2)
bro.back()
bro.quit()
bro.close()

