#-*- coding:utf-8 -*-
# 特殊方法 魔术方法
# __str__ 和 __repr__
# __str__ 这个是显示给用户的 __repr__ 这个是显示给开发人员的

# 下面举一个例子 来重写这2个函数

class student(object):
    """docstring for student."""
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return __name__+' %s,%s ' % (self.name,self.age)

    __repr__ = __str__

s = student('lilei',26,'小学')

#var = dir(s)

#print var
print s
