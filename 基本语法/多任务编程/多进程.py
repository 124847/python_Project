# -*- coding:utf-8 -*-
# author:LeiLei
# 进程是资源分配的最小单位，线程是CPU调度的最小单位
# 进程的创建步骤
# 1.导入进程包
# import multiprocessing
# 2.通过进程类创建进程对象
# 进程对象 = multiprocessing.Process()
# 3.启动进程执行任务
# 进程对象.start()
#
#
#
#
# 通过进程类创建进程对象
# 进程对象 = multiprocessing.Process(target = 任务名)
# 参数名                        说明
# target            执行的目标任务名，这里指的是函数名(方法名)
# name              进程名,一般不用设置
# group             进程组,一般不用，所以使用None
#
#
# 进程执行带有参数
# args      以元组的方式给执行任务传参
# kwargs    以字典的方式给执行任务传参
#
# 获取进程编号
# 获取当前进程的编号  os.getpid()
# 获取当前父进程编号 os.getppid()
# 主进程会等待所有的子进程执行结束再结束
# 所以为了需要可以设置主进程结束后子进程自动销毁，不在执行 可以设置子进程守护主进程即  子进程对象.daemon = True
import os
import time
import multiprocessing


def copy_work(file_name, source_dir, dest_dir):
    source_path = source_dir + '/' + file_name
    dest_path = dest_dir + '/' + file_name
    print(source_path, "------>", dest_path)
    with open(source_path, 'rb') as fp:
        with open(dest_path, 'wb') as wp:
            while True:
                file_data = fp.read(8096)
                if file_data:
                    wp.write(file_data)
                else:
                    break


if __name__ == '__main__':
    source_dir = r'D:\项目\java项目\java基础\src\dayone'
    dest_dir = r'D:\Desktop\day'
    try:
        os.mkdir(dest_dir)
    except:
        print('目标文件夹已经存在,未创建')
    file_lists = os.listdir(source_dir)
    for file_name in file_lists:
        sub_process = multiprocessing.Process(target=copy_work, args=(file_name, source_dir, dest_dir))
        sub_process.start()
