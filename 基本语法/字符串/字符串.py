# 带引号的内容就是字符串
# 单引号 'name'
# 双引号 "name"
# 三引号 '''name'''     """name"""
# 注意  my name is 'name'     包含单引号 外面用双引号定义  "my name is 'name'"
# 同理 包含双引号 外面用单引号定义
# 当既包含双引号又包含单引号时 外面用三引号定义
# 在python中字符串可以乘数字 表示复制多少个
# 字符串的输入和输出
# 输入 input()
# 输出 print() 函数 %S
# 输出 也可以使用 f-strings   以字母'f'或'F'为前缀 和 format用法相似
# eg:name = 5 age = 10  s = f'我的名字是{name},年龄是{age}'
# 或者用format输出 print('我的名字是{name},年龄是{age}'.format(age='55', name='22'))

# 字符串的切片 [开始:结束:步长]  如果已经确定从前往后 那么步长是负数则无意义 同理如果已经确定从后往前 那么步长是负数则无意义
# 不会对原字符串进行改变，会返回一个新的字符串
# 字符串.find('内容') 如果找到则返回下标，永远是从左往右方向的下标，找不到则返回-1   index()方法如果找不到则报异常
# 字符串.rfind('内容')  从右往左找，返回的永远是从往右方向的下标,找不到则返回-1
# 字符串.count('内容',开始, 结束) 统计出现的次数   返回次数
# 字符串的替换 字符串.replace(旧的,新的,count = 字符串.count(旧的))  将旧的换成新的替换为count次
# count如果超过最大次数不会报错，即按最大次数处理 count也可以省略也按最大次数处理  不会对原字符串进行改变，会返回一个新的字符串
# 字符串.split('分割内容')   返回是一个列表
# 字符串大小写转换和一些判断  这些方法不会对原字符串进行改变
# 大小写转换的方法有以下几种：
# upper()： 字符串全部字符转换为大写
# lower()：字符串全部字符转换为小写
# swapcase() ：字符串全部字符大小写互换
# capitalize()：字符串首个单词首字母大写
# title()： 字符串中全部单词首字母大写
# startwith('内容') 是否以...开头
# endwith('内容') 是否以...结尾
# center(width) 返回一个原字符串居中对齐，并使用空格填充长度为width的新字符串
# ljust(width) 返回一个原字符串左对齐，并使用空格填充长度为width的新字符串
# rjust(width) 返回一个原字符串右对齐，并使用空格填充长度为width的新字符串
# partition('内容') 返回元组 前 内容 后   同理也有rpartition('内容')
# splitlines() 按行分割返回列表 等价于 split('\n')
# isalpha()  是否只包含字母
# isdigit()  是否只包含数字
# isalnum()  是否只包含字母或数字
#  isspace() 是否只包含空格


# 原始字符串不能以“\”结尾，否则会抛出异常。
# 另外，也不能通过转义字符转换最后的“\”，程序会在路径末尾原样输出两个“\”。
# 当我们遇到这种需求时，我们需要对末尾的“\”单独进行转义处理，并和前面的字符串连接。
# eg：path = r'D:\new_project\test\nt\files\data''\\'

# 字符串去除两侧指定内容的方法有三种：
#
# strip(chars) ：去除字符串两侧的指定内容，并且，可以同时去除多个相同的指定内容；
# 参数chars为指定的一个或多个字符，不填入该参数则去除字符串两侧所有空格。
# lstrip(chars)  ：去除字符串左侧的指定内容，并且，可以同时去除多个相同的指定内容；
# 参数chars为指定的一个或多个字符，不填入该参数则去除字符串左侧所有空格。
# rstrip(chars) ：去除字符串右侧的指定内容，并且，可以同时去除多个相同的指定内容；
# 参数chars为指定的一个或多个字符，不填入该参数则去除字符串右侧所有空格。

# 字符串的拼接 s = '1'.join(可迭代对象) 把1加入到每两个元素之间 即变为 可迭代对象[0]1可迭代对象[1]1...可迭代对象[长度-1]
# 返回值类型是一个字符串  可迭代对象必须是字符串类型或里面的内容是字符串类型

# 替换部分字符的方法是“replace(old,new,count)”。
#   返回一个新的字符串
# 如上所述，这个函数有三个参数：
#
# old：表示需要被替换的字符或字符串；
# new：表示替换后的新字符或字符串；
# count：表示替换的次数，此参数可省略；如果省略表示替换所有需要被替换的字符或字符串。



