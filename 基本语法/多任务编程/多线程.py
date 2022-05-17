# -*- coding:utf-8 -*-
# author:LeiLei
# 进程是资源分配的最小单位，线程是CPU调度的最小单位
# 一个进程中至少有一个线程来负责执行程序,同时线程自己不拥有系统资源,只需要一点儿在运行中必不可少的资源,但它可以
# 与同属一个进程的其它线程共享进程所拥有的全部资源，这就像通过一个QQ软件(一个进程)打开两个窗口(两个线程)两个人聊天一样
# 实现多任务的同时也节省了资源
# 线程的创建步骤
# 1.导入线程模块
# import threading
# 2.通过线程类创建对象
# 线程对象 = threading.thread(target = 任务名)
# 3.启动线程执行任务
# 线程对象.start()
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
# 主线程会等待所有的子线程执行结束后，主线程再结束
# 可以设置子线程守护主线程，等主线程结束，子线程就立即结束销毁
# 方法一 在创建时       thread_1 = threading.Thread(target=sing,daemon = true)
# 方法二 在创建后       thread_1.setDaemon(True)
# 线程执行顺序是无序的，是由cpu调度决定的
# 获取当前的线程信息 通过current_thread 方法获取线程对象
# current_thread = threading.current_thread()
# print(current_thread) 可以打印出线程相关信息
#
import os
import threading
import time


def copy_files(file_name, source_dir, dest_dir):
    source_file = source_dir + '/' + file_name
    dest_file = dest_dir + '/' + file_name
    print(source_file + '------>' + dest_file)
    with open(source_file, 'rb') as fp:
        with open(dest_file, 'wb') as wp:
            while True:
                datas = fp.read(8096)
                if datas:
                    wp.write(datas)
                else:
                    fp.close()
                    wp.close()
                    break


if __name__ == '__main__':
    source_dir = r'D:\项目\java项目\java基础\src\dayone'
    dest_dir = r'D:\Desktop\day'
    try:
        os.mkdir(dest_dir)
    except:
        print('该文件夹已经创建')
    lists_file = os.listdir(source_dir)
    for fi in lists_file:
        thread = threading.Thread(target=copy_files, args=(fi, source_dir, dest_dir))
        thread.start()
