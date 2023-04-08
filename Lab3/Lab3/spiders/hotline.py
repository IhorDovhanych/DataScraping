import scrapy
from Lab3.items import HotlineItem
    # name = scrapy.Field()
    # price = scrapy.Field()
    # url = scrapy.Field()
    # image_urls = scrapy.Field()

class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/computer/noutbuki-netbuki/33373/"]

    def parse(self, response):
        data = response.css('div.list-item.list-item--row')
        for item in data:
            img_url = "https://hotline.ua/"+item.css('img::attr(src)').get()
            yield HotlineItem (
                name = item.css('a.list-item__title.text-md::text').get(),
                price = item.css('span.price__value::text').get(),
                url = "https://hotline.ua/"+item.css('a.list-item__title.text-md::attr(href)').get(),
                image_urls = [img_url]
            )
