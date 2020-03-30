# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy05Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class QQItem(scrapy.Item):
    name = scrapy.Field()
    company = scrapy.Field()
    href = scrapy.Field()
    location = scrapy.Field()
    salary = scrapy.Field()
    date = scrapy.Field()


