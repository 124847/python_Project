import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from quanzhan.items import QuanzhanItem
from quanzhan.items import DetailItem


class BeginSpider(CrawlSpider):
    name = 'begin'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest']

    rules = (
        Rule(LinkExtractor(allow=r'id=1&page=\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'index\Sid=\d+'), callback='parse_detail')
    )

    def parse_item(self, response):
        lis = response.xpath('//ul[@class="title-state-ul"]/li')
        for li in lis:
            bianhao = li.xpath('./span[1]/text()').extract_first()
            title = li.xpath('./span[3]/a/text()').extract_first()
            item = QuanzhanItem()
            item['title'] = title
            item['new_id'] = bianhao
            yield item

    def parse_detail(self, response):
        text = response.xpath('//div[@class="details-box"]/pre/text()').extract_first()
        id = response.xpath('//div[@class="focus-date clear focus-date-list"]/span[4]/text()').extract_first()
        item = DetailItem()
        item['content'] = text
        item['new_num'] = id
        yield item
