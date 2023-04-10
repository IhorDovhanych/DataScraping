# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class Lab4Pipeline:
    def process_item(self, item, spider):
        return item
class ClearHotlineDataPipeline:
    def process_item(self, item, spider):
        item['name'] = re.sub(r'\([^)]*\)', '', item['name'])
        item['name'].replace('\n', '')
        item['url'].replace('\xa0','')
        return item
