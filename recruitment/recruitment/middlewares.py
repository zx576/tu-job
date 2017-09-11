# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random

# logger = logging.getLogger(__name__)


class RecruitmentSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ProxyMiddleWare(object):
    
    # proxy middleware
    # function: add a proxy on each request

    def __init__(self):
        
        self.proxies = [
                "http://111.13.2.131:80",
                "http://61.152.81.193:9100",
                "http://162.243.18.46:3128",
                "http://183.232.65.202:3128",
                "http://219.149.46.151:3128",
                "http://111.13.2.131:80",
                "http://61.152.81.193:9100",
                "http://162.243.18.46:3128",
                "http://183.232.65.202:3128",
                "http://219.149.46.151:3128",  
                "http://121.69.3.102:8080",
                "http://111.13.109.27:80",
                "http://222.196.33.254:3128",
                "http://111.13.7.120:80",
                "http://111.13.2.138:80",
                "http://111.13.7.117:80",
                "http://111.13.7.119:80",
                "http://223.20.215.217:9000",
                "http://61.136.163.245:3128",
                "http://111.13.7.122:80",
                "http://111.13.7.123:80",
                "http://106.119.0.244:8080",
                "http://93.91.112.185:80",
                "http://120.77.255.133:8088",

                ]

    def process_request(self, request, spider):

        # select a proxy randomly
        proxy = random.choice(self.proxies)

        # add it into meta 
        request.meta['proxy'] = proxy 

        # test if it works
        print('construct a request with proxy {}'.format(request.meta['proxy']))

    def process_exception(self, request, exception, spider):

        invaild_ip = request.meta['proxy']
        self.proxies.remove(invaild_ip)
        request.meta['proxy'] = random.choice(self.proxies)
        new_req = request.copy()

        return new_req

    


# 更改 UA 中间件
class UAMiddleWare():
    def __init__(self):

        self.ua = [
                # safari 5.1 – MAC
                'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                # safari 5.1 – Windows
                'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                # Firefox 38esr
                'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
                # IE 11
                'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
                # IE 9.0
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
                # IE 8.0
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
                # IE 7.0
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
                # IE 6.0
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
                # Firefox 4.0.1 – MAC
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                # Firefox 4.0.1 – Windows
                'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                # Opera 11.11 – MAC
                'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
                # Opera 11.11 – Windows
                'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
                # Chrome 17.0 – MAC
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
                # 傲游（Maxthon）
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
                # 腾讯TT
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
                # 世界之窗（The World） 2.x
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
                # 世界之窗（The World） 3.x
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
                # 搜狗浏览器 1.x
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
                # 360浏览器
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
                # Avant
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
                # Green Browser
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'

            ]

    def process_request(self, request, spider):
        request.headers["User-Agent"] = random.choice(self.ua)
        print("construct request with UA: {}".format(request.headers))



