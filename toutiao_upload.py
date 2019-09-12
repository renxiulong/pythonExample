#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
title: '今日头条写书稿'
author: '任秀龙'
date: '2019-08-27'
"""

import requests
import json
import time
from urllib3 import encode_multipart_formdata


def send_post():
    # url = 'https://mp.toutiao.com/tools/upload_picture/?type=ueditor&pgc_watermark=1&action=uploadimage&encode=utf-8'
    url = 'https://mp.toutiao.com/tools/upload_picture/?type=ueditor&pgc_watermark=0&action=uploadimage&encode=utf-8'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        'Connection': 'keep-alive',
        'Content-Length': '156080',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryV2p9rx4rrNjLJpnc',
        'Cookie': 'tt_webid=6652114556993373708; gr_user_id=fb23d48d-8c39-477e-b9ca-473a7c01fdcf; grwng_uid=300c672c-254f-4037-9810-d1294c6648fe; __tea_sdk__ssid=e3c244c0-1852-4f46-8679-79b3b22d8086; _ga=GA1.2.1658463968.1548834667; _ba=BA0.2-20190130-5110e-gUUdk1aB6qeP38OXDM7d; uuid="w:85b3f70ec1f44e79847f05fc8d70f8e1"; passport_auth_status=72bc0bce8d8f948d41d48198a4172aff; sso_auth_status=e22713719a8778d85a2640d3ae0f03c7; sso_uid_tt=b3a49c7d56ae95737047618a0550ca0a; toutiao_sso_user=abf2bcf788428f3e3c4ac19f12d09c87; _mp_test_key_1=1f6264f881a98d6ad20fa6f12014c791; sid_guard=abf2bcf788428f3e3c4ac19f12d09c87%7C1566617729%7C4828158%7CSat%2C+19-Oct-2019+00%3A44%3A47+GMT; uid_tt=b3a49c7d56ae95737047618a0550ca0a; sid_tt=abf2bcf788428f3e3c4ac19f12d09c87; sessionid=abf2bcf788428f3e3c4ac19f12d09c87; _mp_auth_key=e22713719a8778d85a2640d3ae0f03c7; _mp_auth_key=e22713719a8778d85a2640d3ae0f03c7',
        'Host': 'mp.toutiao.com',
        'Origin': 'https://mp.toutiao.com',
        # 'Referer': 'https://mp.toutiao.com/profile_v3/graphic/publish',
        'Referer': 'https://mp.toutiao.com/profile_v3/graphic/resource-manager',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
    }
    # params = {'pgc_watermark': 1, 'type': 'ueditor', 'action': 'uploadimage', 'encode': 'utf-8'}
    params = {'pgc_watermark': '0', 'type': 'ueditor', 'action': 'uploadimage', 'encode': 'utf-8'}
    data = {
        'type': 'image/jpeg',
    }
    image_url = 'sinaSpider\\slide_4_704_321623\\06d6-iekuaqu0298971.jpg'
    # with open(image_url, 'rb') as f:
    #    imageData = f.read()
    #    data['upfile'] = '(' + imageData + ')'
    files = {'upfile': ('type', open(image_url, 'rb'), 'image/jpeg', {})}

    f = {
        "type": (None, "image/jpeg"),
        "upfile": ("06d6-iekuaqu0298971.jpg", open("sinaSpider\\slide_4_704_321623\\06d6-iekuaqu0298971.jpg", "rb"), "image/jpeg")
    }

    # payload = "------WebKitFormBoundaryV2p9rx4rrNjLJpnc\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\nimage/jpeg\r\n------WebKitFormBoundaryV2p9rx4rrNjLJpnc\r\nContent-Disposition: form-data; name=\"upfile\"; filename=\"1.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n\r\n------WebKitFormBoundaryV2p9rx4rrNjLJpnc--"
    payload = "------WebKitFormBoundaryV2p9rx4rrNjLJpnc\r\nContent-Disposition: form-data; name=\"upfile\"; filename=\"06d6-iekuaqu0298971.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n\r\n------WebKitFormBoundaryV2p9rx4rrNjLJpnc--"

    response = requests.post(url, headers=headers, params=params, data=payload)
    print(json.dumps(response.text, ensure_ascii=False))
    print(response.text)


if __name__ == '__main__':
    send_post()