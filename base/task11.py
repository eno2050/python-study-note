#-*- coding:utf-8 -*-
# 类属性

class Person(object):
	count = 0
	def __init__(self):
		Person.count += 1

		
p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
p5 = Person()
p6 = Person()
print p2.count