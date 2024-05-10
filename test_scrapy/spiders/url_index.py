import scrapy
from mongoengine import connect

from test_scrapy import settings
from test_scrapy import model


class UrlIndexSpider(scrapy.Spider):

    name = "url_index"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):

        # save to database
        url_data = model.Urls(url=str(response.url))
        url_data.save()
        
        yield {
            "url": response.url
        }

        next_page = response.css(".next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
