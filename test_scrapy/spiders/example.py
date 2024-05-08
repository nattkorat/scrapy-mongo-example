"""
Example Spider
---------------
This is the example of spider for testing with MongoDB.
"""
import scrapy


class ExampleSpider(scrapy.Spider):
    """
    Example Spider Class

    Attribute
    ---------
    name: str
        Spider name, which define for identify the specific spider.
    allowed_domains: list
        List of domains that allow spider to follow the link.
    start_urls: list
        URLs list for spider to start exploring.
    """

    name = "example"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        """
        Spider Parser

        Attribute
        ---------
        response: HtmlResponse
            Response object from spider request agent.

        Yield
        --------------
        Generator of quote data as the dictionary object.
        """
        quotes = response.css(".quote")
        for quote in quotes:
            text = quote.css(".text::text").get()
            
            yield {
                "text": text
            }
