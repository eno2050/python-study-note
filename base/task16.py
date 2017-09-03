#-*- coding:utf-8 -*-
#请参考 Student 类，编写一个 Teacher类，也继承自 Person

class Person(object):
	
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex
		

class Student(Person):
	def __init__(self,name,age,sex,grade):
		super(Student,self).__init__(name,age,sex)
		self.grade = grade

		
s1 = Student('xm','16','boy','高二')

print s1.grade