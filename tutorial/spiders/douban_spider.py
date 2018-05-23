# -*- coding: utf-8 -*-

import scrapy


class ZhiHuSpider(scrapy.spiders.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://www.douban.com",
        "https://www.douban.com/group/explore"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
