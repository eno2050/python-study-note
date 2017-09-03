#-*- coding:utf-8 -*-

class Person(object):
	#私有属性
	__count = 0
	#初始化方法
	def __init__(self,name,age):
		#实例属性
		self.name = name
		self.age = age
		
	#实例方法 可以获取任何属性
	def sayHello(self):
		print self.name
		
	#类方法 类方法只能获取类属性
	@classmethod
	def sayMy(cls):
		print cls.__count
		
 
#新建一个学生类  继承会继承父类所有的 方法 和 属性
class Student(Person):
	
	def __init__(self,name,age,grade):
		#先初从父类继承的属性 super(Student,slef) 这个会返回父类 也就是继承的Person
		#下面这个相当于调用父类的__init__方法,self已经隐式传递，所以不用写
		super(Student,self).__init__(name,age)
		#在初始化自己独有的属性
		self.grade = grade

student = Student('jack',12,'小学')
student.sayMy()	

L = dir(student)

L = filter(lambda x:not x[:1]=='_',L)
print L	


