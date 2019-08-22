import config
import requests
import re
import json
import time
from pyquery import PyQuery as pq
# 获取毫秒级时间戳
def get_cur_timestamp():
    return int(round((time.time()) * 1000))

class TieBa:

    tieba_headers = config.headers['tieba_headers']
    passport_headers = config.headers['passport_headers']
    @staticmethod
    def auto_sign():
        with open('auth_cookies.txt', 'r') as f:
            cookiesstr = f.read()
            passport_authcookies = json.loads(cookiesstr)
            auth_cookies=TieBa.get_tieba_authcookies(passport_authcookies)

        mytb_names = list(TieBa.get_mytbdict(auth_cookies).values())
        # 签到
        for tb_name in mytb_names:
            sign_url = 'https://tieba.baidu.com/sign/add'
            sign_data = {
                'ie': 'utf-8',
                'kw': tb_name,
                'tbs': '6868ce0283f2fb151561865643'
            }
            sign_res=requests.post(sign_url, data=sign_data, cookies=auth_cookies, headers=config.headers['tieba_headers'])
            print(sign_res.text)

    @staticmethod
    def get_tieba_authcookies(passport_authcookies):

        # 获取授权cookie
        with open('auth_cookies.txt', 'r') as f:
            cookiesstr = f.read()
            auth_cookies = json.loads(cookiesstr)

        # 首次访问贴吧首页时会重定向到passprot.baidu.com
        tieba_url = 'https://tieba.baidu.com/index.html'
        tieba_r = requests.get(tieba_url, cookies=passport_authcookies, headers=TieBa.tieba_headers,allow_redirects=False)
        # 提取cookie，添加到授权cookie中
        auth_cookies['TIEBA_USERTYPE'] = tieba_r.cookies['TIEBA_USERTYPE']

        # 获取重定向地址，此时为passport.baidu.com，访问改地址后会再次重定向
        pass_url = tieba_r.headers['Location']
        pass_r = requests.get(pass_url, headers=TieBa.passport_headers, cookies=passport_authcookies,
                              allow_redirects=False)

        # 获取headers中的贴吧STOKEN，并设置进auth_cookie
        tieba_stoken_url = pass_r.headers['Location']
        tieba_stoken_r = requests.get(tieba_stoken_url, headers=TieBa.tieba_headers, cookies=passport_authcookies,
                                      allow_redirects=False)
        STOKEN = re.search(r'STOKEN=(\w*[^;])', tieba_stoken_r.headers['Set-Cookie']).group(1)
        passport_authcookies['STOKEN'] = STOKEN

        return passport_authcookies
    @staticmethod
    def get_mytbdict(tieba_authcookies):
        tieba_url = 'https://tieba.baidu.com/index.html'
        with open('auth_cookies.txt', 'r') as f:
            cookiesstr = f.read()
            passport_authcookies = json.loads(cookiesstr)
            auth_cookies = TieBa.get_tieba_authcookies(passport_authcookies)

        # 利用新token请求首页，获取关注的贴吧列表
        tieba_index_r = requests.get(tieba_url, cookies=auth_cookies, headers=config.headers['tieba_headers'])
        content = tieba_index_r.text
        pattern = re.compile(r"{\"user_id\"[^}]*\"is_sign\":\d}")
        tbinfo_list = pattern.findall(content)

        # 用set存放提取出的贴吧列表，防止重复
        mytb ={}
        for item in tbinfo_list:
            json_item = json.loads(item)
            forum_name = json_item['forum_name']
            forum_id = json_item['forum_id']
            mytb[forum_id]=forum_name

        return mytb

if __name__ == '__main__':
    TieBa.auto_sign()

