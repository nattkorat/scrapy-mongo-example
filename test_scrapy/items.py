# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field()
    url_id = scrapy.Field()
    is_downloaded = scrapy.Field()
    is_ocr = scrapy.Field()
    file_links = scrapy.Field()
    file_metadata = scrapy.Field()
    warc_headers = scrapy.Field()

    def validate(self):
        if not isinstance(self["file_links"], list):
            raise ValueError("file_links must be in the list format.")
        
        for file_link in self["file_links"]:
            keys_expected = ["link", "filetype", "file_id"]
            if not isinstance(file_link, dict):
                raise ValueError("File link item must be dictionary with keys(['link', 'filetype', 'file_id'])")
            
            for key_expected in keys_expected:
                if key_expected not in file_link.keys():
                    raise ValueError(f"Missing key {key_expected} in the dictionary.")

        
        if not isinstance(self["is_downloaded"], bool):
            raise ValueError("is_downloaded must be boolean.")
        
        if not isinstance(self["is_ocr"], bool):
            raise ValueError("Is downloaded must be boolean.")
        


if __name__ == "__main__":
    test = TestScrapyItem()

    test["content"] = "hello"
    test["url_id"] = "https://...come"
    test["is_downloaded"] = False
    test["is_ocr"] = False
    test["file_links"] = [{"link": "", "filetype": "", "file_id": ""}]
    test["file_metadata"] = {}
    test["warc_headers"] = {}

    print(type(test))
    test.validate()