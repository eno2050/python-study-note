# _*_ coding:utf-8 _*_

#reduce()函数也是Python内置的一个高阶函数。
#reduce()函数接收的参数和 map()类似，一个函数 f，一个list，第三个参数是可选 代表默认值
#reduce()传入的函数 f 必须接收两个参数，
#reduce()对list的每个元素反复调用函数f，并返回最终结果值。

# 例子中是求和的运算

def f(x,y):
	return x+y

L = [1,2,3]
print reduce(f,L,100)

#作业
#Python内置了求和函数sum()，但没有求积的函数，请利用recude()来求积：

L2 = [2, 4, 5, 7, 12]

def prod(x,y):
	return x*y
	
print reduce(prod,L2,1)


#总结一下 map 和 reduce 如果需求是对L每一个元素，用map 两两计算用 reduce












