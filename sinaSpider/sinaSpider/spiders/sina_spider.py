#!/usr/bin/python
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
	def parse(self, response):
		jsonObj = json.loads(response.body.decode('utf-8'))
		result = jsonObj['result']
		datas = result['data']
		for item in datas:
			print(item['title'])
			print(item['url'])