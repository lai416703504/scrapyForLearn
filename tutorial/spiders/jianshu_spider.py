# -*- coding: utf-8 -*-

import scrapy
from tutorial.items import JianShuItem


class JianShuSpider(scrapy.Spider):
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
        # for sel in response.xpath('//ul[@class="note-list"]/li'):
        #     item = JianShuItem()
        #     item["nickname"] = sel.xpath('div/div[@class="author"]/div[@class="info"]/a[@class="nickname"]/text()').extract()
        #     item["title"] = sel.xpath('div/a/text()').extract()
        #     item["createTime"] = sel.xpath('div/div[@class="author"]/div[@class="info"]/span[@class="time"]/@data-shared-at').extract()
        #     item["abstract"] = sel.xpath('div/p/text()').extract()
        #     item["read"] = sel.xpath('div/div[@class="meta"]/a[1]/text()[last()]').extract()
        #     item["comments"] = sel.xpath('div/div[@class="meta"]/a[2]/text()[last()]').extract()
        #     item["like"] = sel.xpath('div/div[@class="meta"]/span[1]/text()[last()]').extract()
        #     item["money"] = sel.xpath('div/div[@class="meta"]/span[2]/text()[last()]').extract()
        #     yield item

        # collect `item_urls`
        for item_url in item_urls:
            yield scrapy.Request(item_url, self.parse_item)

    def parse_item(self,response):
        item = JianShuItem()
        # populate `item` fields
        # and extract item_details_url
        yield scrapy.Request(item_details_url, self.parse_details, meta={'item': item})

    def parse_details(self, response):
        if "item name" not in response.body:
            open_in_browser(response)

        # item = response.meta['item']
        # return item
