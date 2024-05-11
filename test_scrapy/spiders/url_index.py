"""
Url Indexer
----------
This spider job is to list all the target URLs
in the quote to scrape website.
"""
import scrapy
from urllib.parse import urlparse

class UrlIndexSpider(scrapy.Spider):

    name = "url_index"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        """
        Parse

        Attribute
        ---------
        response: HtmlResponse
            Response from the spider requests.
        
        Yield
        -----
        Item of Url and domain.

        """
        yield {
            "url": response.url,
            "domain": urlparse(response.url).netloc
        }

        next_page = response.css(".next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
