# -*- coding:utf-8 -*-
# author:LeiLei
# 注意获取响应前一定要进行 await进行手动挂起 线程的挂起是阻塞  进程的挂起是淘汰出内存真正的挂起  协程是对线程的分时使用即阻塞等待
# aiohttp 中 get() post() 和 requests 相同   只是 text 变为 text()
# content 变为 read()    json() 不变  proxies={'https':'https://ip:port'}变为proxy = 'http://ip:port'
# aiohttp 中 先实例一个对象
# async with aiohttp.ClientSession as session:
#   async with await session.get() as response:
#       text = await response.text()
