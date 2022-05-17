# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuanzhanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    new_id = scrapy.Field()

class DetailItem(scrapy.Item):
    new_num = scrapy.Field()
    content = scrapy.Field()