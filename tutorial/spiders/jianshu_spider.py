# -*- coding: utf-8 -*-

import scrapy
from tutorial.items import JianShuItem


class JianShuSpider(scrapy.spiders.Spider):
    name = "jianshu"
    allowed_domains = ["jianshu.com"]
    start_urls = [
        "https://www.jianshu.com",
        "https://www.jianshu.com/c/V2CqjW?utm_medium=index-collections&utm_source=desktop"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for sel in response.xpath('//ul[@class="note-list"]/li'):
            item = JianShuItem()
            item["nickname"] = sel.xpath('div/div[@class="author"]/div[@class="info"]/a[@class="nickname"]/text()').extract()
            item["title"] = sel.xpath('div/a/text()').extract()
            item["createTime"] = sel.xpath('div/div[@class="author"]/div[@class="info"]/span/text()').extract()
            item["abstract"] = sel.xpath('div/p/text()').extract()
            item["read"] = sel.xpath('div/div[@class="meta"]/a[1]/text()[last()]').extract()
            item["comments"] = sel.xpath('div/div[@class="meta"]/a[2]/text()[last()]').extract()
            item["like"] = sel.xpath('div/div[@class="meta"]/span[1]/text()[last()]').extract()
            item["money"] = sel.xpath('div/div[@class="meta"]/span[2]/text()[last()]').extract()
            yield item
