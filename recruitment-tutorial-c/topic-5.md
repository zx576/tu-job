## 爬取招聘网站(五)代理中间件


#### 文章结构


- 构建一个简单的代理中间件
- 测试中间件是否成功运行



#### 思路

1. 写一个中间件
2. 在设置中注册该中间件
3. 创建一个爬虫测试中间件是否正常运行

#### produce a new middleware

IP 代理可以从编程教室实验室获取，网址为 `http://lab.crossincode.com/proxy/get` ， 当然也可以从其他网站获取。


middleware.py

```python

class ProxyMiddleWare(object):

    # proxy middleware
    # function: add a proxy on each request

    def __init__(self):

        self.proxies = [
                "http://111.13.2.131:80",
                "http://61.152.81.193:9100",
                "http://162.243.18.46:3128",
                "http://183.232.65.202:3128",
                "http://219.149.46.151:3128"
                ]

    def process_request(self, request, spider):

        # 随机选择一个代理
        proxy = random.choice(self.proxies)

        # 添加代理
        request.meta['proxy'] = proxy

        # 测试时输出看看
        print('construct a request with proxy {}'.format(request.meta['proxy']))

```

这里只是简单的在请求的时候加入了 IP， 更细致一些，应该加入异常处理的代码，即，如果请求出错了，应该更换 IP 重新请求，同时删除该无效的IP， 这里的代码，先交给读者自己去实现。

创建一个测试爬虫

```
$ scrapy genspider httpbin httpbin.org/ip

```

请求 ip 测试网站 `httpbin.org/ip` ， 如果代理成功了，则会返回目前的代理 IP。[try it](http://httpbin.org/ip)

爬虫代码如下：

spiders/httpbin.py

```python

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org/ip']
    # !!! url must be https://httpbin.org/ip
    start_urls = ['https://httpbin.org/ip']

    def parse(self, response):
        print(response.body)

```

注册代理中间件

settings.py

```python

# ...
DOWNLOADER_MIDDLEWARES = {
   'recruitment.middlewares.ProxyMiddleWare': 500,
}

# ...

```
最后，运行代码，可以看到结果

```

construct a request with proxy http://183.232.65.202:3128
2017-09-07 09:58:48 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://httpbin.org/ip> (referer: None)
b'{\n  "origin": "183.232.65.202"\n}\n'
2017-09-07 09:58:49 [scrapy.core.engine] INFO: Closing spider (finished)


```
IP代理中间件确实有效。

#### 动手写一个更换 user-agent 的中间件

上面我们说了如何构造一个代理中间件，在实际的爬虫中， user-agent 最好也能进行更换，请您模仿着上面的代码自己写一个吧。


#### 运行代码

中间件写好并注册到 settings 之后，我们在运行一下 lagou 爬虫。
运行的过程中发现，虽然偶有响应错误的情况，但总体来说，程序能够一直运行下去。

#### 总结

在本节内容中，我们向你展示了如何去构造一个代理中间件， 但应注意到，你没有必要为每个项目都这么做，这完全取决于实际情况，在大多数情况下，仅仅延迟请求间隔就可以了。

最后，招聘网站的爬取部分代码就已经全部完成了, 数据展示部分请查看[视频](http://crossincode.com/school/lesson/126/).
代码以及结果可查看 analysis 文件夹下的文件。