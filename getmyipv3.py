#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: rxl

import requests
import re

r = requests.get('http://txt.go.sohu.com/ip/soip')
ip = re.findall(r'\d+.\d+.\d+.\d+', r.text)
print(ip[0])