# 文件操作
# open 函数
# open函数接受三个参数，第一个参数使文件的名称 第二个参数是打开文件的模式 第三个参数表示缓冲字符串
# r 从一个文件读取 w 写入一个文件 覆盖或新建 a 添加到文件中或新键 r+ 打开文件以进行读和写 a+ 用于读和写 w+ 用于读和写
# wb 以写入模式打开一个二进制文件 rb 读取一个二进制文件 ab 以添加模式打开一个二进制文件 rb+ wb+ ab+ 用于一个二进制文件
# read()函数读取一个字符串中的字节 以一个整数作为参数 该参数表示要读取的字节数 如果该参数为-1 必须读取到该文件的末尾 此外 如果，
# 没有给出这个参数  其默认值为-1 即 read() 和 read(-1) 是相同的
# 如果文件的内容比内存还要大，那么只会读取内存所能容纳的内容 此外 当读取操作结束的时候会返回一个“”空字符串
# a = open('test.txt', 'r')
# x = a.read(-1)
# a.flush()
# a.close()
# print(x)
# 命令行参数
# import sys
# print(' the number of arguments', len(sys.argv))
# print('arguments\n')
# for x in sys.argv:
#     print(x)
# print( c + " 的ASCII 码为", ord(c))
# print( a , " 对应的字符为", chr(a))
# x = 1100000
# print(ord(chr(x)))