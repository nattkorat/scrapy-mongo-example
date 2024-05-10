"""
Example Spider
---------------
This is the example of spider for testing with MongoDB.
"""
import scrapy
from test_scrapy import model


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
    start_urls = [url.url for url in model.Urls.objects() if not url.is_extract]

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
            tags = quote.css(".tag::text").extract()

            item =  {
                "url": response.url,
                "text": text,
                "tags": tags,
                "author": quote.css(".athor::text").get()
            }

            quote_data = model.Quotes(**item)
            quote_data.save()
        
        # update urls
        url_doc = model.Urls.objects.get(url=response.url)
        url_doc.is_extract = True
        url_doc.save()

            
            
