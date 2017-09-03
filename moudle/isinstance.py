#-*- coding:utf-8 -*-

L = [1,2,3]

t = ('monday','tuesday','wedday')

t2 = isinstance(t,tuple)

print t2

# 多态 子类和父类 可以自己定义函数，即使函数名字是一样的，在调用的时候总是优先从自身找这个方法，
# 若果没有找到，才回去父类中去查找
