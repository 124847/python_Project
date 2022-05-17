# -*- coding:utf-8 -*-
# author:LeiLei
import re

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }


    def foo():
        print("starting...")
        while True:
            res = yield 4
            print("res:", res)


    g = foo()
    print(next(g))
    print("*" * 20)
    print(next(g))

