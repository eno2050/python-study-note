# _*_ coding:utf-8 _*_

import os

try:
    open('./img')
except:
    os.mkdir('./img')
    print "ok"
