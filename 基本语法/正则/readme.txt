正则表达式的特点：
具有很强的灵活性、逻辑性和功能性；
可以快速通过非常简单的方式达到字符串的复杂控制；
对于初学者比较晦涩难懂。
“正则表达式”这个名称听上去很深奥，实际上它还有另外一个名称叫“规则表达式”。

它是对字符串操作的一种逻辑公式，用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，用来表达对字符串的一种过滤逻辑。

接下来，我们来了解一下上面提到的特定字符和特定字符组合。

在这里，我对它们做了分类。

一、匹配单个字符

\d：匹配单个数字
\D：匹配单个非数字
\w：匹配单个字母或数字或下划线
\W：匹配单个字母或数字或下划线以外的字符
\s：匹配单个不可见字符，例如：\w\s\-\s\d匹配a – 3。（匹配的是空格）
\S：匹配单个可见字符
.：匹配任意一个字符，例如\w.\d匹配a~3。
\.：匹配字符“.”
二、匹配多个字符

*：匹配任意数量字符
三、匹配范围

[xyz]：匹配xyz中任意一个字符
[^xyz]：匹配非xyz的字符
[x|y]：匹配其中任意一个字符
(xxx|yyy)：匹配其中任意一个字符串
[a-z]：匹配a-z的范围
[^a-z]：匹配a-z以外的范围
四、匹配数量

?：0-1个前方子表达式。例如\w?\d匹配a3和3。
+：数量大于0个前方子表达式。例如：/s+ 表示至少一个空格。
{n}：前方子表达式数量为n次。
{n,}：前方子表达式数量至少为n次。
{n,m}：前方子表达式数量至少为n次，最多为m次。
五、匹配首尾字符

^：匹配字符串起始单个字符，后方紧随首个字符或表达式。
$：匹配字符串末尾单个字符，前方紧随末尾字符或表达式。
\b：匹配单词边界，即字符串末尾字符串。例如：er\b匹配player。
\B：匹配非单词边界，即字符串末尾之前的字符串。例如：er\B匹配error。
六、特殊匹配

\：转义字符
\f：匹配一个换页符
\n：匹配一个换行符
\r：匹配一个回车符
\t：匹配一个制表符
\v：匹配一个垂直制表符
七、零宽度断言

零宽度断言是一种零宽度的匹配，它匹配到的内容不会保存到匹配结果中去，最终匹配结果只是一个位置。
它的作用是给指定位置添加一个限定条件，用来规定此位置之前或者之后的字符必须满足限定条件才能使正则中的字表达式匹配成功。

(?!表达式)：向后匹配一个字符，如果不是表达式对应的字符，则匹配成功。
(?=表达式)：向后匹配一个字符，如果是表达式对应的字符，则匹配成功。
(?<=表达式)：向前匹配一个字符，如果是表达式对应的字符，则匹配成功。
(?<!表达式)：向前匹配一个字符，如果不是表达式对应的字符，则匹配成功。
另外，补充一点，如果想获取到零宽度断言匹配成功的字符，需要在断言后方填写表示单个字符的表达式，例如：(?!,).表示字符不是“,”则获取。

——————————————————————————————-

在上方的分类内容中，有一些内容具有等价关系。

等价是等同于的意思，表示同样的功能，用不同符号来书写。

等价字符：

?等价于匹配长度{0,1}
*等价于匹配长度{0,}
+等价于匹配长度{1,}
\d等价于[0-9]
\D等价于[^0-9]
\w等价于[A-Za-z_0-9]
\W等价于[^A-Za-z_0-9]
既然是等价关系，在编写正则表达式的时候就可以互相替代，使用等价字符能够让表达式变得更简洁。

接下来，我们归纳一下常用的一些运算符与表达式，记住这些内容我们就能够

常用运算符与表达式：

^：字符串开始
$：字符串结尾
()：域段/组（group），能够将匹配表达式的字符临时保存，并通过函数group(args)获取。
[]：包含,默认是一个字符长度
[^]：不包含,默认是一个字符长度
{n,m}：匹配长度
.：任何单个字符
|：或
\：转义
[A-Z]：26个大写字母
[a-z]：26个小写字母
[0-9]：0至9数字
[A-Za-z0-9]：26个大写字母、26个小写字母和0至9数字
,：分割，例如：[A,H,T,W] 包含字母A或H或T或W；[a,h,t,w] 包含字母a或h或t或w；[0,3,6,8] 包含数字0或3或6或8。
温馨提示：以上内容只是对正则表达式的入门了解，如果想更加深入还需要找一些更专业的资料进行学习。

通过对上面内容的了解，我们就可以在代码中使用正则表达式了。

一般来说，通过给定一个正则表达式和一个字符串，我们可以达到以下目的：

判断给定的字符串是否符合正则表达式的过滤逻辑（即匹配）；
通过正则表达式，从给定的字符串中获取特定部分。
示例代码：

import re  # 引入正则表达式模块

def check_phone(phone):  # 定义检查手机号码的函数
    regular = '^1[3,4,5,7,8]\d{9}$'  # 定义正则表达式
    if re.match(regular, phone):  # 调用正则匹配函数进行匹配
        print('手机号码格式正确！')  # 匹配提示
    else:
        print('手机号码格式错误！')  # 不匹配提示

check_phone('15111111111')  # 调用函数，显示输出结果为：手机号码格式正确！
check_phone('25111111111')  # 调用函数，显示输出结果为：手机号码格式错误！
check_phone('12111111111')  # 调用函数，显示输出结果为：手机号码格式错误！
check_phone('1511111111') # 调用函数，显示输出结果为：手机号码格式错误！
check_phone('151111111111')  # 调用函数，显示输出结果为：手机号码格式错误！
check_phone('15a11111111')  # 调用函数，显示输出结果为：手机号码格式错误！
手机号码的验证规则为：

首位字符为1；
第2位字符是“3、4、5、7、8”之一。
其余9位是数字。
号码长度为11位。
那么，在组织正则表达式的时候，我们可以这样来完成。

首位字符为1：表达式需要写入“^1”；
第2位字符是“3、4、5、7、8”之一：表达式需要写入“[3,4,5,7,8]”；
其余9位是数字：表达式需要写入“\d{9}”；
号码长度为11位：表达式需要写入“$”（如果不写入“$”超出11位依然能够匹配，而不是精确匹配）。
把上面每一部分连到一起就是完整的正则表达式。
另外，在代码中我们看到，如果使用正则表达式需要导入相应的模块“re”；

在对正则表达式和字符串进行匹配的时候，需要使用re模块中的match(pattern, string[, flags=0])函数。

如果字符串从起始位置（注意不是任意位置）有0个或多个字符与正则表达式匹配，则返回相应的匹配对象。如果字符串与模正则表达式不匹配，则返回None值；注意None与零长度匹配不同，例如表达式’^$’匹配”，即零长度匹配。

参数pattern是正则表达式；参数string是字符串；参数flags是标志（忽略大小写或全局匹配等）。

关于参数flags：

re.I/re.IGNORECASE：忽略大小写。
re.L/re.LOCALE：让\w、\W、\b、\B、\s和\S依赖当前的区域语言设定。
re.M/re.MULTILINE：影响’^’和’$’的行为，指定后，’^’会增加匹配每行的开始（即换行符后的位置）；’$’会增加匹配每行的结束（即换行符前的位置）。
re.S/re.DOTALL：影响’.’的行为，指定后，可以匹配换行符。
re.U/re.UNICODE：让\w、\W、\b、\B、\d、\D、\s和\S依赖Unicode库。
re.X/re.VERBOSE：指定后，忽略所有空白字符（方括号内以及被反斜杠转义的除外）；而且，在每行中“#”号后的所有字符也将被忽略（既能够在正则表达式内部写注释）。
提示：如果想了解函数match的返回结果，可以上方代码的check_phone()函数中添加下列语句：

print(re.match(regular, phone))
会显示类似“<_sre.SRE_Match object; span=(0, 11), match=’15111111111′>”的结果。

其中，span是匹配的区间，match是匹配的全部字符或字符片段。

我们再来看一个通过正则表达式获取身份证号码中出生日期的例子。

示例代码：

import re  # 引入正则表达式模块

def get_birthday(card_id):  # 定义检查身份证号码的函数
    regular = '^\d{6}(\d{4})(\d{2})(\d{2})\d{3}[\d|X]$'  # 定义正则表达式并指定域段
    result=re.match(regular, card_id) #将匹配结果保存到变量
    if result: #如果匹配结果不为None
        return result.group(1,2,3)  # 获取匹配结果中的指定域段并返回结果

print(get_birthday('11011219990109633X'))  # 调用函数，显示输出结果为：('1999', '01', '09')
注意：上方代码中的正则表达式并非真正身份证验证的正则表达式，此案例中仅用于取出出生日期。

大家能够看到，在正则表达式中，我们将一段表达式放入()中，如果有与这段表达式相匹配的字符串，就会被保存。

然后，我们通过group(args)函数能够获取到保存的这些内容，参数args是保存内容的顺序位置，参数为0，可获取匹配的完整字符串。

最后，我们再来看两个示例关于预编译和贪婪模式。

示例代码：（预编译）

import re  # 引入正则表达式模块

regular = r'\d{3}'  # 创建正则表达式
c = re.compile(regular)  # 预编译正则表达式，
print(c.match('abc123',3))  # 显示输出结果为：<_sre.SRE_Match object; span=(3, 6), match='123'>
函数compile(pattern, flags)可以对正则表达式进行预编译并保存到变量中，通过变量调用match(string[, pos[, endpos]])函数即可进行匹配。

大家注意，预编译处理之后调用match函数时的参数是不同的，参数pos为匹配的起始位置，参数endpos为匹配的终止位置。

也就是说，当进行预编译处理后，和指定字符串的匹配可以不是从起始位置开始，而是可以指定匹配的区间。

示例代码：（贪婪模式）

import re # 引入正则表达式模块

print(re.match(r'^(\d+)(0*)$', '102300').groups())  # 结果为('102300', '') # 贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())  # 结果为('1023', '00') # 非贪婪匹配
上方代码中，两个正则表达式有如下特点：

第一个正则表达式中\d+为贪婪匹配，会导致0*无法匹配00。
第二个正则表达式中\d+?为非贪婪匹配， 0*不受影响可以正常匹配00。
贪婪模式会在整个表达式匹配成功的前提下，尽可能多的匹配，而非贪婪模式会在整个表达式匹配成功的前提下，尽可能少的匹配。

关于贪婪模式的量词（特定字符和字符组合）包括：“{m,n}”、“{m,}”、“?”、“*”和“+”。

这些贪婪模式的量词叫匹配优先量词，在这些匹配优先量词的后方后加上“?”，即变成非贪婪模式，叫做忽略优先量词。