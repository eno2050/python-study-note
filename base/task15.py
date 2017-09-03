#-*- coding:utf-8 -*-
#如果将类属性 count 改为私有属性__count，则外部无法读取__score，但可以通过一个类方法获取，请编写类方法获得__count值。


class Person(object):
	__count = 0
	
	@classmethod
	def getCount(cls):
		return cls.__count
	
	def __init__(self):
		Person.__count += 1

p1 = Person()

print Person.getCount()

print p1.getCount()