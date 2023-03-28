import scrapy


class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["http://hotline.ua/"]

    def parse(self, response):
        pass
