#-*- coding:utf-8 -*-
# 定义一个无理数的加减乘除
class Rational(object):
    """docstring for Rational."""
#定义一个无理数，里面有分子和分母
    def __init__(self, son,mother):
        self.son = son
        self.mother = mother
        self.__getSimperRational()
# 分数的加法运算
    def __add__(self,next):
        if self.mother == next.mother:
            return Rational(self.son+next.son,self.mother)
        return Rational(self.son*next.mother+self.mother*next.son,self.mother
    *next.mother)
#定义一个输出的无理数的方法
    def __str__(self):
        if self.son % self.mother == 0:
            #能除尽，直接显示
            return str(self.son/self.mother)
            #用分数表示
        return '%s/%s' % (self.son,self.mother)
#减法
    def __sub__(self,next):

        #2个分数一样的情况
        if self.son*next.mother-self.mother*next.son == 0 :
            return 0
        #分母一样的情况
        if self.mother == next.mother:
            return Rational(self.son-next.son,self.mother)
        return Rational(self.son*next.mother-self.mother*next.son,self.mother
    *next.mother)

#定义一个函数，化简分数
    def __getSimperRational(self):
        if self.son > self.mother:
            minnum = self.mother
        else:
            minnum = self.son

        for i in range(minnum,1,-1):
            if self.son % i == 0 and self.mother % i ==0:
                self.son = self.son/i
                self.mother = self.mother/i
                break
#定义一个乘法
    def __mul__(self,next):
        return Rational(self.son*next.son,self.mother*next.mother)
#第一个除法
    def __div__(self,next):
        return Rational(self.son*next.mother,self.mother*next.son)
#可以讲结果转换成浮点数
    def __float__(self):
        return self.son*1.0/self.mother
#转换成整数
    def __int__(self):
        return self.son // self.mother



r1 = Rational(9,2)
r2 = Rational(2,2)
r3 = Rational(10,3)
print int(r3)
print float(r3)
print r3
print r1 + r2
print r1 - r2
print r1*r2
print r1/r2
