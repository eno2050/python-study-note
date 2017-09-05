# _*_ coding:utf-8 _*_

#转换cmd 的编码格式 chcp 65001 就是换成UTF-8代码页 chcp 950 返回简体u中文

import re
import urllib2
from BeautifulSoup import BeautifulSoup

html = urllib2.urlopen('http://www.cfwk120.com/index.html').read()
html=unicode(html,'gb2312','ignore').encode('utf-8','ignore')
#print html
soup  = BeautifulSoup(html)
result = soup.find('div',{'class':'mysubnav blue text-center'})
result = str(result)
print result
#print type(result)
big = re.findall(r'alt=\"(.*)\"\s+\/>',result)
#print big
small = re.findall(r'<a.*?>(.*?)</a>',result)
#print len(small)
#循环输出
for names in big:
    print names

list = ''
for names in range(len(small)):
    list = list + small[names] + ','

print list
