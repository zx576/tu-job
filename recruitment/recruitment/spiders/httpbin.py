# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org/ip']
    start_urls = ['https://httpbin.org/ip']

    def parse(self, response):
        print(response.body)
