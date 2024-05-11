"""
Quote Spider
---------------
This is the Quote of spider for testing with MongoDB.
"""
import scrapy
from test_scrapy import model


class QuoteSpider(scrapy.Spider):
    """
    Quote Spider Class

    Attribute
    ---------
    name: str
        Spider name, which define for identify the specific spider.
    allowed_domains: list
        List of domains that allow spider to follow the link.
    start_urls: list
        URLs list for spider to start exploring.
    """
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = []
    for url in model.Urls.objects():
        if url.domain in allowed_domains and not url.is_extract:
            start_urls.append(url.url)


    def parse(self, response):
        """
        Spider Parser

        Attribute
        ---------
        response: HtmlResponse
            Response object from spider request agent.

        Yield
        --------------
        Item of quote data as the dictionary object.
        """
        quotes = response.css(".quote")
        for quote in quotes:
            item =  {
                "url": response.url,
                "text": quote.css(".text::text").get(),
                "tags": quote.css(".tag::text").extract(),
                "author": quote.css(".athor::text").get()
            }

            yield item
