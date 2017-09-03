#-*- coding:utf-8 -*-
# 请把上节的 Person 类属性 count 改为 __count，再试试能否从实例和类访问该属性。

class Person(object):
	__count = 0
	def __init__(self):
		Person.__count +=1

p1 = Person()

#print p1.__count  访问不了
#print Person.__count  #访问不了

# 尝试访问的话就可以用下try

try:
	print p1.__count 
except:
	try:
		print Person.__count
	except:
		print "访问不了"
	

