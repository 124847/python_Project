# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QiushiPipeline(object):
    fp = None

    def open_spider(self, spider):
        print('开始爬虫')
        self.fp = open('糗事.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ":")
        self.fp.write(content + "\n")
        return item

    def close_spider(self, spider):
        print('结束爬虫')
        self.fp.close()
class SecondPipeline(object):
    fp = None

    def open_spider(self, spider):
        print('开始爬虫')
        self.fp = open('糗事备份.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ":")
        self.fp.write(content + "\n")
        return item

    def close_spider(self, spider):
        print('结束爬虫')
        self.fp.close()
