# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Mkr2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class EkItem(scrapy.Item):
    name = scrapy.Field()
    img_url = scrapy.Field()
    shop_list = scrapy.Field()
    price_list = scrapy.Field()