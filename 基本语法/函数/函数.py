# 函数可以实现一个具体的功能
# 函数的文档说明本质就是注释，只不过这个注释有特定的位置书写要求，要写在函数名的下方用三引号

# 函数参数

# 局部变量不能在函数外部使用

# 全局变量就是在函数外部定义的变量
# 要想在函数内部修改全局变量的值，需要使用global关键字声明这个变量为全局变量
# 要想在函数内部的函数中修改函数中的局部变量，需要使用nonlocal关键字声明这个变量

# 函数的返回值
# 默认使元组 但也可以返回列表或字典等   return [a,b...] return {a:b,c:d...}
# return 后面可以不写数据值，默认返回 none  不写return 也会默认返回None

# 关键字传参
# 混合使用时，先写位置传参，再写关键字传参 需注意顺序

# 缺省传参即默认传参  如果不传参数则使用默认值
# 定义时应该先写位置参数后写默认参数 eg: def func(a,b,c=10)    错误写法: def func(a=10,b,c)

# 不定长参数,即收集参数 def func(*名字)  这里面传入后变成一个元组 接受所有的位置传参
# def func(**名字) 这里面传入后变成一个字典  接受所有的关键字传参
# def func(*args, **kwargs) 结合使用

# 参数顺序 普通形参 不定长元组参数， 缺省形参，不定长字典形参
#
# 匿名函数 lambda()
# a = 10
# b = 1
# print((lambda a,b:a-b)(a,b))

# def iseven(n):  # 定义验证数字是否偶数的函数
#     if n % 2 == 0:  # 判断参数是否为偶数
#         return True  # 符合条件返回真值
#     else:
#         return False #否则返回假值
#
# lst = list(filter(iseven, number)) # 通过函数iseven对每个number的元素进行验证，验证为真的保留，并将最终结果转换为list。
# print(lst) # 显示输出结果为：[2, 4, 6]
# number = [1, 2, 3, 4, 5, 6]  # 整数列表
#
# lst = list(filter(lambda x: x % 2 == 0, number)) # 通过lambda表达式对每个number的元素进行验证，并将所有验证结果转换为list。
# print(lst) # 显示输出结果为：[2, 4, 6]
# list(filter(函数,可迭代对象(列表等)))   将filter 函数返回值强转为 list
# 排序 list.sort(key = len) 根据列表中字符串的长度排序  list.sort(key = lambda x:(x['age'],x['name'])) 先根据年龄后根据名字

# 列表推导式 快速生成一个列表
# 变量 = [生成数据的规则 for 临时变量 in xxx 可以是多个for循环  后面可以跟if语句]
# 每循环一次就会创建一个数据
# eg:
# number = [1, 2, 3, 4, 5, 6]  # 整数列表
# square = [1, 4, 9, 16, 25, 36]  # 平方列表
# lst = ['{0}²={1}'.format(str(x), str(y)) for x in number for y in square if x <= 3 and x * x == y]
# print(lst) # 显示输出结果为：['1²=1', '2²=4', '3²=9']
