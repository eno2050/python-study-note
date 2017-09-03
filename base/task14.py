#-*- coding:utf-8 -*-
#请给 Person 类增加一个私有属性 __score，表示分数，再增加一个实例方法 get_grade()，能根据 __score 的值分别返回 A-优秀, B-及格, C-不及格三档。

	
class Person(object):
	__score = 0
	def __init__(self,score):
		self.__score = score
	
	def get_grade(self):
		if(self.__score >= 90):
			print 'A-优秀'
		elif(self.__score >= 60):
			print 'B-及格'
		else:
			print 'C-不及格三档。'
			
p1 = Person(80)

p1.get_grade()
