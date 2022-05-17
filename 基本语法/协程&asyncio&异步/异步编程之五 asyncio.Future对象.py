    # -*- coding:utf-8 -*-
# author:LeiLei
# Future对象是task类的基类
# 低级接口，等待异步结果
# 相当于就是 await ...没有结果就会一直等下去,返回None代表有结果而不是无结果
# 等结果是由Future对象创建的
# _state 状态变为完成 await就不再等了就继续往下走
# asyncio.get_running_loop() 获取当前事件循环
# fut = loop.create_future() 创建一个任务(future对象)，这个任务什么也不干
# await fut 等待任务最终结果,没有结果就一直等下去
import asyncio


async def hahy():
    print('diaodehen')
    loop = asyncio.get_running_loop()
    print(777)
    future = loop.create_future()
    await loop.create_task(hah(future))
    print(888)
async def hah(future):
    # future.set_result("789")
    await asyncio.sleep(4)
    print('555')

open()

if __name__ == '__main__':
    asyncio.run(hahy())