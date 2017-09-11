# -*- coding: utf-8 -*-
import scrapy
import json


class LagouSpider(scrapy.Spider):
	
	# 拉勾爬虫
	# refer: headers 中的参数
	# dct : post 请求中的参数， 包含 页码 pn 与 搜索关键字 kd 参数
	# signal : 继续爬取的信号， 爬取的过程中页码会不停加一，
	# 如果判断无返回内容时，将 signal 赋值为 false 停止继续抓取。

	name = 'lagou'
	allowed_domains = ['lagou.com']

	def __init__(self):

		super(LagouSpider, self).__init__()
		self.signal = True

	# 开始请求
	def start_requests(self):
		start_url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false&isSchoolJob=0'
		refer = 'https://www.lagou.com/jobs/list_Python?px=default&city=%E5%85%A8%E5%9B%BD'
		ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
		dct = {
			'kd': 'Python'
			}
		count = 10
		while True:
			# 不再继续往下请求
			if not self.signal:
				break
			dct['pn'] = str(count)
			# post 请求使用 FormRequest 方法
			yield scrapy.FormRequest(
				url=start_url,
				formdata=dct,
				headers={
					'Referer': refer,
					'User-Agent':ua
					},
				callback=self.parse,
				dont_filter=True
			)

			count += 1
			# break

	def parse(self, response):
		
		# 解析返回内容
		res = json.loads(response.body_as_unicode())
		try:	
			lst_result = res['content']['positionResult']['result']
		except:
			print(res)
			return 
		# 如果列表为空，则说明已经拿到了所有资源
		# 将信号置为 False 
		if not lst_result:
			self.signal = False
			return
		
		# 逐条解析
		for i in lst_result:

			item = {}
			item['source'] = '拉勾'
			item['name'] = i.get('positionName')
			item['salary'] = i.get('salary')
			item['city'] = i.get('city')
			item['years'] = i.get('workYear')
			item['degree'] = i.get('education')
			item['companyname'] = i.get('companyFullName')
			item['companysize'] = i.get('companySize', -1)
			item['industry'] = i.get('industryField')
			item['keywords'] = '-'.join(i.get('positionLables'))
			item['wealfare'] = '-'.join(i.get('companyLabelList'))

			yield item