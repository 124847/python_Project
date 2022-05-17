import requests
import scrapy
from qiushi.items import QiushiItem

class QiuSpider(scrapy.Spider):
    name = 'qiu'
    # allowed_domains = ['www.qiushi.com']
    start_urls = ['https://www.qiushibaike.com/imgrank/page/1/']
    url = 'https://www.qiushibaike.com/imgrank/page/{}/'
    page = 1
    def parse(self, response):
        lists = response.xpath('//div[@class="col1 old-style-col1"]/div')
        # 返回的是列表   但是元素类型是Selector类型的对象
        # extract可以将Selector对象中的字符串提取出来
        # extract_first 返回列表中第一个元素的data
        for list in lists:
            item = QiushiItem()
            item['author'] = ''.join(list.xpath('./div[@class="author clearfix"]//text()').extract()).replace("\n","").replace("\r","")
            item['content'] = ''.join(list.xpath('.//div[@class="content"]/span/text()').extract()).replace("\n","").replace("\r","")
            yield item
        self.page+=1
        if self.page <= 5:
            new_url = self.url.format(str(self.page))
            print(new_url)
            yield scrapy.Request(url=new_url,callback=self.parse)