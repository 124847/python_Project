# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BukaiPipeline:
    con = None
    def open_spider(self,spider):
        self.con = spider.cont
    def process_item(self, item, spider):
        dic = {
            "name":item["ti"],
            "desc":item["content"]
        }
        self.con.lpush('urlsdata',dic)
        return item
