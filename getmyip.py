#!/usr/bin/python
# -*- coding:utf8 -*-
# by rxl

import urllib2
import re

url = urllib2.urlopen("http://txt.go.sohu.com/ip/soip")
text = url.read()
ip = re.findall(r'\d+.\d+.\d+.\d+', text)

print ip[0]