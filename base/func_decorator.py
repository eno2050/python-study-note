# _*_ coding:utf-8 _*_

# 装饰器 decorator

# 设计不定参的decorator *args **kw

#请编写一个@performance，它可以打印出函数调用的时间。 
import time
import functools
def performance(fn):
	#@functools.wraps(fn)
	def inner_fn(*args,**kw):
		#输出一个时间
		print time.asctime( time.localtime(time.time()) )
		return fn(*args,**kw)
	
	return inner_fn #返回内部函数
	
@performance
def fn(x,y,z):
	return x*y*z
	
print fn(5,6,7)
print fn.__name__





		
		
	
	
	











