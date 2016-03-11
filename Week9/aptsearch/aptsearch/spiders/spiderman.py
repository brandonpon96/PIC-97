import scrapy
from aptsearch.items import AptsearchItem

# scrapy startproject spiderman
# 2 important files are items.py and spiderman.py
# scrapy crawl spiderman -o file.csv -t csv

class Spiderman(scrapy.Spider):
    name = "spiderman"
    allowed_domains = ["youtube.com"]
    start_urls = [
        "https://www.youtube.com/results?search_query=work",
    ]

    def __init__(self):
        self.i = 0

    def parse(self, response):
        #if self.i < 10:
        for sel in response.xpath('//ol[@class="item-section"]/li/div'):
        #for sel in response.xpath('//li[@class= "regular-search-result"]'):
            item = AptsearchItem()
            item['title'] = sel.xpath('.//div[@class="yt-lockup-content"]/h3/a/text()').extract()
            yield item
            # item['title'] = sel.xpath('.//a[@class = "biz-name"]/span/text()').extract()[0].strip()
            # item['price'] = sel.xpath('.//div[@class="biz-rating biz-rating-large clearfix"]/div/i/@title').extract()[0].strip()
            # item['address'] = sel.xpath('.//div[@class="secondary-attributes"]/address/text()').extract()[0].strip()
            # item['price'] = sel.xpath('.//div[@class= "ygl_info_price"]/text()').extract()[0].strip()
            # item['bed'] = sel.xpath('.//div[@class= "ygl_info_beds"]/text()').extract()[0].strip()
            # item['bath'] = sel.xpath('.//div[@class = "ygl_info_baths"]/text()').extract()[0].strip()


            item_info = sel.xpath('.//div[@class="yt-lockup-content"]/h3/a/@href').extract()
            url = response.urljoin(item_info[0])
            request = scrapy.Request(url, callback=self.parse_item)
            request.meta['item'] = item
            yield request
        

        # self.i += 1    

    def parse_item(self, response):
        item = response.meta['item']
        #body = response.xpath('//div[@id = "productDetails_feature_div"]')
        # products = body.xpath('//table[@class = "a-keyvalue prodDetTable"]//tr/td/text()').extract()
        # descripts =  body.xpath('//table[@class = "a-keyvalue prodDetTable"]//tr/th/text()').extract()
        # descripts = [x.strip() for x in descripts]
        # products = [x.strip() for x in products]
        item['dim'] = response.xpath('//div[@id="watch8-sentiment-actions"]//span[@class="yt-uix-button-content"]/text()').extract()[0].strip()
        #item['weight'] = products[descripts.index("Item Weight")]
        yield item







