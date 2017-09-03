#-*- coding:utf-8 -*-
# 面向对象编程
class Person(object):
	def __init__(self,name,skin = "yellow"):
		self.name = name
		self.__dict__.skin = skin

		
xiaoming = Person('xiaoming')
hahha = Person('hahha')

print xiaoming.name
print xiaoming.skin
print hahha.name