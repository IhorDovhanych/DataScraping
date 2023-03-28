import scrapy
from requests import get
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]
    links_arr = []
    links_arr_copy = []
        

    def parse(self, response):
        data = ET.Element('links')
        links = response.xpath('//a/@href').getall()
        for link in links:
            href = "https://www.worldometers.info" + link
            if href not in self.links_arr:
                data_item = ET.SubElement(data, 'link')
                data_item.set('domain', urlparse(href).netloc)
                data_item.text = href
                self.links_arr.append(href)
        links_arr_copy = self.links_arr.copy()
        for page in links_arr_copy:
            if page not in links_arr_copy:
                    data_item = ET.SubElement(data, 'link')
                    data_item.set('domain', urlparse(page).netloc)
                    data_item.text = page
                    self.links_arr.append(href)
            yield scrapy.Request(page)
            # print(response.xpath('//h1/@text()').get())
            # for link in response.xpath('//a/@href').getall():
            #     href = "https://www.worldometers.info" + link
            #     if href not in links_arr_copy:
            #         data_item = ET.SubElement(data, 'link')
            #         data_item.set('domain', urlparse(href).netloc)
            #         data_item.text = href
            #         links_arr.append(href)
                
        #     page = get(link, headers=HEADERS)
        #     print(page)
            # for additional_link in page.xpath('//a/@href').getall():
            #     href = additional_link
            #     if href not in links_arr:
            #         data_item = ET.SubElement(data, 'link')
            #         data_item.set('domain', urlparse(href).netloc)
            #         data_item.text = href
            #         links_arr.append(href)
        b_xml = ET.tostring(data)
        
        with open("countriesLinks.xml", "wb") as f:
            f.write(b_xml)

            # href = link.get('href')
        #     if href is not None and href not in links_arr:
        #         if link_regex.match(href):
        #             data_item = ET.SubElement(data, 'link')
        #             data_item.set('domain', urlparse(href).netloc)
        #             data_item.text = href
        #             links_arr.append(href)
        #     links_arr_copy = links_arr.copy()
        