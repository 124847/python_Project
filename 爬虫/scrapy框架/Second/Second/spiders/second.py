import scrapy


class SecondSpider(scrapy.Spider):
    name = 'second'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
