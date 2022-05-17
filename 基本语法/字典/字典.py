# {key:value,key:value...}
# 字典 dict  定义使用{}定义，是由键值对组成(key:value) 一个键值对是一个元素
# 字典的key可以是字符串和数字类型等 即不可变类型，   不可以是列表
# value 可以是任何类型
# 定义空字典   x = {}
# 访问value值 字典中没有下标的概念， 是通过key找到value
# value = x['key']  若key值不存在则会报错   x.get('key')  若key值不存在不会保错,返回的是None
# x.get('key',12) 如果key值不存在则返回12
# len(字典) 返回键值对的个数

# 字典中添加和修改数据;如果key值存在则是修改，如果key值不存在就是添加 x[key] = 1
# 字典中key值 int的1和float的1.0是一样的

# 字典中删除数据
# del关键字 del 字典名[key]
# 字典.pop(key) 返回key对应的value值
# 字典.clear()  清空字典 删除所有的键值对
# del 字典名  删除整个字典

# 字典的遍历数据
# 字典.items() 获取所有的键值对，类型是dict_items, key,value 组成的元组类型
# 可以使用 list() 进行类型转化，转换为列表类型
# 可以使用for循环遍历


# enumerate() 函数用于将一个可遍历的数据对象（列表，元组或字符串）组合为一个索引序列，同时列出数据下标和数据 变为元组，一般用在for循环当中

# 运算符 +合并 *复制 in元素是否存在 not in 是否不存在    如果是字典判断的是key值是否存在
# max()  min()  对于字典来说比较的是key值
