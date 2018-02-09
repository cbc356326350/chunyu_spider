# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import Hospital


def get_hospital_id_from_url(url):
    def not_empty(s):
        return s and s.strip()
    return list(filter(not_empty, url.split('/')))[-1]


class HospitalsSpider(scrapy.Spider):
    name = 'hospitals'
    allowed_domains = ['`']
    start_urls = ['https://www.chunyuyisheng.com/pc/hospitals/']

    def parse(self, response):
        citys = response.css(".city").css('a::attr(href)').extract()
        for city_url in citys:
            yield Request(url=city_url, callback=self.parse_city)

    def parse_city(self, response):
        city_list = response.css('.list')
        for city in city_list:
            city_url = city.css('.hospital-name::attr(href)').extract()[0]
            print(city_url)
            yield Request(url=city_url, callback=self.parse_hospital)
        pass

    def parse_hospital(self, response):
        hospital = Hospital()
        hospital['id'] = get_hospital_id_from_url(response.url)
        hospital['name'] = response.css('h3.title::text').extract()[0]

        return hospital
