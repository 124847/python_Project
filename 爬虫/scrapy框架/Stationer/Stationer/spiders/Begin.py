import scrapy
from Stationer.items import StationerItem

class BeginSpider(scrapy.Spider):
    name = 'Begin'
    # allowed_domains = ['https://sc.chinaz.com/tupian/']
    start_urls = ['https://www.qiushibaike.com/imgrank/page/1/']
    urw = 'https://www.qiushibaike.com/imgrank/page/{}/'
    page = 1
    def papa(self,response):
        item = response.meta['item']
        url = 'https:'+response.xpath('.//*[@id="single-next-link"]/div[2]/img/@src').extract_first()
        item['url'] = url
        print(item['name'])
        yield item
    def parse(self, response):
        divs = response.xpath('.//div[@class="col1 old-style-col1"]/div')
        for div in divs:
            item = StationerItem()
            sname = ''.join(div.xpath('./div[1]//text()').extract()).replace("\n","").replace("\r","")
            src = 'https://www.qiushibaike.com'+div.xpath('.//div[@class="thumb"]/a/@href').extract_first()
            item['name'] = sname
            yield scrapy.Request(url = src, callback=self.papa,meta={'item':item})
        print('第'+str(self.page)+'打印完成')
        self.page+=1
        if self.page<=5:
            yield scrapy.Request(url=self.urw.format(str(self.page)),callback=self.parse)
