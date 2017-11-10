# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author:eno2050
# email:117908549@qq.com
# 2017-10-1

import urllib2
import urllib
import cookielib

filename = "cookie.txt"
# 创建一个cookie容器
cookie = cookielib.LWPCookieJar(filename)
# 创建处理cookie的hander
hander = urllib2.HTTPCookieProcessor(cookie)
# 通过hander创建一个opener
opener = urllib2.build_opener(hander)
# 要访问的链接
url = "http://m2.plcxyy.com/BRsN40vdBe/login.php"
# 发送的数据
data = {
    "userid":"admin",
    "pwd":"cbiTeaLW3Y"
}
data = urllib.urlencode(data)
req = urllib2.Request(url,data)
# 随便访问一个网址 open里面是可以用Request构建请求体的
res = opener.open(req)
# 保存cookie
cookie.save(ignore_discard=True, ignore_expires=True)

print res
