import scrapy
from scrapy.linkextractor import LinkExtractor

class WeidsSpider(scrapy.Spider):
     name = "weids"
     allowed_domains = ["wds.modian.com"]
     start_urls = ['http://www.gaosiedu.com/gsschool/']

     def parse(self, response):
         link = LinkExtractor(restrict_xpaths='//ul[@class="list"]/li')
         links = link.extract_links(response)
         print(links)
         print(link)