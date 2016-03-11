import scrapy
from aptsearch.items import AptsearchItem

# scrapy startproject spiderman
# 2 important files are items.py and spiderman.py
# scrapy crawl spiderman -o file.csv -t csv

class Spiderman(scrapy.Spider):
    name = "spiderman"
    allowed_domains = ["relisto.com"]
    start_urls = [
        "http://relisto.com/rentals/?searchButton=Search&city0=&beds_from=1&beds_to=2&min_rent=&max_rent=5000&pet=&tags=",
    ]

    def __init__(self):
        self.i = 0

    def parse(self, response):
        #if self.i < 10:
        for sel in response.xpath('//li[@style = "line-height: 1.15em;"]'):
            item = AptsearchItem()
            item['title'] = sel.xpath('.//h3[@class = "ygl_info_title"]/a/text()').extract()[0].strip()
            item['address'] = sel.xpath('.//div[@class = "ygl_info_address"]/text()').extract()[0].strip()
            item['price'] = sel.xpath('.//div[@class= "ygl_info_price"]/text()').extract()[0].strip()
            item['bed'] = sel.xpath('.//div[@class= "ygl_info_beds"]/text()').extract()[0].strip()
            item['bath'] = sel.xpath('.//div[@class = "ygl_info_baths"]/text()').extract()[0].strip()
            yield item
        #         item_info = sel.xpath('.//a/@href').extract()
        #         url = response.urljoin(item_info[0])
        #         request = scrapy.Request(url, callback=self.parse_item)
        #         request.meta['item'] = item
        #         yield request

        #     href = response.xpath('//div[@id = "bottomBar"]/div[@id = "pagn"]/span[@class = "pagnRA"]/a/@href').extract()
        #     url = response.urljoin(href[0])
        #     yield scrapy.Request(url, callback=self.parse)
        # self.i += 1    

    # def parse_item(self, response):
    #     item = response.meta['item']
    #     body = response.xpath('//div[@id = "productDetails_feature_div"]')
    #     products = body.xpath('//table[@class = "a-keyvalue prodDetTable"]//tr/td/text()').extract()
    #     descripts =  body.xpath('//table[@class = "a-keyvalue prodDetTable"]//tr/th/text()').extract()
    #     descripts = [x.strip() for x in descripts]
    #     products = [x.strip() for x in products]
    #     item['dim'] = products[descripts.index("Product Dimensions")]
    #     item['weight'] = products[descripts.index("Item Weight")]
    #     yield item







