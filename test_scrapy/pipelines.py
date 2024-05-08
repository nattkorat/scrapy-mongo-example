# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter
from test_scrapy import settings


class TestScrapyPipeline:
    client = pymongo.MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DB]

    def process_item(self, item, spider):
        self.db[spider.name].insert_one(dict(item))

        return item
