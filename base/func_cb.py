# _*_ coding:utf-8 _*_

# 函数的返回值可以是一个函数

def myabs(x):
	return abs(x)

# 直接调用myabs 返回是abs的函数

print myabs(-1)

#任务
#请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。

def calc_prod(lst):
	def calc(x,y):
		return x*y	
	def delay_calc_prod():
		return reduce(calc,lst)		
	return delay_calc_prod

f = calc_prod([1, 2, 3, 4])

print f()

#注意返回值是函数 还是 函数运行后计算的结构 里面的函数该干嘛就干嘛 关键是最后的返回值 要注意



		
		
	
	
	











