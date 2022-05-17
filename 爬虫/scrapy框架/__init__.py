# -*- coding:utf-8 -*-
# author:LeiLei
# 框架: 就是一个集成了很多功能并且具有很强通用性的一个项目模板
# 框架的学习：专门学习框架封装的各种功能的详细用法
# scrapy
# 爬虫中封装好的一个明星框架
# 功能：高性能的持久存储，异步的数据下载，高性能的数据解析，分布式
#
# 创建一个工程：scrapy startproject xxx
# 在spiders子目录中创建一个爬虫文件
#   scrapy genspider spiderName www.xxx.com
# 执行工程：scrapy crawl spiderName
# 不遵守ROBOTS协议  ROBOTSTXT_OBEY = False
# 运行时使用 scrapy crawl spiderName --nolog 没有日志消息
# 一般不用上面的方法 使用 LOG_LEVEL = "ERROR"
# 进行ua伪装
# scrapy 持久化存储
# 基于终端的指令
#   要求 只可以将parse方法的返回值存储到本地的文本文件中
#   注意 持久化存储对相应的文本类型只可以为 'json','jsonlines','jl','csv','xml'等
#   指令 scrapy crawl xxx -o filepath
#   优点 简洁高效便捷
#   缺点 局限性比较强 数据只可以存储到指定后缀的文本文件中 并且是parse方法的返回值
# 基于管道
#   数据解析
#   在item类中定义相关属性
#   将解析的数据封装存储到item类型的对象中
#   将item类型的对象提交给管道进行持久化存储操作
#   在管道类的process_item中要将其接受到的item对象中存储的数据进行持久化存储操作
#   在配置文件中开启管道
#   好处 通用性强
#   管道文件中一个管道类对应的是将数据存储到一种平台
#   爬虫文件提交的item只会给管道文件中第一个被执行的管道类接受
#   process_item中的return item 表示将item传递给下一个即将被执行的管道类
# 全站数据爬取
#   方法一 start_urls 添加 (不推荐)
#   方法二 自行手动请求发送
#
# 五大核心组件
# 引擎
# spider类
# 调度器
# 下载器
# 管道
#
# 请求传参 和持久化存储相关
# 传递item 通过meta = {} 可以将字典数据传递给对应的回调函数
# 数据不在一个页面中，但是要封装到同一个页面中
# 字符串和图片爬取不同 因为字符串数据比较小而图片数据比较大，所以一般来说，不是将图片的二进制数据封装到item中再提交给管道而是封装url到item
# 而是使用 ImagesPipeline这个内部封装好的类
# 图片的数据爬取之ImagesPipeline
# 只需要将img的是src的属性值进行解析提交到管道，管道就会对图片的是url进行请求发送获取图片的二进制数据，而且还会帮我们进行持久化存储
# 使用流程
# from scrapy.pipelines.images import ImagesPipeline
# class 类名(ImagesPipeline):
#   重写方法
# 中间件
# 下载中间件 引擎和下载器之间   作用 批量拦截到整个工程中所有的请求和响应
# 拦截请求
# -UA伪装
# -代理ip
# 拦截响应
# 篡改响应数据，响应对象
#
# 爬虫中间件 引擎和spider之间
# CrawlSpider 类 spider的一个子类
#       全站数据爬取的方式
#       ~基于Spider：手动请求发送
#       ~基于CrawlSpider
# CrawlSpider的使用
# 创建爬虫文件时不一样，变为 scrapy genspider -t crawl xxx www.xxx.com
# linkExtractor  链接提取器 使用正则allow参数对应规则             url 的提取
# Rule 规则解析器  对response进行解析 follow为True 可以将链接提取器继续作用到链接提取器提取到的链接所对应的页面中
# xpath中不能存在tbody因为匹配不到
# 分布式爬虫
# 需要搭建一个分布式的机群，让其对一组资源进行分布联合爬取
# 作用 提升爬取数据的效率
# 原生的scrapy不可以实现分布式
# 必须要结合scrapy_redis
# 可以给原生的scrapy框架提供可以被共享的管道和调度器
# 实现流程
# 创建
# 导入from scrapy_redis.spiders import RedisCrawlSpider
# start_urls 变为 redis_key =  'sun'
# 父类改为RedisCrawlSpider
# 修改配置文件settings
# 指定使用可以被共享的管道
# ITEM_PIPELINES = {'scrapy_redis.pipelines.RedisPipeline':400}
# 指定使用的调度器
# 设置过滤器
# DUPEFILTER_class = "scrapy_redis.dupefilter.RFPDupeFilter"
# 设置调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 是否持久化 即当爬虫结束了要不要清空Redis中的请求队列和去重的set
# SCHEDULER_PERSIST = True
#window中 修改 redis_config 中的bind注释 和 protected关闭
#
# 启动服务 redis-server
# 启动客户端redis-cli
# 执行时 scrapy runspider xxx.py
# lpush sun url
#在settings中设置 REDIS_HOST = ''  服务器 ip
# REDIS_PORT = xxx  端口号
# 增量式爬虫
# 清空 flushall
# 查看 allkeys
# conn=Redis(host,port)
# conn.sadd(xxx)
# conn.lpush(name,dict)

