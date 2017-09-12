# coding=utf-8

from models import RecruitmentItem
import re

class Analysis(object):

	def _salary(self):

		# 统计薪水
		# 方法： 
		# 第一步： 使用正则找出所有匹配的薪水数字
		# 第二步： 使用统计薪水所处的区间
		query = RecruitmentItem.select()
		pattern = re.compile(r'(\d+)k')
		res = []
		for i in query:
			res_ = [int(i) for i in re.findall(pattern, i.salary)]
			res.extend(res_)
			
		res.sort()
		
		# 统计薪水区间
		dct = {}
		pre_fix = [0, 5, 10, 15, 20, 25, 30, 100000]
		for num in res:
			for idx in range(len(pre_fix)):
				if num < pre_fix[idx]:
					if pre_fix[idx] == 100000:
						key = '{0}k+'.format(pre_fix[idx-1])
					elif pre_fix[idx] == 5:
						key = '{0}k-'.format(pre_fix[idx])
					else:
						key = '{0}k-{1}K'.format(pre_fix[idx-1], pre_fix[idx])
						
					num = dct.setdefault(key, 0)
					dct[key] += 1
					break

		print(dct)
		return dct

	def _city(self):

		# 统计城市
		# 1. 统计抓到的所有城市及其数量
		#　２. 某些城市数量较少，所以把所有职位数量小于　10　的城市归于　其他城市
		query = RecruitmentItem.select()

		# 初次统计结果
		dct = {}
		for i in query:
			city = i.city
			citycount = dct.setdefault(city, 0)
			dct[city]  = citycount + 1
		
		# 优化结果
		res = {}
		for k,v in dct.items():
			if v > 10:
				res[k] = v
			else:
				othercount = res.setdefault('其他城市', 0)
				res['其他城市'] = othercount + v

		print(res)
		return res
			


if __name__ == '__main__':
	ana = Analysis()
	# ana._salary()
	ana._city()

