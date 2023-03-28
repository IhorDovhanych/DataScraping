import scrapy


class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/av/audio/"]
    links = []

    def parse(self, response):
        names = response.css('a.list-item__title.text-md.m_b-10::text').getall()
        values = response.css('div.list-item')
        for value in values:
            print(f"name: {value.css('a.list-item__title.text-md.m_b-10::text').get()}\n")
            print(f"category: {value.css('a.list-item__title.text-sm.m_b-10::text').get()}\n")
            print(f"price: {value.css('span.price__value::text').get()} грн\n")
            self.links.append(f"https://hotline.ua{value.css('a.btn.btn--orange::attr(href)').get()}")
        for link in self.links:
            if link is not None:
                values = response.css('a.shop__title::text').getall()
                print(values)
                yield scrapy.Request(response.urljoin(link))
