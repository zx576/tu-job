# coding=utf-8

from models import RecruitmentItem


class Analysis(object):

	def _salary(self):

		query = RecruitmentItem.select()
		for i in query:
			print(i.industry)

	


if __name__ == '__main__':
	ana = Analysis()
	ana._salary()

