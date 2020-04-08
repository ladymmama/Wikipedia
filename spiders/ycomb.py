# -*- coding: utf-8 -*-
import scrapy
import re
from Wikipedia.items import ycombItem


class YcombSpider(scrapy.Spider):
    name = 'ycomb'
    # allowed_domains = ['https://www.ycombinator.com/topcompanies']
    # start_urls = ['http://https://www.ycombinator.com/topcompanies/']
    def start_requests(self):
        base_url = 'https://www.ycombinator.com/topcompanies'
        yield scrapy.Request(url=base_url, callback=self.parse)

    def parse(self, response):
        item = ycombItem()
        t1 = re.findall(r'data-name="(.*?)"', response.text)
        t2 = re.findall(r'data-rank="(\d)"', response.text)
        t3 = response.xpath('//div[@class ="col-lg-9 col-md-12"]//tbody/tr/td[3]/p[1]/text()').extract()
        t4 = response.xpath('//div[@class ="col-lg-9 col-md-12"]//tbody/tr/td[3]/p[2]/text()').extract()
        t5 = response.xpath('//div[@class ="col-lg-9 col-md-12"]//tbody/tr/td[4]/p/text()').extract()
        t6 = re.search(r'data-jobs-created="(.*?)" ', response.text)
        t7 = response.xpath('//div[@class ="col-lg-9 col-md-12"]//tbody/tr/td[1]/a/@href').extract()
        t8 = response.xpath('//div[@class ="col-lg-9 col-md-12"]//tbody/tr/td[8]/p/text()').extract()

        for num in range(102):
            item['company_name'] = t1[num]
            item['rank'] = t2[num]
            item['overview'] = t3[num]
            item['founder'] = t4[num]
            item['sector'] = t5[num]
            item['jobs_created'] = t6[num]
            item['website'] = t7[num]
            item['HQ'] = t8[num]
            yield item
