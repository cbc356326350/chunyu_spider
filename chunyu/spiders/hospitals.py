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
    allowed_domains = ['www.chunyuyisheng.com']
    start_urls = ['https://www.chunyuyisheng.com/pc/hospitals/']

    def parse(self, response):
        citys = response.css(".city").css('a::attr(href)').extract()
        for city_url in citys:
            yield Request(url=city_url, callback=self.parse_city)

    def parse_city(self, response):
        city_list = response.css('.list')
        for city in city_list:
            city_name = city.css('label::text').extract_first()
            city_url = city.css('.hospital-name::attr(href)').extract_first()
            print(city_url)
            yield Request(url=city_url, callback=lambda response, city_param=city_name: self.parse_hospital(response,city=city_param))
        pass

    def parse_hospital(self, response, city):
        hospital = Hospital()
        hospital['id'] = get_hospital_id_from_url(response.url)
        hospital['name'] = response.css('h3.title::text').extract_first()
        hospital['province'] = response.css('ul.bread-crumb').css('item')[0].css('a::text').extract_first()
        hospital['city'] = city
        hospital['level'] = response.css('div.content-title').css(".label::text")[0].extract_first()
        hospital['type'] = response.css('div.content-title').css(".label::text")[1].extract_first()
        hospital['detail'] = response.css
        return hospital
