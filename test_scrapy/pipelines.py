# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from test_scrapy import settings
from test_scrapy import model


class TestScrapyPipeline:

    def process_item(self, item, spider):
        if spider.name != "url_index":
            data = model.Quotes(**item)

            update_url = model.Urls.objects.get(url=item.get("url", ""))
            if update_url and not update_url.is_extract:
                update_url.is_extract = True
                update_url.save()
        else:
            data = model.Urls(**item)
   
        data.save()
        return item
