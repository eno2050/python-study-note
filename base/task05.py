#-*- coding:utf-8 -*-

#请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

import math

def is_sqr(x):
	#可以将取的平方根先搞成整数，在判断是否相等
    #return int(math.sqrt(x)) == math.sqrt(x)
	#和1取模 是否等于0
	return math.sqrt(x)%1 == 0

print filter(is_sqr, range(1, 101))