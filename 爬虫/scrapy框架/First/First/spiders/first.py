import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/','http://www.baidu.com/']  # 自动被请求 可以有多个

    def parse(self, response):  # response参数表示请求成功后对应的响应对象
        print(response)
