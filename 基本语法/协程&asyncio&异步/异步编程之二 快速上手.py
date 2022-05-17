# -*- coding:utf-8 -*-
# author:LeiLei
# 协程函数,定义函数时候 async def 函数名
# 协程对象  协程函数()得到协程对象
# eg:
# async def func():
# print('') ...
# f = func() 执行协程函数创建协程对象，函数内部代码不会执行.
# 执行时需要借助事件循环
# 1.python3.6及之前的写法
# loop = asyncio.get_event_loop()
# loop.run_until_complete(f)
# 2.python3.7及之后的简便写法
# asyncio.run(f)  这一句话等价于上面的两句话，即python3.7后把那两句话封装了









import asyncio

async def func():
    print('大黄')


f = func()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(f)
asyncio.run(f)