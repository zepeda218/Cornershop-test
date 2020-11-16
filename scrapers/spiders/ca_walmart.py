import scrapy
import json
import re
from scrapers.items import ProductItem

class CaWalmartSpider(scrapy.Spider):
    name = "ca_walmart"
    allowed_domains = ["walmart.ca"]
    start_urls = ["https://www.walmart.ca/en/grocery/fruits-vegetables/fruits/N-3852"]
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; http://www.google.com/bot.html) Chrome/W.X.Y.Z‡ Safari/537.36 '
    }

    def parse(self, response):
        for url in response.css('.product-link::attr(href)').getall():
            yield response.follow(url, callback=self.parse_html, cb_kwargs={'url': url})

        next_page = response.css('#loadmore::attr(href)').get()
        
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        
    def parse_html(self, response, url):
        branches = {'3124', '3106'}
        print('theres a reponse!')