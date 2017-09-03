# _*_ coding:utf-8 _*_

#filter()函数是 Python 内置的另一个有用的高阶函数，
#filter()函数接收一个函数 f 和一个list，
#这个函数 f 的作用是对每个元素进行判断，返回 True或 False，
#filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。

# 挑选可用元素 

# 保留偶数
L = [1, 4, 6, 7, 9, 12, 17]

def f(x):
	return x % 2 == 0
	
L2 = filter(f,L)
print L2

# 保留基数

def is_odd(x):
	return x % 2 == 1
	
print is_odd(3)
print is_odd(4)

# 删除None 或者 空字符串

def is_empty_str(x):
	return x and len(x.strip())>0

L3 = ['test', None, '', 'str', '  ', 'END']

print filter(is_empty_str,L3)


# 作业
# 请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：
import math

L4 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def intSqur(x):
	return math.sqrt(x)%1 == 0

L5 = filter(intSqur,L4)
print L5
	
	
	











