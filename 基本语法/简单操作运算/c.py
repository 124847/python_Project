# 迭代器,生成器和列表解析
# for的强大功能
# for i in l
#   do something
# 迭代器
# 1111111111111111111
# l = [1,2,3,4]
# t = iter(l)
# a  = []
# # 跳过异常 StopIteration
# try:
#     while True:
#         a.append(t.__next__())
#         print(a[0])
# except StopIteration:
#     print("error")
#     print(a[0])
# # raise StopIteration 重新启动异常 StopIteration
# 22222222222222222
# a = [1,2,3,4]
# m = iter(a)
# j = m.__next__()
# try:
#     while True:
#         print(j)
#         j = m.__next__()  或者 j = next(m)
# except:
#     pass
# 定义一个可迭代的对象
# class yrange:
#     def __init__(self, n):
#         self.a = int(input('press:\t'))
#         self.d = int(input('press:\t'))
#         self.i = self.a
#         self.n = n
#     def _iter_(self):
#         return self
#     def _next_(self):
#         if self.i < self.n:
#             i = self.i
#             self.i  = self.i + self.d
#             return  i
#         else:
#             raise StopIteration()
# y = yrange
# y.__init__(y, 8)
# y._iter_(y)
# print(y)
# print(y._next_(y))
# print(y._next_(y))
# print(y._next_(y))

# y = yrange(8)
# x = y._iter_()
# print(x)
# print(x._next_())
# print(x._next_())
# print(x._next_())


# 生成器是生成所需序列的函数 然而 生成器和常规函数之间有一个内在的区别 在生成器中 当我们处理这些值的时候 才会生成这些值 因此 如果一旦
# 一个特定的值生成了 再返回函数中 那么不是回到了函数的开头处 而是返回最初离开函数的那个位置
# 这个任务似乎有点难,但是生成器这个概念可以帮助程序员生成包含了想要的序列的列表 例如 如果我们想要生成包含一个等差数列的各项的列表 其中
# 每一项比前面的一项多d 生成器就派上用场了 类似的 使用生成器也很容易实现像等比数列 斐波那契额数列等序列
# python带有yield关键字 它帮助从我们离开的地方开始 这和常规函数中使用的return 有一个显著的区别 return并不会保存我们离开时的状态
# 如果调用带return的函数 那么它会重新开始执行一次
# 等差数列
# def arithmetic_progression(a, d, n):
#     i = 1
#     while i <= n:
#         yield a + (i - 1) * d
#         i += 1
#
# x = arithmetic_progression(1, 1, 10)
# print(x)
# for m in x:
#     print(m)
# 等比数列
# def ge(a, r, n):
#     i = 1
#     while i <= n:
#         yield a*pow(r, i-1)
#         i += 1
# m = ge(1,2,3)
# print(m)
# for i in m:
#     print(i)
# 斐波那契数列
# def fib(n):
#     a = []
#     if n == 1:
#         a.append(1)
#         yield 1
#     elif n == 2:
#         a.append(1)
#         a.append(1)
#         yield 1
#         yield 1
#     else:
#         i = 2
#         a.append(1)
#         a.append(1)
#         yield 1
#         yield 1
#         while i < n:
#             b = a[i-1] + a[i-2]
#             a.append(b)
#             i += 1
#             yield b
#     print(a) 在下面用循环遍历后才可以将此次结果打印出来 即循环遍历才能执行该函数
# f = fib(5)
# for i in f:   若存在yield 必须用循环遍历才能使该函数该函数执行 打印或者其它功能
#     print(i)
# 列表解析
# l1 = [x**3 for x in range(10)]
# print(l1)
# s = 'winter is comming'.split()
# print(s)
# ss = [[w.upper(), w.lower(), len(w)] for w in s if len(w) > 5]
# print(ss)
# for i in ss:
#     print(i)
# l = [2, 3, 4]
# x = [x + 5 for x in l]
# print(x)
# 利用列表解析求笛卡儿积
# a = ['a', 'b', 'c']
# b = [1, 2, 3, 4]
# axb = [(x,y) for x in a for y in b]
# print(axb)
