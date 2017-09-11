# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .items import TestItem, RecruitmentItem

class RecruitmentPipeline(object):

    def process_item(self, item, spider):
        if not RecruitmentItem.table_exists():
            RecruitmentItem.create_table()

        RecruitmentItem.create(
            source=item['source'],
            name=item['name'],
            salary=item['salary'],
            city=item['city'],
            years=item['years'],
            degree=item['degree'],
            companyname=item['companyname'],
            companySize=item['companysize'],
            industry=item['industry'],
            keywords=item['keywords'],
            wealfare=item['wealfare'],
            description=''
        )
        return item


class TestPipeline(object):

    def process_item(self, item, spider):
        if not TestItem.table_exists():
            TestItem.create_table()

        TestItem.create(
            field1=item['field1'],
            field2=item['field2'],

        )
        return item