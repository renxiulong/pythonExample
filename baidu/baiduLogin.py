# -*- coding: utf-8 -*-
import requests
import time
import config
import re
import json
# 获取毫秒级时间戳
def get_cur_timestamp():
    return int(round((time.time()) * 1000))
# 将callback转换为json
def parsecallback_tojson(callbackstr):
    return json.loads(re.search(r'\(.*\)', callbackstr).group().replace("(", "").replace(")", ""))
class QRLogin:
    @staticmethod
    def get_auth_cookie():
        # 封装登陆用的cookie
        login_cookies = {}
        # 随机生成的字符串、格式固定
        gid = '6F11F8D-EDD5-4A78-8B51-42D86D2DA7F4'
        headers = config.headers['passport_headers']
        init_url='https://passport.baidu.com/passApi/js/uni_login_wrapper.js?cdnversion=1561973784431&_=1561973762531'
        init_r = requests.get(init_url, headers=headers, verify=False)
        # 获取BAIDUID
        init_cookies = init_r.cookies
        login_cookies['BAIDUID'] = init_cookies['BAIDUID']
        # 获取token
        token_url = 'https://passport.baidu.com/v2/api/?getapi'
        t_params = {
            'tpl': 'mn',
            'apiver': 'v3',
            'tt': get_cur_timestamp(),
            'class': 'login',
            'gid': gid,
            'loginversion': 'v4',
            'logintype': 'dialogLogin',
            'traceid': None,
            'callback': 'bd__cbs__5kjmhe'
        }
        token_r = requests.get(token_url, headers=headers, params=t_params, cookies=login_cookies, verify=False)
        token = re.search(r'[\w]{32}', token_r.text).group()
        # 获取验证码地址
        qrcode_url = 'https://passport.baidu.com/v2/api/getqrcode'
        qr_params = {
            'lp': 'pc',
            'qrloginfrom': 'pc',
            'gid': gid,
            'callback': 'tangram_guid_1561697778375',
            'apiver': 'v3',
            'tt': get_cur_timestamp(),
            'tpl': 'mn',
            '_': get_cur_timestamp()
        }
        qrcode_r = requests.get(qrcode_url, headers=headers, params=qr_params, cookies=login_cookies, verify=False)
        signcode = re.search(r'[\w]{32}', qrcode_r.text).group()
        qrimg_url = 'https://passport.baidu.com/v2/api/qrcode?sign=%s&lp=pc&qrloginfrom=pc' % signcode
        # 将验证码保存进入图片
        with open('qrcode.jpg', 'wb') as f:
            qr_r = requests.get(qrimg_url, headers=headers, cookies=init_cookies, verify=False)
            f.write(qr_r.content)
        # 获取passid,ubi,history参数
        login_cookies['HOSUPPORT'] = '1'
        loginhistory_url = 'https://passport.baidu.com/v2/api/?loginhistory'
        loginhistory_params = {
            'token': token,
            'tpl': 'mn',
            'apiver': 'v3',
            'tt': get_cur_timestamp(),
            'loginversion': 'v4',
            'gid': gid,
            'traceid': None,
            'callback': 'bd__cbs__um4fp5'
        }
        loginhistory_r = requests.get(loginhistory_url, params=loginhistory_params, headers=headers, cookies=login_cookies, verify=False)
        loginhistory_cookiestr = loginhistory_r.headers['Set-Cookie']
        passid = None
        ubi = None
        history = None
        # 获取PASSID
        paasid_searchres = re.search(r'PASSID=(\w*[^;])', loginhistory_cookiestr)
        if paasid_searchres:
            passid = paasid_searchres.group(1)
        # 获取UBI
        ubi_searchres = re.search(r'UBI=([\w%-]*[^;])', loginhistory_cookiestr)
        if ubi_searchres:
            ubi = ubi_searchres.group(1)
        # 获取HISTORY
        history_searchres = re.search(r'HISTORY=(\w-*[^;])', loginhistory_cookiestr)
        if history_searchres:
            history = history_searchres.group(1)
        login_cookies['PASSID'] = passid
        login_cookies['UBI'] = ubi
        login_cookies['HISTORY'] = history
        # 获取扫码登陆信息，判断是否已经扫码
        channel_url = 'https://passport.baidu.com/channel/unicast'
        chanel_param = {
            'channel_id': signcode,
            'tpl': 'mn',
            'gid': gid,
            'callback': 'tangram_guid_1561776159383',
            'apiver': 'v3',
            'tt': get_cur_timestamp(),
            '_': get_cur_timestamp()
        }
        while True:
            channel_r = requests.get(channel_url, headers=headers, cookies=login_cookies, verify=False, params=chanel_param)
            channel_r_json = parsecallback_tojson(channel_r.text)
            # 获取bdussd，此处巨坑，判定扫码之后需再次请求一次否则获取不到bdussd
            if (channel_r_json['errno'] == 0) and (json.loads(channel_r_json['channel_v'])['status']) == 1:
                channel_r = requests.get(channel_url, headers=headers, cookies=login_cookies, verify=False,params=chanel_param)
                bdussd = json.loads(parsecallback_tojson(channel_r.text)['channel_v'])['v']
                break
        # 利用bdussd进行登陆
        login_url = 'https://passport.baidu.com/v3/login/main/qrbdusslogin'
        login_params = {
            'v': get_cur_timestamp(),
            'bduss': bdussd,
            'u': 'https://www.baidu.com/?tn=62095104_7_oem_dg',
            'qrcode': '1',
            'pl': 'mn',
            'apiver': 'v3',
            'tt': get_cur_timestamp(),
            'traceid': None,
            'callback': 'bd__cbs__raxv3h'
        }
        login_r = requests.get(login_url, headers=headers, params=login_params, cookies=login_cookies, verify=False)
        # 解析授权cookie
        auth_cookies = {}
        loginsuccess_cookiestr = login_r.headers['Set-Cookie']
        BDUSS = re.search(r'BDUSS=([\w%-]*[^;])', loginsuccess_cookiestr).group(1)
        STOKEN = re.search(r'STOKEN=([\w%-]*[^;])', loginsuccess_cookiestr).group(1)
        PTOKEN = re.search(r'PTOKEN=([\w%-]*[^;])', loginsuccess_cookiestr).group(1)
        auth_cookies['BDUSS'] = BDUSS
        auth_cookies['STOKEN'] = STOKEN
        auth_cookies['PTOKEN'] = PTOKEN
        with open('auth_cookies.txt', 'w') as f:
            f.write(json.dumps(auth_cookies))
        return auth_cookies
if __name__ == '__main__':
    print(QRLogin.get_auth_cookie())