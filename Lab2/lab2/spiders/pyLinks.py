import scrapy
from requests import get
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlparse


class PylinksSpider(scrapy.Spider):
    name = "pyLinks"
    allowed_domains = ["www.pythontutorial.net"]
    start_urls = ["https://www.pythontutorial.net/python-basics/python-write-text-file/"]

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        links_arr = []
        links_arr_copy = []
        link_regex = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
        HEADERS = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }
        #* ^^-variables-^^
        data = ET.Element('links')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None and href not in links_arr:
                if link_regex.match(href):
                    data_item = ET.SubElement(data, 'link')
                    data_item.set('domain', urlparse(href).netloc)
                    data_item.text = href
                    links_arr.append(href)
            links_arr_copy = links_arr.copy()
        for link in links_arr_copy:
            page = get(link, headers=HEADERS)
            soup = BeautifulSoup(page.text, 'lxml')
            for additional_link in soup.find_all('a'):
                href = additional_link.get('href')
                if href is not None and href not in links_arr:
                    if link_regex.match(href): 
                        data_item = ET.SubElement(data, 'link')
                        data_item.set('domain', urlparse(href).netloc)
                        data_item.text = href
                        links_arr.append(href)
        b_xml = ET.tostring(data)
        
        with open("links.xml", "wb") as f:
            f.write(b_xml)
