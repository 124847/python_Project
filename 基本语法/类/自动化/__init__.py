# -*- coding:utf-8 -*-
# author:LeiLei
import asyncio
import concurrent.futures
import time
from concurrent.futures import ThreadPoolExecutor

headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }

async def mc():

    pool = ThreadPoolExecutor(max_workers = 5)
    task = []
    loop = asyncio.get_running_loop()
    for i in range(10):
        loop.run_in_executor(pool,wu)
        # task.append(asyncio.ensure_future(asyncio.wrap_future(pool.submit(wu))))


def wu():
    time.sleep(2)
    print("123456789")
    return 15

if __name__ == '__main__':
    # pool = ThreadPoolExecutor(max_workers = 5)
    # for i in range(10):
    #     fut = asyncio.wrap_future(pool.submit(wu,i))
    #     print(fut)
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(mc())
    print(time.time()-t1)
