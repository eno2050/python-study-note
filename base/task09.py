#-*- coding:utf-8 -*-
#请编写一个@performance，它可以打印出函数调用的时间。
import time
def performance(f):
	def fn(*args,**kw):
		#打印log 或者 时间
		print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		return f(*args,**kw)
	return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)