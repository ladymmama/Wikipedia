# -*- coding: utf-8 -*-
import scrapy
import re
import pandas as pd
from Wikipedia.items import WikipediaItem

def excel_one_line_to_list():
    df = pd.read_excel("../global_2000.xlsx",
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.iloc[7:, 2: ].values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    return result

class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia'
    # allowed_domains = ['wiki.com']
    # start_urls = ['http://wiki.com/']

    def start_requests(self):
        company_name = excel_one_line_to_list()
        # base_url = 'https://en.wikipedia.org/wiki/Overwatch_(video_game)'
        # yield scrapy.Request(url=base_url, callback=self.parse)
        for name in company_name:
            base_url = f'https://en.wikipedia.org/wiki/{name}'
            yield scrapy.Request(url=base_url, meta = {'company_name': name, 'url': base_url}, callback=self.parse)


    def parse(self, response):
        item = WikipediaItem()
        item['company_name'] = response.meta['company_name']
        item['url'] = response.meta['url']
        tmp1 =  re.search(r'isin=(.*?)">', response.text)
        if tmp1:
            item['isin_number'] = tmp1.group(1)
        else:
            item['isin_number'] = ''

        tmp2 = re.search(r'XNYS:(.*?)">', response.text)
        tmp3 = re.search(r'href="https://www.nasdaq.com/symbol/(.*?)">', response.text)

        if not tmp2 and not tmp3:
            item['stock'] = ''
        elif not tmp2:
            item['stock'] = tmp3.group(1)
        elif not tmp3:
            item['stock'] = tmp2.group(1)

        item['founder'] = re.search(r'title=(.*?)">', response.text)

        yield item


