# 字符流 文本文件
# 打开文件  open(file 文件名,mode=文件打开的方式，encoding = 编码方式)   将文件从硬盘读取到内存中
# file 文件的名字，类型是str
# mode 文件打开的方式 r(read) 只读打开 文件不存在会报错， w(write) 只写打开 文件不存在会创建新文件 a(append) 追加打开
# encoding 文件的编码格式 常见的 gbk utf-8
# open()函数 返回值是一个文件对象
# 读取文件 文件对象.read()
# 关闭文件 文件.close() 将内存中的文件同步到硬盘中
# open() 函数打开文件没有指定文件的编码，Windows默认是gbk linux和mac默认是utf-8
# 在pycharm中双击打开文件，默认使用的编码是utf-8
# 使用不同的编码打开数据时会出现乱码 编码 就是如何将中文字母变为二进制，解码 使二进制变为中文或字母
# 不管是 a模式还是w模式 都是使用write() 函数
# read(n) 默认不写 读取所有的内容   n表示一次读取多少个字节  也会读取\n
# readline(n) 按行读取  默认不写n  读取一行的内容 不会读取\n
# readlines() 返回值是列表  会读取\n   strip() 可以去掉 \n
# 读取大文件 的两种方法
# while True:
#     buf = f.readline()
#     if buf:
#         print()
#     else:
#         break
# while True:
#     buf = f.read(64)
#     if buf:
#         print()
#     else:
#         break

# 字节流 rb wb ab  不需要指定 encoding 参数  因为是二进制    mp3 mp4 ...
# 写的时候 需要使用 '你好'.encode()方法 将字符转换为二进制    decode()方法 将二进制转换为字符

# 文件的创建用 open(路径和文件名字,'w')
# 文件重命名 os.rename(旧的名字,新的名字)
# 删除文件 os.remove(文件名字)
# 创建文件夹 os.mkdir(文件夹名)
# 获取当前目录 os.getcwd()
# 改变默认目录 os.chdir()   os.chdir('../') ../上级目录 ./和写默认是本目录  也可以指定 同下面的方法   os.chdir('test')
# 获取目录列表 os.listdir() 默认不写返回当前目录的所有文件名包括文件夹名 返回列表  可以有./  os.listdir('./') 下级
# 删除空文件夹 os.rmdir()
# 只检查文件
# import os
# os.path.isfile("test-data")判断是否是文件      os.path.listdir("test-data")   判断是否是文件夹
# 通过这个方法，如果文件”test-data”不存在将返回False，反之返回True。
#
# 即是文件存在，你可能还需要判断文件是否可进行读写操作。
# 判断文件是否可做读写操作
# 使用os.access()方法判断文件是否可进行读写操作。
#
# 语法：
#
# os.access(path, mode)
#
# path为文件路径，mode为操作模式，有这么几种:
#
# os.F_OK: 检查文件是否存在;
#
# os.R_OK: 检查文件是否可读;
#
# os.W_OK: 检查文件是否可以写入;
#
# os.X_OK: 检查文件是否可以执行
#
# 该方法通过判断文件路径是否存在和各种访问模式的权限返回True或者False。
# 可以用循环批量创建删除或修改



#方法一：
# 测试文件共6862646行，79.3M大小，耗时6.7秒。
# 缺点：每一行数据内容不能大于内存大小(一般不会)，否则就会造成MemoryError。
#
# import time
#
# print("开始处理...")
# start = time.time()
# file = r'e:\Python\mypy\搜狗词库\sogou_jianhua_new.txt'
# with open(file, 'rb') as f:								#rb方式最快
# 	for line in f:
# 		li = line.strip()
# 		lin = str(li).lstrip("b")
# end = time.time()
# shi = end - start
# print("已完成！总耗时%s秒！" % shi)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 方法二：
# 使用yield：简单理解，yield就是return，返回一个值，并记住返回的位置，下次迭代就从这个位置后(下一行)开始。
# 正常情况使用上面的方式就可以了，但是，如果遇到整个文件只有一行，
# 而且按照特定的字符进行分割，上面的方式则不行了，这时候yield就非常有用了。
# 举个例子，log的形式是以{|}做为分割符的：
# 2018-06-18 16:12:08,289 - main - DEBUG - Do something{|}……
# 优点：不再限制每行数据的大小，即使整个大文件只有一行。
# 缺点：速度比上面的方式要慢。
#
# def read_line(filename, split, size):
#     with open(filename, 'r+') as f:
#         buff = ''										#定义缓冲区
#         while True:
#             while split in buff:						#若split分割符在缓冲区
#                 position = buff.index(split)			#查找分割符第一次出现的位置
#                 yield buff[:position]					#返回一个值，并记住返回的位置，下次从此开始
#                 buff = buff[(position + len(split)):]	#更新buff，继续下一步
#             chunk = f.read(size)						#若split不在缓冲区，则读取size个字符
#             if not chunk:								#若chunk为空
#                 yield buff
#                 break 									#跳出循环
#             buff = buff + chunk 						#若chunk不为空，则更新buff，继续下一步