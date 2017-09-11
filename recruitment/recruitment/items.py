# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from peewee import *
from .settings import USER,PASSWORD,NAME


db = MySQLDatabase(
                    database=NAME,
                    user=USER,
                    passwd=PASSWORD,
                    host='localhost'
                )


class BaseModel(Model):
    # base model for other items

    class Meta:
        database = db


class TestItem(BaseModel):
    # for test

    field1 = CharField()
    field2 = IntegerField()


class RecruitmentItem(BaseModel):

    source = CharField(verbose_name='信息来源')
    name = CharField(verbose_name='职位名')
    salary = CharField(verbose_name='薪水')
    city = CharField(verbose_name='工作地点')
    is_negotiable = BooleanField(verbose_name='是否面议', default=False)
    years = CharField(verbose_name='工作年限')
    degree = CharField(verbose_name='学历')
    description = TextField(verbose_name='职位描述')
    companyname = CharField(verbose_name='公司名')
    companySize = CharField(verbose_name='公司规模')
    industry = CharField(verbose_name='行业')
    keywords = CharField(verbose_name='职位关键字')
    wealfare = CharField(verbose_name='职位福利')

    # 防止爬取或分析的过程中有新的需求
    # 建立两个保留字段
    re1 = CharField(verbose_name='保留字段一', default='')
    re2 = CharField(verbose_name='保留字段二', default='')


db.connect()

'''

class RecruitmentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

'''
