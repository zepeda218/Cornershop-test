import scrapy
import json
import re
from scrapers.items import ProductItem

class CaWalmartSpider(scrapy.Spider):
    name = "ca_walmart"
    allowed_domains = ["walmart.ca"]
    start_urls = ["https://www.walmart.ca/en/grocery/fruits-vegetables/fruits/N-3852"]
    
    # configuring correct user agent to avoid cookies/js problem
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; http://www.google.com/bot.html) Chrome/W.X.Y.Z‡ Safari/537.36 '
    }

    def parse(self, response):
        for url in response.css('.product-link::attr(href)').getall():
            yield response.follow(url, callback=self.parse_item, cb_kwargs={'url': url})

        next_page = response.css('#loadmore::attr(href)').get()
        
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        
    def parse_item(self, response, url):
        for info in response.css("div.css-0"):
            yield {
                # 'store': info.css('h1[data-automation="product-title"]::text').get(),
                # 'barcodes': info.css('h1[data-automation="product-title"]::text').get(),
                # 'sku': info.css('h1[data-automation="product-title"]::text').get(),
                # 'brand': info.css('h1[data-automation="product-title"]::text').get(),
                'name': info.css('h1[data-automation="product-title"]::text').get(),
                # 'description': info.css('h1[data-automation="product-title"]::text').get(),
                # 'package': info.css('h1[data-automation="product-title"]::text').get(),
                # 'image-url': info.css('h1[data-automation="product-title"]::text').get(),
                # 'category': info.css('h1[data-automation="product-title"]::text').get(),
                # 'url': info.css('h1[data-automation="product-title"]::text').get(),
            }