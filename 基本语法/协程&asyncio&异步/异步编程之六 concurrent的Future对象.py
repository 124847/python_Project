# -*- coding:utf-8 -*-
# author:LeiLei
# concurrent.futures.Future 对象
# 使用线程池,进程池实现异步操作时使用到的对象
# 创建线程池
# pool = ThreadPoolExecutor(max_workers=10)
# fut = pool.submit(func,1)  第一个是函数名 第二个是函数的参数
# 先调用ThreadPoolExecutor的submit方法去线程池申请一个线程去执行func函数
# 返回concurrent.futures.Future 对象
# 同理
# 创建进程池
# # pool = ProcessPoolExecutor(max_workers=10)
# 因为有写第三方模块不支持协程的异步，所以有些时候需要同时使用基于线程池，进程池的异步和基于协程的异步
# 第一步 内部会先调用ThreadPoolExecutor的submit方法去线程池申请一个线程去执行func函数,
# 返回concurrent.futures.Future对象
# 第二步调用asyncio.wrap_future将concurrent.futures.Future对象包装成asyncio.Future对象
# 因为concurrent.futures.Future对象不支持await语法 所以需要包装为asyncio.Future对象才能使用
# fut = loop.run_in_executor(None,func) 返回一个基于协程的对象   第一个参数为None 时默认创建一个线程池
# result = await fut
# 等价于 with concurrent.futures.ThreadPoolExecutor() as pool:
#           result = await loop.run_in_executor(pool,func)
#
#
# 进程池同理with concurrent.futures.ProcessPoolExecutor() as pool:
#            result = await loop.run_in_executor(pool,func)
#
import asyncio
import concurrent.futures
import time

def yu():
    time.sleep(2)
    return "789"

async def wer():
    loop = asyncio.get_running_loop()

    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool,yu)
        print(result)



    # submit = executor.submit(yu, i)
    # print(submit.done())
asyncio.run(wer())