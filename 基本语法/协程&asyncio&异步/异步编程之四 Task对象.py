# -*- coding:utf-8 -*-
# author:LeiLei
# Task对象  在事件循环中添加多个任务的
# Tasks用于并发调度协程，通过asyncio.create_task(协程对象)的方式创建Task对象,这样可以让协程加入事件循环中等待被调度执行
# 除了使用asyncio.create_task() 函数之外, 还可以用低层级的asyncio.loop.create_task()或asyncio.ensure_future()函数，
# 不建议手动实例化Task对象 注意在python3.7及之后才可以使用asyncio.create_task()
# 在之前通常使用asyncio.ensure_future()函数
# 一般用列表把 task 放进来
# 例如 tasks = [asyncio.create_task(func1(),name = 't1'(可以不写，系统会给名字)),asyncio.create_task(func2())]
# 结果返回元组 (done,pending) = await asyncio.wait(tasks，timeout=2 (最多到2秒，即超时)) timeout默认是None等待完成，不会超时
#  done是集合 是完成任务的返回值    pending也是集合 是没有完成的任务

import asyncio
import time


# 方法一：不常用
async def func():
    print('大黄')
    await asyncio.sleep(5)
    return 'end'
async def func1():
    print('大黄1')
    await asyncio.sleep(1)
    print('end1')

async def main():
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func1())
    task3 = asyncio.create_task(func1())
    print('ok')

    # done, pending = await asyncio.wait([task1, task2], timeout=1)
    # print(done)
    print(55554112)
    x = await task1  # 仅仅是等待返回结果的
    print(55555544444)
    await task2


    print(45)
    await task3
    # print(done)


asyncio.run(main())

# 方法二：常用
# async def func():
#     print('大黄')
#     await asyncio.sleep(2)
# async def main():
#     tasks = [asyncio.create_task(func()),asyncio.create_task(func())]
#     done,pending = await asyncio.wait(tasks,timeout=1)
#     print(pending)
#
# asyncio.run(main())
# 方法三：对方法二的改造
# async def func():
#     print('大黄')
#     await asyncio.sleep(2)
# tasks = [func(),func()]
# done,pending = asyncio.run(asyncio.wait(tasks,timeout=1))
# print(pending)
