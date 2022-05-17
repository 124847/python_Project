# -*- coding:utf-8 -*-
# author:LeiLei
import jieba

headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }

print(list(jieba.cut_for_search("你好你好")))