import scrapy


class BeginSpider(scrapy.Spider):
    name = 'begin'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://news.163.com/']

    def parse(self, response):
        text = response.text
        with open('ip.html','w',encoding='utf-8')as fp:
            fp.write(text)
            fp.close()
