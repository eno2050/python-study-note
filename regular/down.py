# _*_ coding:utf-8 _*_

import re
import urllib2

req = urllib2.urlopen('http://www.yeitu.com/')
buf = req.read()
list = re.findall(r'data-echo=\"(.*(jpg|png))',buf)

#print list[0][0]


#下载图片
picname = 0
for url in list:
    imgFlie = open('./img/'+'pic'+str(picname)+'.'+url[1],'wb')
    #获取图片
    req = urllib2.urlopen(url[0])
    buf = req.read()
    imgFlie.write(buf)
    imgFlie.close()
    picname = picname + 1
