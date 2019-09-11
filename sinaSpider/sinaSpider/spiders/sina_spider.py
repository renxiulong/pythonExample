#!/usr/bin/python3
# -*- coding: utf-8 -*-

import scrapy
import json


class SinaSpider(scrapy.Spider):
	name = "sina"
	allowed_domains = ["sina.com.cn"]
	# start_urls = ['https://ent.sina.com.cn/star/']
	start_urls = ['https://feed.sina.com.cn/api/roll/get?pageid=107&lid=1244&num=30&versionNumber=1.2.4&page=1&encode=utf-8']
	# https://feed.sina.com.cn/api/roll/get?pageid=107&lid=1244&num=5&versionNumber=1.2.4&page=1&encode=utf-8&callback=feedCardJsonpCallback&_=1567144901827
	urls = []
	titles = []
	start_flag = True

	def parse(self, response):
		print('self.start_flag=', self.start_flag)
		if self.start_flag:
			jsonobj = json.loads(response.body.decode('utf-8'))
			result = jsonobj['result']
			datas = result['data']
			for item in datas:
				self.titles.append(item['title'])
				self.urls.append(item['url'])

			print(self.titles)
			print(self.urls)
			self.start_flag = False
			next_page = self.urls[0]
			if next_page is not None:
				next_page = 'http://slide.ent.sina.com.cn/star/slide_4_704_321623.html'
				yield scrapy.Request(next_page, self.parse)
		else:
			contents = response.css('div#eData>dl>dd::text').extract()
			rows = len(contents)
			for num in range(0, rows, 6):
				print('url:%s' % contents[num])
				print('content:%s' % contents[num + 4])
			pass
			# print(response.text)
			# with open('sina.txt', 'wb+') as fs:
			#	fs.write(response.text.encode('utf-8'))
			# with open('content.txt', 'wb+') as f:
			#	title = response.css('h1.main-title::text').extract_first()
			#	print('title:%s' % title)
			#	content = response.css('div.quotation>p::text').extract_first()
			#	print('content:%s' % content)
			#	f.write(title.encode('utf-8'))
			#	f.write(content.encode('utf-8'))
