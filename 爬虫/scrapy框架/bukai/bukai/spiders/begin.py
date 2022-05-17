import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from bukai.items import BukaiItem

class BeginSpider(CrawlSpider):
    name = 'begin'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.qiushibaike.com/imgrank/page/1/']
    cont = Redis(host='127.0.0.1', port=6379)
    rules = (
        Rule(LinkExtractor(allow=r'/imgrank/page/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        alls = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for wu in alls:
            ur = 'https://www.qiushibaike.com'+ wu.xpath('./a/@href').extract_first()
            hd = self.cont.sadd('urls', ur)
            if hd == 1:
                item = BukaiItem()
                item['ti'] = wu.xpath('./a/@href').extract_first()
                print('该url还没有爬过')
                yield scrapy.Request(ur,callback=self.parse_detail,meta={"item":item})
            else:
                print('数据还未更新')
    def parse_detail(self,response):
        item = response.meta["item"]
        alls = response.xpath('//*[@class="article-title"]/text()').extract_first()
        item['content'] = alls
        yield item



