import scrapy
from mkr2_2.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
from mkr2_2.items import EkItem

class EkSpider(scrapy.Spider):
    name = "ek"
    allowed_domains = ["ek.ua"]
    start_urls = [f"https://ek.ua/ua/list/84/{page}/" for page in range(1,3)]
    def start_requests(self):   
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=2
            )
            
    def parse(self, response):
        for card in response.css('div.model-short-div.list-item--goods'):
            shop_list = card.css('table.model-hot-prices u::text').getall()
            price_list = card.css('table.model-hot-prices a::text').getall()
            if(len(shop_list) == 0):
                shop_list = [card.css('div.pr31-sh.posr u::text').get()]
                price_list = [card.css('div.pr31.ib span::text').get()]
                if(price_list == [None]):
                    price_list = [card.css('div.model-hot-prices-td span::text').get()]
                    if(price_list == [None]):
                        price_list = [card.css('td.model-shop-price span::text').get()]
            for item in price_list:
                if(item == ' ' or item == '\xa0'):
                    price_list.remove(item)
            else:
                for i in range(len(price_list)):
                    price_list[i] = price_list[i].replace(u'\xa0', u'')
                    price_list[i] = price_list[i].replace('грн.', '')
                price_list = list(filter(lambda a: a != '', price_list))
            if(len(shop_list) != 0 and shop_list != [None]):
                for i in range(len(shop_list)):
                    yield EkItem (
                        name = card.css("span.u::text").get(),
                        img_url = card.css("img::attr(src)").get(),
                        shop = shop_list[i],
                        price = price_list[i]
                    )