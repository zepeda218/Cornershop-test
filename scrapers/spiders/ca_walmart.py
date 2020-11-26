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
        product = json.loads(response.css('.evlleax2 > script:nth-child(1)::text').get())

        sku = product['sku']
        description = product['description']
        name = product['name']
        brand = product['brand']['name']
        image_url = product['image']

        for info in response.css("div.css-0"):
            store = info.css('div[data-automation="sold-shipped"] > svg > title').get()
            package = info.css('p[data-automation="short-description"]').get()
            url = response.xpath("//meta[@property='og:url']/@content")[0].extract()
        
        print(sku)
        print(description)
        print(name)
        print(brand)
        print(image_url)
        print(store)
        print(package)
        print(url)

        # item = ProductItem()

        # item['store'] = store
        # # item['barcodes'] = store
        # item['sku'] = sku
        # item['brand'] = brand
        # item['name'] = name
        # item['description'] = description
        # item['package'] = package
        # item['image_url'] = image_url
        # # item['category'] = category
        # item['url'] = url

        branches = {'3106', '3124'}

        for branch in branches:
            pass
        