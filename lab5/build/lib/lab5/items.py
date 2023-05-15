# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Lab5Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class SkinItem(scrapy.Item):
    href = scrapy.Field()
    img_url = scrapy.Field()
    fav_numb = scrapy.Field()
    years_ago = scrapy.Field()