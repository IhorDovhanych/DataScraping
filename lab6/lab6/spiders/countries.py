import scrapy
from requests import get
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
from lab6.items import CountryItem

class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]
    links_arr = []
    links_arr_copy = []
        

    def parse(self, response):
        a_data = response.xpath('//a')
        for selector in a_data:
            href = "https://www.worldometers.info" + selector.css('::attr(href)').get()
            title = selector.css('::text').get()
            if href not in self.links_arr:
                self.links_arr.append(href)
                yield scrapy.Request(href, self.parse_child_page, meta={'link': href, 'title': title})
    def parse_child_page(self, response):
        yield CountryItem (
            title = response.meta['title'],
            link = response.meta['link'],
            links_inside = response.xpath('//a/@href').getall()
        )