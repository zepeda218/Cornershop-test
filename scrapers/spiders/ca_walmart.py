import scrapy
import json
import re
from scrapers.items import ProductItem

class CaWalmartSpider(scrapy.Spider):
    name = "ca_walmart"
    allowed_domains = ["walmart.ca"]
    start_urls = ["https://www.walmart.ca/en/grocery/fruits-vegetables/fruits/N-3852"]

    def parse(self, response):
        with open("test.html", 'wb') as file:
            file.write(response.body)

        if not response.meta.get('solve_captcha',False): 
            print("CAPTCHA")