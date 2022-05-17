# num = int(input('enter a \t:'))
# if(num < 100 | num > 999):
#     print('you have not enter a number')
# else:
#     flag = 0
#     o = num/10
#     t = num/100
# 三元运算符
# a = 2
# b = 3
# c = a if(a > b) else b
# print(c)
# if 结构
# 1 if    :
#   elif  :
#   else:
# 2 if    :
#   else  :
# get 结构  针对于字典
#
# div= {'mm':12,
#       'cc':34,
#       'dd':55,
#       'ff':66}
#
# print(div.get('mm','bad')) 结果12
# print(div.get('xx','bad')) 结果bad 即若前面的键找不到，就得到返回后面的值
# 查看ascll的值 ord('')
# print(ord('a')) 结果97
# while 循环结构
# i = 0
# while i < 10:
#     i += 1
#     print(i)
# else:
#     print('end')
# import math
# print(math.factorial(3))  3的阶乘
# 用while实现阶乘
# t = 1
# i = 1
# while t <= 3:
#     i *= t
#     t += 1
# print(i)
#
# i = 5
# for m in range(i):
#     print('M:',m)
#     for j in range(m+1):
#
#         print('*', end='')
#     print()   打印乘法表类型的图形，用’*‘组成
# 斐波那契数列
# def fib(n):
#     if (n == 1) or (n == 2):
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(6))
# 阶乘递归
# def hh(n):
#     if(n == 1):
#         return 1
#     else:
#         return n*hh(n-1)
# print(hh(3))
# 使用递归的缺点 虽然递归使事情变得容易，但是复杂度太高了 我们可以使用先行方法完成相同的任务
# 类似的 分而治之的递归过程也需要大量的时间 传上述问题外 递归还有一个缺点 需要很多内存 尽管一部分内存是为栈而保留的，但是递归过程
# 会消耗所有可用的内存，然而递归方法很有趣