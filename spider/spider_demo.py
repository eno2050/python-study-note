# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author:eno2050
# email:117908549@qq.com
# 2017-10-1

import urllib
import urllib2

# 定义一个函数获取get请求
def use_get_res(url):
    request = urllib2.Request(url)
    res = urllib2.urlopen(request)
    print res.read()

url = "http://www.hao123.com"
use_get_res(url)
