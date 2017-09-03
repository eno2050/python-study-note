# _*_ coding:utf-8 _*_

# 文件就是一个对象，linux任何元素都是文件
# _*_ coding:utf-8 _*_

# 文件就是一个对象，linux任何元素都是文件

#sys.stdin 文件的标准输入
#sys.stdout 文件的标准输出
#sys.stderr 文件的标准错误
#talk is cheaper show me the code

#httpbin.org/ip
import urllib2
import urllib
from json import loads

#获取妹子总数的页码
def getPages():
    html = urllib2.urlopen('https://mm.taobao.com/tstar/search/tstar_model.do?'+
    '_input_charset=utf-8').read().decode('gbk').encode('utf-8')
    pages = loads(html)['data']['totalPage']
    return int(pages)

#print getPages() 1450

#获取所有妹子主页的url
def getGilsList():
    L = []
    for i in range(1,2):
        values = {
            'currentPage':i,
        }
        data = urllib.urlencode(values)
        req = urllib2.Request('https://mm.taobao.com/tstar/search/tstar_model.do?'+
        '_input_charset=utf-8',data = data)
        res = urllib2.urlopen(req)
        datas = res.read().decode('gbk').encode('utf-8')
        list = loads(datas)['data']['searchDOList']
        L = L+list
    return L

#print getGilsList()[0]['city']
num = getGilsList()
#获取单个妹子的id
for item in num:
    print item['userId']
