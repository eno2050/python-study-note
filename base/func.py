# _*_ coding:utf-8 _*_

# 函数式编程 特点：1.把计算视为函数而非指令 2.纯函数编程：不需要变量,没有副作用，测试简单 3.支持高阶函数

#能接收函数作为参数的函数就是高阶函数。

def sumAbs(x,y,fn):
	return fn(x)+fn(y)
	

print sumAbs(-1,-2,abs)












