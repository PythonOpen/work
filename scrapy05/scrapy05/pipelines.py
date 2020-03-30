# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class Scrapy05Pipeline(object):
    def process_item(self, item, spider):
        return item


class QQPipeline(object):
    # 初始化配置数据库
    def __init__(self):
        self.client = pymongo.MongoClient(
            host=settings['MONGO_HOST'],
            port=settings['MONGO_PORT']
        )
        self.client.admin.authenticate(
            settings['MONGO_USER'],
            settings['MONGO_PWD']
        )
        # 获得数据库的句柄
        self.db = self.client[settings['MONGO_DB']]
        # 获得collection的句柄
        self.coll = self.db[settings['MONGO_COLL']]

        def process_item(self, item, spider):
            postItem = dict(item)
            # 查到数据库里面
            self.coll.insert(postItem)
            return item

