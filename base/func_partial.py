# _*_ coding:utf-8 _*_

# partial 偏函数 这事functools 下面的一个方法  可以重新一定一个函数的默认参数
#functools.partial可以把一个参数多的函数变成一个参数少的新函数，
#少的参数需要在创建时指定默认值，这样，新函数调用的难度就降低了

import functools


#task
#我们在sorted这个高阶函数中传入自定义排序函数就可以实现忽略大小写排序。
#请用functools.partial把这个复杂调用变成一个简单的函数：

#装饰器可以给函数加功能 decorator
#偏函数可以修改已知函数的默认参数，让调用简单 partial

#functools 函数工具 

#目前知道2中用法 
#1.复制原函数的属性 @functools.wraps(fn) 
#2.生成偏函数 functools.partial(fn,key=)

sorted2 = functools.partial(sorted,key = lambda x:x.upper())





		
		
	
	
	











