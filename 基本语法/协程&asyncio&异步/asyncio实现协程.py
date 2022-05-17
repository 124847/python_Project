# -*- coding:utf-8 -*-
# author:LeiLei
import asyncio


@asyncio.coroutine
def func1():
    print(1)
    yield from asyncio.sleep(2)
    print(2)


@asyncio.coroutine
def func2():
    print(3)


# tasks = [asyncio.ensure_future(func1()), asyncio.ensure_future(func2())]
tasks = [func1(), func2()]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
asyncio.run(asyncio.wait(tasks))