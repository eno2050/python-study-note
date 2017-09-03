# _*_ coding:utf-8 _*_

#开胃菜 sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。

def getSum(L):
	sum = 0
	for num in L:
		sum += num

	return sum


print getSum([1,2,3,4,5])












