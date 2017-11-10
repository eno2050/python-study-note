# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author:eno2050
# email:117908549@qq.com
# 2017-10-2

import urllib2
import urllib
import re
import cookielib

page = 2
url = "https://www.qiushibaike.com/hot/page/"+str(page)
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'
}
cookie = cookielib.CookieJar()
hander = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(hander)


try:
    req = urllib2.Request(url,headers=headers)
    res = opener.open(req)
    result =  res.read()
    #print result;
    #exit
    result = result.decode("utf-8")
    pattern = re.compile(ur'<div.*?author clearfix">.*?src="(.*?)".*?<h2>(.*?)</h2>.*?content">.*?<span>(.*?)</span>.*?thumb.*?src="(.*?)".*?likenum.*?img.*?>(.*?)</div>',re.S)
    list_joke = re.findall(pattern,result)
    for item in list_joke:
        print item[0],item[1],item[2],item[3],item[4]
except urllib2.URLError as e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reason'):
        print e.reason
