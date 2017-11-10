# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author:eno2050
# email:117908549@qq.com
# 2017-10-1

import urllib2
import cookielib

# 创建一个cookie
cookie = cookielib.CookieJar()
# 利用urllib2 来处理这个cookie
hander = urllib2.HTTPCookieProcessor(cookie)
# 利用cookie 创建一个opener 实例
opener = urllib2.build_opener(hander)
# 利用实例的open方法，打开一个网址
res = opener.open('http://www.baidu.com')
for item in cookie:
    print item.value
