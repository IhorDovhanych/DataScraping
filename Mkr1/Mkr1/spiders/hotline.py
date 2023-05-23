import scrapy
from Mkr1.items import HotlineShopItem
class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/av/audio/"]
    links = []
    def parse(self, response):
        values = response.css('div.list-item')
        for value in values:
            name = f"name: {value.css('a.list-item__title.text-md.m_b-10::text').get()}"
            category = f"category: {value.css('a.list-item__title.text-sm.m_b-10::text').get()}"
            price = f"price: {value.css('span.price__value::text').get()}"
            yield scrapy.Request(f"https://hotline.ua{value.css('a.btn.btn--orange::attr(href)').get()}", self.parse_foll, meta={
                'name': name,
                'category': category,
                'price': price
                })
        
    def parse_foll(self, response):
        values = response.css('div.list__item.row.flex')
        for value in values:
            yield HotlineShopItem(
                name = value.css('a.shop__title::text').get(),
                price = value.css('span.price__value::text').get(),
                url = f"https://hotline.ua{value.css('a.info__buy-shop::attr(href)').get()}"
            )