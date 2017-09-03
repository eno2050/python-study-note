#-*- coding:utf-8 -*-
# 异常控制
import os
print os.getcwd()
try:
	fp = open('test.txt','w')
	fp.write("hello world")
except:
	print "文件不存在"
else:
	print "写入成功"
	fp.close()
	

