# -*- coding:utf-8 -*-
# author:LeiLei
# 异步迭代器:
# 实现了 __aiter__() 和 __anext__() 方法的对象. __anext__() 必须返回一个awaitable 对象,
# async_for 会处理异步迭代器的 __anext__()方法返回的可等待对象,
# 直到其引发一个stopAsyncIteration异常 由 PEP 492引入
#
# 异步可迭代对象:
# 可在 async for语句中被使用的对象,必须通过它的__aiter__() 方法返回一个 asynchronous iterator
# async for 语句必须在协程函数内


import asyncio

#
# class Reader(object):
#     """自定义异步迭代器(同时也是异步可迭代对象)"""
#
#     def __init__(self):
#         self.count = 0
#
#     async def readlines(self):
#         self.count += 1
#         if self.count == 100:
#             return None
#         return self.count
#
#     def __aiter__(self):
#         return self
#
#     async def __anext__(self):
#         val = await self.readlines()
#         if val == None:
#             raise StopAsyncIteration
#         return val
#
#
# async def func():
#     obj = Reader()
#     async for item in obj:
#         print(item)
#
#
# asyncio.run(func())

#
class yibudiedai(object):
    def __init__(self):
        self.count=0
    def __aiter__(self):
        return  self
    async def readdd(self):
        self.count+=1
        if self.count ==100:
            return None
        else:
            if self.count%5==0:
                await asyncio.sleep(2)
                print("dengyid")
            return self.count
    async def __anext__(self):
        x = await self.readdd()
        if x == None:
            raise StopAsyncIteration
        return x
async def main():
    t = yibudiedai()
    async for i in t:
        print(i)
asyncio.run(main())

