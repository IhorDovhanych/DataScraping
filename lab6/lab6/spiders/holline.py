import scrapy
from lab6.items import HotlineItem 


class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/computer/noutbuki-netbuki/33373/"]

    def parse(self, response):
        data = response.css('div.list-item.list-item--row')
        for item in data:
            image_link = "https://hotline.ua/"+item.css('img::attr(src)').get()
            yield HotlineItem (
                name = item.css('a.list-item__title.text-md::text').get(),
                price = item.css('span.price__value::text').get(),
                url = "https://hotline.ua/"+item.css('a.list-item__title.text-md::attr(href)').get(),
                image_urls = [image_link],
            )
