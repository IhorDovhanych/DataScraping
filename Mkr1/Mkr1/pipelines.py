# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Mkr1Pipeline:
    def process_item(self, item, spider):
        return item
class HotlinePipeline:

    def process_item(self, item, spider):
        try:
            item["price"] = float(item.get("price").replace("\xa0", ""))
            item["name"] = item.get("name").replace("\n              ", "").replace("\n            ", "")
            return item
        except:
            raise print(f"Bad values in {item}")