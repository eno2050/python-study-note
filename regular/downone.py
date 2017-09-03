# _*_ coding:utf-8 _*_

import re
import urllib2

url = 'http://img.yeitu.com/2017/0822/20170822094358917.jpg'

f = open('./img/1.jpg','wb')
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"}
req = urllib2.Request(url,headers=headers)
res = urllib2.urlopen(req)
buf = res.read()
f.write(buf)
f.close()
