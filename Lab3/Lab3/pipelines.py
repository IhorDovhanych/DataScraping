# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
import mysql.connector

class Lab3Pipeline:
    def process_item(self, item, spider):
        return item
class ClearHotlineDataPipeline:
    def process_item(self, item, spider):
        item['name'] = re.sub(r'\([^)]*\)', '', item['name'])
        item['name'].replace('\n', '')
        item['url'].replace('\xa0','')
        return item
class MySqlPipeline:
    def open_spider(self, spider):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="laravel",
            password="laravel",
            database="scrapy"
        )
        self.cursor = self.connection.cursor()
        spider.logger.info("Connected to MySQL ")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS 
        items (
            id INT AUTO_INCREMENT,
            PRIMARY KEY (id),
            name VARCHAR(50) NOT NULL,
            price VARCHAR(500),
            url VARCHAR(500),
            image_urls VARCHAR(500),
            img LONGBLOB
        );""")
        spider.logger.info("DB is ready ")
        
    def close_spider(self, spider):
        self.connection.close()
        spider.logger.info("Disconnected from MySQL ")

    def process_item(self, item, spider):
        if self.is_duplicate(item):
            self.cursor.execute("""
                UPDATE items
                SET price = %s, url = %s, image_urls = %s, img = %s
                WHERE name = %s
                """,
                [item.get("price"), item.get("url"), item['image_urls'][0], item['image_binary'], item.get("name")])
        else:
            self.cursor.execute(
                "INSERT INTO items (name, price, url, image_urls, img) VALUES (%s, %s, %s, %s, %s);",
                [item.get("name"), item.get("price"), item.get("url"), item['image_urls'][0], item['image_binary']])

        self.connection.commit()
        return item

    def is_duplicate(self, item):
        self.cursor.execute(
            "SELECT COUNT(id) FROM items WHERE name = %s;",
            [item.get("name")])
        count = self.cursor.fetchone()[0]
        return count > 0