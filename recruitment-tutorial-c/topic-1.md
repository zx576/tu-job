## 爬招聘网站(一)


在之前爬虫课程中，很多同学反映，课程中的内容不够贴合实际。于是我们想着如何解决这一问题，讨论之后就有了本系列教程。
本系列教程完全从实际出发，重点介绍从 0 开始到最后抓下数据这一过程中，如何解决碰到的实际问题。

比如：

- 如何连接 scrapy 到 mysql 或者 mongodb
- 如何自己实现一个中间件
- 如何分析 ajax 加载的网页
等等


#### 目的

- 更加熟悉 Python 语言
- 简单的项目规划能力
- 能对付简单的反爬手段
- 能分析基本的 ajax 加载的网页

#### 所需 Python 包

scrapy 自不必说，简单提一下 peewee, peewee 是一个 python 下的 ORM 库，它能够让我们以更加 python 的方式与数据库交互，详细的介绍请点击以下链接。

- scrapy
- [peewee](http://docs.peewee-orm.com/en/latest/)

如果你还不够了解 scrapy, 请点击以下链接：

- [官方文档](https://doc.scrapy.org/en/latest/intro/tutorial.html)
- [scrapy框架介绍-视频](http://crossincode.com/school/lesson/123/)
- [scrapy框架介绍-图文](http://crossincode.com/school/lesson/156/)


#### 系统环境

- linux / windows / macos
- python 3+

#### 选择爬取网站

- [猎聘](https://c.liepin.com)
- [拉钩](https://www.lagou.com/)
- [智联](http://ts.zhaopin.com/jump/index.html)
- [前程无忧](http://www.51job.com)
- [boss直聘](http://www.zhipin.com/?sid=sem_pz_bdpc_index)

可能还有其他的招聘网站，你大可以选择你想爬的站。本项目中，因为要演示如何分析 ajax 加载的网页，所以我选择了 拉钩 作为示例。


#### 总结

这本节内容中，我们做了一些项目准备工作，看起来没什么难度。在下一节内容中，我们将试着分析一下 lagou 的 ajax 加载形式。
