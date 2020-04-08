# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi



class WikipediaPipeline(object):
    def __init__(self):
        dbparms = dict(
            host='localhost',
            db='wiki',
            user='root',
            passwd='Haha123!',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )

        self.dbpool = adbapi.ConnectionPool("pymysql", **dbparms)


    def process_item(self, item, spider):
        company_name = item['company_name']
        rank = item['rank']
        overview = item['overview']
        founder = item['founder']
        sector = item['sector']
        job_created = item['jobs_created']
        website = item['website']
        HQ = item['HQ']

        import pandas as pd
        from sqlalchemy import create_engine

        try:
            data = pd.DataFrame({"company": company_name, "rank": rank,
                                 "overview": overview, "founder": founder, "sector": sector, "job_created": job_created, "website": website, "HQ": HQ}, index=[0])
            connect = create_engine('mysql+pymysql://root:Haha123!@localhost:3306/wiki?charset=utf8')
            pd.io.sql.to_sql(data, 'ycomb', connect, schema='wiki', if_exists='append')

        except Exception as err:
            print('Insert Failed')
            print(err)

        return item
