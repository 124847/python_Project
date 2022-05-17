# # '''
# # 为了保存值，需要使用变量variable python中的已切都是一个对象 每个对象都有一个标识，
# 一个类型和一个值 在python中标识指向地址并且是不能够修改的。
# #
# # None :表示没有值
# # 数字：python 有三种类型的数字
# #     整数：表示没有任何小数部分
# #     浮点数：可以存储带有小数部分的数字
# #     复数：可以存储实部和虚部
# # '''
# # from decimal import Decimal
# # from fractions import Fraction
# # import math
# # # ceil 用于向上取整
# # a = math.ceil(2.678)
# # print(a)
# # # copysign 用于将第二个参数的符号赋值给第一个参数，作为执行该函数的结果返回
# # a = math.copysign(a, -5)
# # print(a)
# # # fabs 用于求一个数的绝对值
# # print(math.fabs(a))
# # # factorial 从一到这个函数所给参数的阶乘
# # print(math.factorial(3))
# # # floor 用于向下取整
# # print(math.floor(2.5))
# # # 分数和小数
# # # fraction
# # print(Fraction(128, -26))
# # print(Fraction(256))
# # print(Fraction())
# # print(Fraction('2/5'))
# # print(Fraction('2.675438'))
# # print(Fraction(-32.75))
# # print(Fraction('5e-3'))
# # print(Fraction(7.85))
# # print(Fraction(1.1))
# # print(Fraction(2476979795053773, 2251799813685248))
# # print(Fraction(Decimal('59.5')))
# #
# # 序列：表示元素的有序集合 python中有三种类型的序列：
# #     字符串
# # name = 'leilei'
# # print(name)
# # print(name[0])
# # print(name[-2])
# # print(len(name) - 1)
# # name += 'arsh'
# # print(name)
# # print(len(name))
# # print(name[len(name) - 1 - 2])
# # a = name.rsplit('i')
# # for i in a:
# #     print(i)
# # 分片
# name = 'leilei'
# name1 = name[1:]
# print(name1)
# print(name[:2])
# print(name[-2:])
# # 字符串不可变性 当我们写下
# name = 'hello' + name
# # 这时候实际上我们创建了一个新的字符串，他将hello 和name中存储的值拼接了起来，当我们试图修改字符串中一个特定字符串的值的时候，将会产生一个错误，把这一点
# # 联系起来就能够理解字符串的不可变性了
# # name[2] = 'a' 这一步报错 原因字符串不可修改
# print(name)
#     列表
# 在python中列表是对象的集合 列表是python语言中所提供的最通用的序列 和字符串不同 列表是可以改变的 也就是说
# 列表中的一个特定位置的元素是可以修改的
# 在处理同构和异构的学些的时候 列表很有用
#   列表可以是相似的元素 （同构） 的一个集合 如 【1，2，3】
#   他也可以包含不同的元素（异构） 的 如[1，’abc‘，2.4]
# 列表也可以是空的
# 列表可以包含一个列表 即 列表可以嵌套
# a = ['xiaoxiao','leilei' ]
# print(a)
#     元组
# 元组的特点
#  元组是不可变的
# tupl = (2,3)
# tupl[0] = 5   报错
# print(tupl[0])
#   对元组使用+运算符 会把两个元组拼接起来
# a = (1,2)
# b = (3,4)
# c = a+b
# print(c)    结果(1,2,3,4)
# # print(tupl)
# print('the first element is :%d'%tupl[0])
# (a,b) = tupl
# print(a)
# tupll  = (101,'leilei')
# tuplll = (102,'yiyi')
# (wu , da) = tupll
# (xiao,hu) = tuplll
# print('the second element is :%s'%hu)
# print('enter the first number\t:')
# b = int(input())
# print('enter the second number\t:')
# c = int(input())
# print('\nthe numbers entered are %s,%s'%(b,c))
# (b,c) = (c,b)
# 习题
# a = 'harsh'
# b = a[1:len(a)]
# print(b)
# print([-3,len(a)])
# print(2*(a+b))
# 集合：这是元素的无序集合
#     关键字： 这些是具有特殊含义的单词 并且解释器能够识别它们 例如 and del from not while as elif global else is pass yield
#     break except import class raise continue finally return def for try
# 运算符：
#     算数运算符：+ - * / % ** //
#     赋值运算符：+ += -+ *= /= %= **= //=
#     逻辑运算符 or and not
#     比较运算符 < <= > >= !=或者<> ==
# 编程实践
# 1
# (a,b) = (1,2)
# (b,a) = (a,b)
# print(a)
import math
# 2
# print('one:\t')
# M = (a, b) = (int(input()), int(input()))
# print('two:\t')
# N = (c, d) = (int(input()), int(input()))
# print(math.pow((a - c), 2))
# print(math.pow((b - d), 2))
# print(math.sqrt(math.pow((a - c), 2) + math.pow((b - d), 2)))
# print('one:\t')
# 3
# M = (a, b) = (int(input()), int(input()))
# N = (c, d) = (int(input()), int(input()))
# Q = (e, f) = (int(input()), int(input()))
# if(float(f - d) / (e - c) == float(f - b) / (e - a)):
#     print('ok')
