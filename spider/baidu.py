# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author:eno2050
# email:117908549@qq.com
# 2017-10-1

import urllib2

req = urllib2.Request('http://blog.csdn.net/asddsada')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError as e:
    print e.code
    print e.reason
