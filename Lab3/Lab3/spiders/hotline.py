import scrapy
from Lab3.items import HotlineItem

class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/computer/noutbuki-netbuki/33373/"]

    def parse(self, response):
        data = response.css('div.list-item.list-item--row')
        for item in data:
            image_link = "https://hotline.ua/"+item.css('img::attr(src)').get()
            yield scrapy.Request(image_link, callback=self.scrape_image, meta={'item': item, 'image_link': image_link}) 
            
    def scrape_image(self,response):
        
        yield HotlineItem (
                name = response.meta['item'].css('a.list-item__title.text-md::text').get(),
                price = response.meta['item'].css('span.price__value::text').get(),
                url = "https://hotline.ua/"+response.meta['item'].css('a.list-item__title.text-md::attr(href)').get(),
                image_urls = [response.meta['image_link']],
                image_binary = response.body
            )