# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from ..items import Doctor
import pymongo


def filter_empty(c):
    return list(filter(lambda a: a and a.strip(), c))


def get_detail(des):
    des = filter_empty(des)
    return ''.join(str(i) for i in list(map(lambda a: a.strip(), des))[1:])


def get_hospital_id_from_url(url):
    return filter_empty(url.split('/'))[-1]


class DoctorSpider(scrapy.Spider):
    chunyu_domain = 'https://www.chunyuyisheng.com'
    name = 'doctor'
    allowed_domains = ['www.chunyuyisheng.com/pc/doctor']

    # start_urls = ['http://www.chunyuyisheng.com/pc/doctor/']

    def start_requests(self):
        self.client = pymongo.MongoClient(host=self.settings.get('MONGO_HOST'), port=self.settings.get('MONGO_PORT'))
        for result in self.client['spider']['Hospital'].find(projection={'_id': False, 'url': True}):
            yield Request(url=result['url'], callback=self.parse_department)

    def parse_department(self, response):
        for li in response.css('#clinic').css('li'):
            url = self.chunyu_domain + li.css('a::attr(href)').extract_first()
            yield Request(url=url, callback=self.parse_hospital_doctor)

    def parse_hospital_doctor(self, response):
        for doctor_div in response.css('dev.doctor-list clearfix').css('div'):
            url = self.chunyu_domain + doctor_div.css('a::attr(href)').extract_first()
            skills = doctor_div.css('p.class::text').extract_first().split('：')[1].split('、')
            yield Request(url=url, callback=lambda response, skills_param=skills: self.parse_doctor(response,
                                                                                                    skills=skills_param))
        next = self.chunyu_domain + response.css('dev.pagebar').css('a.next::attr(href)')
        yield Request(url=next, callback=self.parse_hospital_doctor)

    def parse_doctor(self, response, skills):
        doctor = Doctor()
        doctor_head_div = response.css('div.doctor-wrap clearfix')
        doctor['skills'] = skills
        doctor['avatar'] = doctor_head_div.css('div.avatar-wrap').css('img::attr(src)').extract_first()
        doctor['name'] = doctor_head_div.css('span.name::text').extract_first().strip()
        doctor['department'] = doctor_head_div.css('a.clinic::text(href)').extract_first().strip()
        doctor['level'] = doctor_head_div.css('span.grade::text').extract_first().strip()
        doctor['hospital'] = doctor_head_div.css('a.hospital::text').extract_first().strip()
        doctor['hospital_id'] = get_hospital_id_from_url(doctor_head_div.css('a.hospital::attr(href)').extract_first())
        doctor['label'] = doctor_head_div.css('div.doctor-hospital').css('span::text').extract()
        doctor['consult_price'] = int(doctor_head_div.css('a.doctor-pay-wrap').css('span.price::text').extract_first())
        doctor['consult_time'] = int(
            doctor_head_div.css('ul.doctor-data').css('li')[0].css('span.number::text').extract_first())
        doctor['rate'] = float(
            doctor_head_div.css('ul.doctor-data').css('li')[1].css('span.number::text').extract_first())
        doctor['recognise'] = int(
            doctor_head_div.css('ul.doctor-data').css('li')[2].css('span.number::text').extract_first())
        doctor['patient_heart'] = int(
            doctor_head_div.css('ul.doctor-data').css('li')[3].css('span.number::text').extract_first())
        doctor['background'] = get_detail(response.css('p.detail')[0].css('::text').extract())
        doctor['skills_detail'] = get_detail(response.css('p.detail')[1].css('::text').extract())
        doctor['patient_judge'] = list(map(lambda s: s.strip(), response.css('ul.tags').css('li::text').extract()))
        doctor['favourable_questions'] = response.css('li.tag-item::attr(data-keywords)').extract()
        return doctor
