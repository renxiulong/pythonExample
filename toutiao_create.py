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


def send_post():
    url = 'https://mp.toutiao.com/core/article/edit_article_post/?source=mp&type=article'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        'Connection': 'keep-alive',
        'Content-Length': '654',
        'Content-Type': 'application/x-www-form-urlencoded;charset = UTF-8',
        'Cookie': 'tt_webid=6652114556993373708;gr_user_id=fb23d48d-8c39-477e-b9ca-473a7c01fdcf;'
                  'grwng_uid=300c672c-254f-4037-9810-d1294c6648fe;__tea_sdk__ssid=e3c244c0-1852-4f46-8679-79b3b22d8086;'
                  '_ga = GA1.2.1658463968.1548834667;_ba = BA0.2-20190130-5110e-gUUdk1aB6qeP38OXDM7d;'
                  'uuid="w:85b3f70ec1f44e79847f05fc8d70f8e1";passport_auth_status=72bc0bce8d8f948d41d48198a4172aff;'
                  'sso_auth_status=e22713719a8778d85a2640d3ae0f03c7;sso_uid_tt=b3a49c7d56ae95737047618a0550ca0a;'
                  'toutiao_sso_user=abf2bcf788428f3e3c4ac19f12d09c87;mp_test_key_1=1f6264f881a98d6ad20fa6f12014c791;'
                  'sid_guard=abf2bcf788428f3e3c4ac19f12d09c87%7C1566617729%7C4828158%7CSat%2C+19-'
                  'Oct-2019+00%3A44%3A47+GMT;uid_tt=b3a49c7d56ae95737047618a0550ca0a;'
                  'sid_tt=abf2bcf788428f3e3c4ac19f12d09c87;sessionid=abf2bcf788428f3e3c4ac19f12d09c87;'
                  '_mp_auth_key=e22713719a8778d85a2640d3ae0f03c7;_mp_auth_key=e22713719a8778d85a2640d3ae0f03c7;'
                  'ptcn_no=0d198a5e7dcdad68ed080145c5d04845',
        'Host': 'mp.toutiao.com',
        'Origin': 'https://mp.toutiao.com',
        'Referer': 'https://mp.toutiao.com/profile_v3/graphic/publish',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
    }
    params = {'source': 'mp', 'type': 'article'}
    data = {
        'article_type': 0,
        'title': '天若有情天亦老第五弹',
        'content': '<p>人间正道是沧桑ok，钟山风雨起苍黄，百万雄师过大江 </p>',
        'activity_tag': 0,
        'title_id': '1566870204522_1620168526573582',
        'claim_origin': 0,
        'article_ad_type': 3,
        'add_third_title': 0,
        'recommend_auto_analyse': 0,
        'tag': '',
        'article_label':'',
        'is_fans_article': 0,
        'quote_hot_spot': 0,
        'govern_forward': 0,
        'push_status': 0,
        'push_android_title': '',
        'push_android_summary': '',
        'push_ios_summary:': '',
        'timer_status': 0,
        'timer_time': time.strftime('%Y-%m-%d %H:%M', time.localtime()),# '2019-08-27 22:43',
        'praise': 0,
        'community_sync': 0,
        'column_chosen': 0,
        'pgc_id': 0,
        'qy_self_recommendation': 0,
        'pgc_feed_covers': [],
        'from_diagnosis': 0,
        'origin_debut_check_pgc_normal': 0,
        'tree_plan_article': 0,
        'save': 0
    }
    response = requests.post(url, headers=headers, params=params, data=data)
    print(json.dumps(response.text, ensure_ascii=False))


if __name__ == '__main__':
    send_post()