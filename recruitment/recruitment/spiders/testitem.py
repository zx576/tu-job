# -*- coding: utf-8 -*-
import scrapy


class TestitemSpider(scrapy.Spider):
    name = 'testitem'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']
    custom_settings = {
        'ITEM_PIPELINES': {
           'recruitment.pipelines.TestPipeline': 300,
        }
    }

    def parse(self, response):
        item = {}
        item['field1'] = 'qwer'
        item['field2'] = 4
        yield item