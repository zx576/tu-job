## 爬取招聘网站(三) - 搭建数据库管道

#### 文章结构

- 编写连接 mysql 部分代码
- 测试连接是否成功
- 编写实际的数据模型代码


#### 思路与代码

参考： [scrapy配置mongodb](http://crossincode.com/school/lesson/167/)

这里详细提一下 scrapy 配置 mysql. 并且在正式爬取之前，我们先编写一些测试代码检测是否成功连接数据库。


##### 1、配置基本信息

在配置基本信息之前，我默认你已经安装好了 mysql ， 未安装 mysql 的同学查看

- [windows安装mysql](http://www.jb51.net/article/39188.htm)
- [ubuntu安装mysql](http://www.linuxidc.com/Linux/2016-07/133128.htm)
- [mac安装mysql](http://www.jb51.net/article/103841.htm)


然后建立了一个名为 `job` 的数据库, 如果没有的话

-  [请点击我](https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04)


settings.py

 ```python

ROBOTSTXT_OBEY = False

 # ...

 HOST = 'localhost'
 NAME = 'job'           # 数据库名  ---------- #
 USER = 'mysqlname'     # 用户名    自定义修改  #
 PASSWORD = 'password'  # 密码     ---------- #


 # ...

 ```

##### 2、编写一个简单的数据模型

这里我们使用 **peewee** 取代传统的 scrapy items 来编写数据映射,还未了解 peewee 的请点击 [peewee document](http://docs.peewee-orm.com/en/latest/)


items.py

```python

from peewee import *
from .settings import USER,PASSWORD,NAME

# 配置基础设置
db = MySQLDatabase(
                    database=NAME,
                    user=USER,
                    passwd=PASSWORD,
                    host='localhost'
                )


# 建立一个基本的数据模型
class BaseModel(Model):
    class Meta:
        database = db


# 测试用
class TestItem(BaseModel):

    field1 = CharField()
    field2 = IntegerField()


# 连接数据库
db.connect()

```

##### 3、配置 pipelines

```python
from .items import TestItem

class TestPipeline(object):
    '''for test'''
    def process_item(self, item, spider):
        #  判断表是否存在
        if not TestItem.table_exists():
            TestItem.create_table()

        TestItem.create(
            field1=item['field1'],
            field2=item['field2'],

        )
        return item

```

##### 4、生成一个测试爬虫

```
$ scrapy genspider testitem baidu.com

```

recruitment/recruitment/spiders/testitem.py

```python
import scrapy


class TestitemSpider(scrapy.Spider):
    name = 'testitem'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    # 使用自定义设置指定 pipelines
    custom_settings = {
        'ITEM_PIPELINES': {
           'recruitment.pipelines.TestPipeline': 300,
        }
    }

    def parse(self, response):
        # 测试用例
        item = {}
        item['field1'] = 'qwer'
        item['field2'] = 4
        yield item


```

##### 5、test your code / 测试代码

```

$ scrapy crawl testitem

```

运行无误后，即可以正式编写实际用到的代码。


#### 6、建立实际的数据模型

测试之后， 根据上一节的分析结果， 我们开始设计数据模型

items.py

```python
class RecruitmentItem(BaseModel):

    source = CharField(verbose_name='信息来源')
    name = CharField(verbose_name='职位名')
    # ..

    # 防止爬取或分析的过程中有新的需求
    # 建立两个保留字段
    re1 = CharField(verbose_name='保留字段一')
    re2 = CharField(verbose_name='保留字段二')

```

#### summary / 总结

在本节内容中，我们讨论了如何连接　scrapy 到 mysql 上，如何使用 peewee 取代传统的 items，　最后我们编写了实际了数据库映射代码。

在下一节，我们将开始抓取 lagou 网站，保存数据到数据库中。
