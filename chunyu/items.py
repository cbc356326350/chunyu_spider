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
    departments = scrapy.Field()
    url = scrapy.Field()


class Doctor(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    department = scrapy.Field()
    position = scrapy.Field()
    hospital_id = scrapy.Field()
    label = scrapy.Field()
    background = scrapy.Field()
    skills = scrapy.Field()
    skills_detail = scrapy.Field()
    consult_time = scrapy.Field()
    consult_price = scrapy.Field()
    rate = scrapy.Field()
    recognise = scrapy.Field()
    patient_heart = scrapy.Field()
    patient_judge = scrapy.Field()
    favourable_questions = scrapy.Field()
