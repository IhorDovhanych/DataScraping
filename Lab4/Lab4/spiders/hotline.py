import scrapy


class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = [""]
    start_urls = ["http:///"]

    def parse(self, response):
        pass
