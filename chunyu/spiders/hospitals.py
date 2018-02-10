# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import Hospital


def item_is_not_empty(c):
    return c and c.strip()


def filter_empty(c):
    return list(filter(item_is_not_empty, c))


def get_hospital_id_from_url(url):
    return filter_empty(url.split('/'))[-1]


class HospitalsSpider(scrapy.Spider):
    name = 'hospitals'

    chunyu_domain = 'https://www.chunyuyisheng.com'

    allowed_domains = ['www.chunyuyisheng.com']
    start_urls = ['https://www.chunyuyisheng.com/pc/hospitals/']

    def parse(self, response):
        citys = response.css(".city").css('a::attr(href)').extract()
        for city_url in citys:
            url = self.chunyu_domain + city_url
            yield Request(url=url, callback=self.parse_city)

    def parse_city(self, response):
        city_list = response.css('.list')
        for city in city_list:
            city_name = city.css('label::text').extract_first()
            for hospital_li in city.css('li'):
                city_url = hospital_li.css('.hospital-name::attr(href)').extract_first()
                url = self.chunyu_domain + city_url
                yield Request(url=url, callback=lambda response, city_param=city_name: self.parse_hospital(response,
                                                                                                           city=city_param))
        pass

    def parse_hospital(self, response, city):
        hospital = Hospital()
        hospital['id'] = get_hospital_id_from_url(response.url)
        hospital['name'] = response.css('h3.title::text').extract_first()
        hospital['province'] = response.css('ul.bread-crumb').css('.item')[0].css('a::text').extract_first()
        hospital['city'] = city
        hospital['level'] = response.css('div.content-title').css(".label::text")[0].extract()
        hospital['type'] = response.css('div.content-title').css(".label::text")[1].extract()
        departments = response.css("#clinic").css('a::text').extract()
        hospital['departments'] = list(map(lambda c: c.strip(), departments))
        hospital['url'] = response.url
        hospital['description'] = self.get_detail(response.css('p.detail')[0].css('::text').extract())
        hospital['address'] = self.get_detail(response.css('p.detail')[1].css('::text').extract())
        hospital['phone'] = self.get_detail(response.css('p.detail')[3].css('::text').extract())
        return hospital

    def get_detail(self, des):
        des = filter_empty(des)
        return ''.join(str(i) for i in list(map(lambda a: a.strip(), des))[1:])
