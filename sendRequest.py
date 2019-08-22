# -*- coding: utf-8 -*-
__author__ = '任秀龙'

import requests
from requests_html import HTMLSession


headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'zh-CN,zh;q=0.9',
	'cache-control': 'max-age=0',
	'cookie': '__yadk_uid=1esvOsAEDnIAddxGthc77vZn3N2jDLn2; read_mode=day; default_font=font2; locale=zh-CN; _m7e_session_core=ce4b7f0936d8b63130687139783f6e3f; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1566291676,1566371802,1566372712,1566372809; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fp%2F111d5fd45487; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ca78df33d484-0f7396fe88a85d-a7f1a3e-2073600-16ca78df33e2be%22%2C%22%24device_id%22%3A%2216ca78df33d484-0f7396fe88a85d-a7f1a3e-2073600-16ca78df33e2be%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22%22%7D; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1566377663',
}
#res = requests.get('https://www.jianshu.com/p/111d5fd45487', headers=headers)
#print(res.status_code) # 状态码
#print(res.headers['content-type']) # 响应header
#print(res.encoding) # 编码
#print(res.text) # 内容，文本形式

session = HTMLSession()
r = session.get('https://www.jianshu.com/p/111d5fd45487');
r.html.render();