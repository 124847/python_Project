# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WangyiPipeline(object):
    def open_spider(self,spider):
        print('开始爬虫')
        self.fp = open('./1.txt', 'w',encoding='utf-8')



    def process_item(self, item, spider):
        self.fp.write(item['title']+':'+item['text'])
        return item

    def close_spider(self,spider):
        print("结束爬虫")
        self.fp.close()