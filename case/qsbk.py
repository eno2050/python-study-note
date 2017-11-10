# _*_ coding:utf-8 _*_
# /usr/bin/env python
# author:eno2050
# email:117908549@qq.com
# 2017-10-2
# 爬取糗事百科笑话页面

import urllib
import urllib2
import re
import cookielib
import os
from bs4 import BeautifulSoup
from math import ceil

class qsbk:
    #初始化
    def __init__(self):
        self.pageno = 1
        self.url = 'https://www.qiushibaike.com/hot/page/'
        self.headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36',
        'Upgrade-Insecure-Requests':'1'
        }
        self.cookie = cookielib.CookieJar()
        self.hander = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.hander)
        # 存放每一页的笑话
        self.jokes = []
        self.pages = self.get_pages()
        self.create_cache_file()

    def get_page_code(self,pageno):
        self.pageno = pageno
        self.req = urllib2.Request(self.url+str(self.pageno),headers=self.headers)
        try:
            res = self.opener.open(self.req)
            result = res.read()
            return result
        except urllib2.URLError as e:
            if hasattr(e,'reason'):
                print u'错误原因是',e.reason
                return None
    # 获取pageno的最大值
    def get_pages(self):
        pattern = re.compile(r'<li>.*?<span.*?>(.*?)</span>.*?</li>',re.S)
        pages = re.findall(pattern,self.get_page_code(1))
        for index,value in enumerate(pages):
            pages[index] = value.strip()
        return int(pages[len(pages)-3])
    # 获取笑话列表
    def create_cache_file(self):
        for item in range(1,self.pages+1):
            result = self.get_page_code(item)

            # 新建一个文件
            if os.path.exists('cache/'+str(item)+'.html'):
                break
            print '采集到第'+str(item)+'页'
            fp = open('cache/'+str(item)+'.html','w')
            fp.write(result)
            fp.close()

    def get_list(self):
        for item in range(1,self.pages+1):
            soup = BeautifulSoup(open('cache/'+str(item)+'.html'),'html.parser')
            print '完成了'+str(ceil(float(item)/(self.pages+1)*100))+'%'
            #print soup.prettify().encode("utf-8", 'ignore');
            for item2 in soup.findAll('div',class_="article"):
                d = {
                    'author':item2.h2.string.strip(),
                    'headimg':item2.img['src'],
                    'body':item2.select('.content span')[0].string,
                    'bodyimg':''
                }
                if len(item2.select('.thumb img')) == 0:
                    d['bodyimg'] = 'none'
                else:
                    d['bodyimg'] = item2.select('.thumb img')[0]['src']
                self.jokes.append(d)
        return self.jokes

qsbk = qsbk()
print len(qsbk.get_list())
