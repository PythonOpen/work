# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class Scrapy02Pipeline(object):
    def process_item(self, item, spider):
        return item


class MeijuPipeline(object):
    def __init__(self):
        self.file = open('meiju.json', 'wb')
    '''
    此方法必须被实现
    用来具体处理item内容
    且必须返回一个item
    '''
    def process_item(self, item, spider):
        with open('meiju.json', 'a', encoding='utf-8')as f:
            json.dump(dict(item), f, ensure_ascii=False)
            f.write(',\n')
        return item
