# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WikipediaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    isin_number = scrapy.Field()
    company_name = scrapy.Field()
    stock = scrapy.Field()
    url = scrapy.Field()
    founder = scrapy.Field()

class ycombItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company_name = scrapy.Field()
    rank = scrapy.Field()
    overview = scrapy.Field()
    founder = scrapy.Field()
    sector = scrapy.Field()
    jobs_created = scrapy.Field()
    website = scrapy.Field()
    HQ = scrapy.Field()




