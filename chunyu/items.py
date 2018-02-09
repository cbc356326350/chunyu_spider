# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Hospital(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    address = scrapy.Field()
    level = scrapy.Field()
    type = scrapy.Field()
    phone = scrapy.Field()
    detail = scrapy.Field()

    pass

