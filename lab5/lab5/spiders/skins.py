import scrapy
from lab5.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
from lab5.items import SkinItem

class SkinsSpider(scrapy.Spider):
    name = "skins"
    allowed_domains = ["uk.namemc.com"]
    start_urls = ["https://uk.namemc.com/minecraft-skins/random"]

    def start_requests(self):   
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10
            )
            
    def parse(self, response):
        for card in response.css("div.col-4"):
            href = "https://uk.namemc.com"+card.css("a").attrib['href']
            img_url = card.css("img::attr(src)").get()
            fav_numb = card.css("div.position-absolute.bottom-0.right-0.text-muted.mx-1.small-xs.normal-sm::text").get()
            years_ago = card.css("div.position-absolute.bottom-0.left-0.text-muted.mx-1.small-xs.normal-sm::text").get()+card.css("small::text").get()
            yield SkinItem(
                href = href,
                img_url = img_url,
                fav_numb = fav_numb,
                years_ago = years_ago
            )