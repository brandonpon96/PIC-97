# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AptsearchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    rating = scrapy.Field()
    dim = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    # bed = scrapy.Field()
    # bath = scrapy.Field()
    # desc = scrapy.Field()
