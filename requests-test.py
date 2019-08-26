#-*- coding:utf-8 -*-

import requests
import time

#print(time.time())
#t = time.localtime()
#print(t)
#print(t.tm_year)
# r = requests.get('https://api.github.com/events')

jianshu_url = 'https://www.jianshu.com/p/111d5fd45487'
headers = {
    #'Origin': "https://www.jianshu.com",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605"
                  ".1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15",

    'Referer': jianshu_url,
    #'Content-Type': "text/plain",
    #'Cache-Control': "no-cache"data='uuid=97d8a8c8-0c81-4aeb-9172-3d4f510fc5e6', 
}
r = requests.post('https://www.jianshu.com/notes/111d5fd45487/mark_viewed.json', headers=headers)
print(r.status_code)
print(r.text)
print(r.content)
