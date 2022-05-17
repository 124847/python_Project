# -*- coding:utf-8 -*-
# author:LeiLei
# 事件循环 理解为一个死循环,去检测并执行某些代码
# 生成或获取一个事件循环
# loop = asyncio.get_event_loop()
# 将任务放到任务列表
# loop.run_until_complete(任务)
#
import asyncio


async def haha():
    print(100)
async def ha():
    print(99)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
asyncio.run(asyncio.wait([haha(),ha()]))