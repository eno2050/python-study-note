#-*- coding:utf-8 -*-
#闭包
def count():
	fs = []
	for i in range(1,4):
		a = i
		def f(x):
			return x*x
		fs.append(f(a))
	return fs

print count()