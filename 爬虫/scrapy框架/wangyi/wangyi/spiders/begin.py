import scrapy
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
from wangyi.items import WangyiItem

class BeginSpider(scrapy.Spider):
    name = 'begin'
    start_urls = ['https://news.163.com/']
    mod_urls = []

    def __init__(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument(
            f'user-agent={headers["User-Agent"]}')

        # driver = Chrome('./chromedriver', options=chrome_options)
        self.bro = Chrome(options=chrome_options)
        with open('D:/GitHub/stealth.min.js-main/stealth.min.js-main/stealth.min.js') as f:
            js = f.read()

        self.bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": js
        })

    def parse(self, response):
        all_li = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        allindex = [2, 3, 5, 6]
        for li in allindex:
            src = all_li[li].xpath('./a/@href').extract_first()
            self.mod_urls.append(src)

        for it in self.mod_urls:
            yield scrapy.Request(url=it, callback=self.parse_m)

    def parse_m(self, response):
        div_list = response.xpath('.//div[@class="ndi_main"]/div')
        for dic in div_list:
            item = WangyiItem()
            title = dic.xpath('.//div[@class="news_title"]//a/text()').extract_first()
            urls = dic.xpath('.//div[@class="news_title"]//a/@href').extract_first()
            item['title'] = title
            yield scrapy.Request(url=urls, callback=self.parse_detail,meta = {"item":item})

    def parse_detail(self, response):
        text = "".join(response.xpath('.//div[@class="post_body"]//text()').extract())
        item = response.meta["item"]
        item['text'] = text
        yield item
    def closed(self, spider):
        self.bro.quit()
