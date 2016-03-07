import scrapy
from webcrawl.items import WebcrawlItem

# scrapy crawl spiderman -o file.csv -t csv

class Spiderman(scrapy.Spider):
    name = "spiderman"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=ipad+case",
    ]

    def __init__(self):
        self.i = 0

    def parse(self, response):
        if self.i < 10:
            for sel in response.xpath('//li[@class = "s-result-item celwidget"]'):
                item = WebcrawlItem()
                item['title'] = sel.xpath('.//a/@title').extract()
                item['price'] = sel.xpath('.//a[@class = "a-link-normal a-text-normal"]/span[@class = "a-size-base a-color-price s-price a-text-bold"]/text()').extract()
                item['rating'] = sel.xpath('.//a[@class = "a-popover-trigger a-declarative"]/i/span/text()').extract()
                item_info = sel.xpath('.//a/@href').extract()
                url = response.urljoin(item_info[0])
                request = scrapy.Request(url, callback=self.parse_item)
                request.meta['item'] = item
                yield request

            href = response.xpath('//div[@id = "bottomBar"]/div[@id = "pagn"]/span[@class = "pagnRA"]/a/@href').extract()
            url = response.urljoin(href[0])
            yield scrapy.Request(url, callback=self.parse)
        self.i += 1    

    def parse_item(self, response):
        item = response.meta['item']
        body = response.xpath('//div[@id = "productDetails_feature_div"]')
        products = body.xpath('//table[@class = "a-keyvalue prodDetTable"]//tr/td/text()').extract()
        descripts =  body.xpath('//table[@class = "a-keyvalue prodDetTable"]//tr/th/text()').extract()
        descripts = [x.strip() for x in descripts]
        products = [x.strip() for x in products]
        item['dim'] = products[descripts.index("Product Dimensions")]
        item['weight'] = products[descripts.index("Item Weight")]
        yield item







