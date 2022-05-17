# -*- coding:utf-8 -*-
# author:LeiLei
# python检测到一个错误时，解释器就无法继续执行了，反而出现了一些错误的提示，这就是所谓的异常
"""
try:
    可能发生异常的代码
except 异常的类型:
    发生异常执行的代码
"""
# 捕获多个类型的异常
# 方法一 可以在 except (异常类型1,异常类型2,...)
# 方法二 except 异常类型1:
#           pass
#       except 异常类型2:
#           pass
# 打印异常信息
#
# try:
#     可能发生异常的代码
# except 异常的类型 as 变量名:
#     发生异常执行的代码
#     print(变量名)
#
#
# 捕获所有的异常
# try:
#   可能发生异常的代码
# except Exception as e:   如果不想要打印信息可以直接except: 后面不跟任何东西
#   print(e)  打印异常
# Exception 是常见异常类的父类   BaseException是Exception的父类   object是BaseException的父类
# 一般写Exception 写BaseException也可以  但是object不可以打印不出来东西，因为object中少东西
#
# 异常的完整结构
# try:
#   可能发生异常的代码
# except Exception as e:
#   print(e)
# else:
#   代码没有发生异常执行的代码
# finally:
#   不管有没有发生异常都会执行
#
# 异常的传递
# 是python异常处理的底层机制，是原理层面上的，不需要我们自己写代码实现，是python已经实现好的
# 异常传递：当一行代码发生异常之后，会向外层将这个异常进行传递，直到被捕获或者程序报错为止，异常传递捕获优先
# 1. try嵌套
# 2. 函数嵌套
#
# 抛出自定义异常
# raise 异常对象('解释信息')  #当程序代码遇到raise的时候，程序就报错
# 异常对象 =  异常类(参数)
# 抛出自定义异常类
# 1.自定义异常类，继承Exception或者BaseException  class 自定义异常类名(Exception): pass   即可
# 2.选择书写,定义__init__方法,定义__str__ 方法 不写的话使用继承父类的方法
# 3.在合适的时机抛出异常对象即可


