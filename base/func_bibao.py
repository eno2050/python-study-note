# _*_ coding:utf-8 _*_

# 闭包 内层函数引用的外层函数的变量，然后返回内层函数的情况 这个叫做闭包

#example

def a(s):
	def g():
		return s
	return g

fa = a('haha')

#print fa()


def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            return lambda : i*i
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()






# list 这个用法很奇特 第一次见 

L4 = [1,2,3,4]

a1,a2,a3,a4 = L4

print a1,a2,a3,a4


		
		
	
	
	











