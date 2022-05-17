# re.findall(规则,匹配对象,匹配模式)     返回列表    匹配模式，一般用re.S行匹配，很少用re.M多行匹配
# 修饰符	描述
# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使 . 匹配包括换行在内的所有字符
# re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
# if not os.path.exists(path):  os.mkdir(path)
#''.join(re.findall('[\u4e00-\u9fa5a-zA-Z0-9]+', author_list[i], re.S))
# 匹配汉字然后返回列表 ，可以用 ''.join(可迭代对象)  变为字符串
# ex1 = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>' eg:获取src 即()号里面的返回为列表
# l = ['1 2 ', '2   3', '  3 4']
# import re
# print(eval(re.sub(r'\s*', '', str(l))))
# 返回字符串 通过eval去掉引号变为列表    方法是将前面旧的替换为后面新的 作用于后面的对象

# >> > s = '12 34/n56 78/n90'
#
# >> > re.findall(r'^/d+', s, re.M)  # 匹配位于行首的数字
#
# ['12', '56', '90']
#
# >> > re.findall(r’ / A / d +’, s, re.M )  # 匹配位于字符串开头的数字
#
# ['12']
#
# >> > re.findall(r'/d+$', s, re.M)  # 匹配位于行尾的数字
#
# ['34', '78', '90']
#
# >> > re.findall(r’ / d + / Z’, s, re.M )  # 匹配位于字符串尾的数字
#
# ['90']

# from bs4 import BeautifulSoup
# text = BeautifulSoup(requests.get(url),'lxml')
# text.find('a') 返回第一个a标签内容 等价于 text.a
# text.find_all('a') 返回所有a标签内容为一个列表
# text.find_all('a',class_或id='song') 返回指定class或id

# text.select('.song > ul > div > a')
# text.select('.song > ul  a')
# 括号里面可以是class id等 注意前面的. 返回的是一个列表 层级的分隔符> 中间不支持索引  可以得到列表后再使用索引
# 空格表示多个层级 >号表示一个层级
# 获取标签的文本数据:text.find_all('a',class_或id='song').text
# 或.get_text() 或 .string   前面两种方法获取所有的文本 后面只能获取直系的文本 这三种方法作用于内容只能是单个带标签的字符串
# 获取标签中属性值: text.select('.song > ul  a')['属性名称']获取对应a标签中的属性值  返回集合
# 编码问题
# 利用apparent_encoding
# res = requests.get(url, headers = header)
# res.encoding = res.apparent_encoding   也可以 res.encoding = 'utf-8'
# print(res.text)

# BeautifulSoup 总结
# （1）通过标签名查找
#
# print
# soup.select('title')
# # [<title>The Dormouse's story</title>]
#
# print
# soup.select('a')
# # [<a class="sister" href="http://example.com
# /elsie" id="link1"><!-- Elsie --></a>, <a class="sister" hre
# f="http://example.com/lacie" id="link2">Lacie</a>, <a class="siste
# r" href="http://example.com/tillie" id="link3">Tillie</a>]
#
# print
# soup.select('b')
# # [<b>The Dormouse's story</b>]
# （2）通过类名查找
#
# print
# soup.select('.sister')
# # [<a class="sister" href="http://example.com/elsie" id="l
# ink1"><!-- Elsie --></a>, <a class="sister" href="http:
# //example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="h
# ttp://example.com/tillie" id="link3">Tillie</a>]
# （3）通过
# id
# 名查找
#
# print
# soup.select('#link1')
# # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
# （4）组合查找
#
# 组合查找即和写
#
#
# class 文件时，标签名与类名、id名进行的组合原理是一样的，例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开
#
#
# print
# soup.select('p #link1')
# # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
# 直接子标签查找
#
# print
# soup.select("head > title")
# # [<title>The Dormouse's story</title>]
# （5）属性查找
#
# 查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。
#
#
# print
# soup.select("head > title")
# # [<title>The Dormouse's story</title>]
#
# print
# soup.select('a[href="http://example.com/elsie"]')
# # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
# 同样，属性仍然可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格
#
# print
# soup.select('p a[href="http://example.com/elsie"]')
# # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]


# 注意: 爬虫从网页中爬取的数据中带了一个&nbsp;这样的空格，
# 使用trim()函数和replace(" ", "")去掉不了，找了一下资料发现，
# 空格有两种一种是从键盘输入的对应的unicode值是32，另一种是从网页抓取的对应的unicode值为160，
# 所以提换从网页抓取数据中的空格，使用replace("\u00a0", "")，就可以了:)
# xpath 方法
# 先 from lxml import etree
# 实例化一个etree 对象  本地实例化etree.parse(filepath)
# 本地实例化和BeautifulSoup的区别一个是路径，一个是对象，BeautifulSoup是对象 BeautifulSoup(open(filepath,'r'),'lxml')
# 互联网实例化etree.HTML(响应对象)
# /表示从根节点开始定位。表示的是一个层级  //表示多个层级，也可表示所有的都定位到
# 属性定位://div[@class='song]   即tag[@attrName='attrValue']
# 索引定位//div[@class='song]/p[3]  索引从1开始
# 取文本/text() 取直系文本   //text() 取所有的文本包括直系的文本内容
# 取属性值 //div[@class='song]/p[3]/@src       /@属性名 即可得到属性值
#  如果使用text() 方法最好去一下空格和用.join(可迭代对象)进项处理
