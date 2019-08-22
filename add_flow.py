# -*- coding: utf-8 -*-
"""简书刷阅读数
-------------------------------------------------
   File Name：     add_flow
   Description :
   Author :       MrLonelyZC88
   date：          2018/10/26
-------------------------------------------------
   Change Activity:
                   2018/10/26:
-------------------------------------------------
"""
import requests
import re
import urllib.request
import urllib.parse as urlparse


def download(url, user_agent='iosdevlog', proxy=None, num_retries=2):
    """Download function with support for proxies"""
    # print('Downloading:', url)
    headers = {'User-agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    opener = urllib.request.urlopen(request)
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib.ProxyHandler(proxy_params))
    try:
        html = opener.read().decode('utf-8')
    except urllib.error.URLError as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                html = download(url, user_agent, proxy, num_retries-1)
    return html


# 阅读数
def crawl_views_count(jianshu_url):
    jianshu = download(jianshu_url)
    views_count = re.search(r'views_count":(\d+),', jianshu).group(1)
    print("views_count = " + views_count)


# uuid
def crawl_uuid(jianshu_url):
    jianshu = download(jianshu_url)
    uuid = re.search(r'uuid":"([a-z0-9\-]+?)"}', jianshu).group(1)

    return uuid


if __name__ == '__main__':
    #jianshu_url = 'https://www.jianshu.com/p/xxxxxxxx'
    jianshu_url = 'https://www.jianshu.com/p/111d5fd45487'
    max_count = 100  # 想刷的阅读次数

    uuid = crawl_uuid(jianshu_url)
    # print("uuid = " + uuid)
    mark_viewed_url = jianshu_url.replace("/p/", "/notes/") + '/mark_viewed.json'
    # print("mark_viewed_url = " + mark_viewed_url)
    payload = "uuid=" + uuid
    # print("payload = " + payload)

    headers = {
        'Origin': "https://www.jianshu.com",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605"
                      ".1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15",

        'Referer': jianshu_url,
        'Content-Type': "text/plain",
        'Cache-Control': "no-cache"
    }

    for _ in range(0, max_count):
        requests.request("POST", mark_viewed_url, data=payload, headers=headers)
        crawl_views_count(jianshu_url)


