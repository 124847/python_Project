# -*- coding:utf-8 -*-
# author:LeiLei
import re

headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }


if __name__ == '__main__':
    print(re.match('(a{1})b', "abcd").group())
    print([x for x in re.match('(a{1})(b)cd',"abcd").group()])


