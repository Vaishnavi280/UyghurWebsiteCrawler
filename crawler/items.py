# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#define models with own words
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    des = scrapy.Field()
    pass
