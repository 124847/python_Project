# -*- coding:utf-8 -*-
# author:LeiLei
# uvloop:
# 是asyncio的事件循环的替代方案  事件循环效率>默认asyncio的事件循环   效率接近默认的两倍
# import asyncio
# import uvloop
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# 下面的编写asyncio的代码和之前写的代码一致
# 内部的事件循环自动变为uvloop
# asyncio.run(...)
# 注意 一个asgi->uvicorn内部就是uvloop  Djang快的原因之一就是使用了uvlooppip
