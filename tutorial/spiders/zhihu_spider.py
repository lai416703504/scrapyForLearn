# -*- coding: utf-8 -*-

import scrapy


class ZhiHuSpider(scrapy.spiders.Spider):
    name = "zhihu"
    allowed_domains = ["zhihu.com"]
    start_urls = [
        "https://www.zhihu.com"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
