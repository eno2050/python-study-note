# -*- coding: utf-8 -*-
#计算L的里面元素的平方和
def square_of_sum(L):
    num = 0
    for i in L:
        num += i*i
    return num

#print square_of_sum([1,2])

#求一元二次方程的2个解 ax² + bx + c = 0
import math
def quadratic_equation(a, b, c):
    de = b*b-4*a*c
    if de>=0:
        x1 = (-b+math.sqrt(de))/(2*a)
        x2 = (-b-math.sqrt(de))/(2*a)
	return x1,x2
    else:
		return None

#print quadratic_equation(4, 1, 3)

#计算n的阶乘,还是注意缩进啊
def fact(n):
	if(n<=0):
		print '数字不正确'
		return
	if(n==1):
		return 1
	return n*fact(n-1)

#print fact(0)

#汉诺塔 (http://baike.baidu.com/view/191666.htm) 的移动也可以看做是递归函数。

#-*- coding:utf-8 -*-
# move(n, a, b, c)表示的是有n个盘子在a柱子上，将要移到b柱子上面去
def move(n, a, b, c):
# 这个函数应该这么解释：看参数
# n 代表A柱子上所有的盘子
# a 代表a柱子
# b 代表过渡的柱子
# c 代表目的地
# 如果a柱子上面只有一个盘子，则直接移到c柱子上面去并输出路径，结束递归
    if n == 1:  
        print a, '-->', c
        return
# 表示的是将n-1的盘子从a柱子上面移到b柱子上面去	
    move(n-1, a, c, b)
# 输出
    print a, '-->', c
# 将b柱子上面的n-1个盘子移动到c柱子上面
    move(n-1, b, a, c)

#move(3, 'A', 'B', 'C')
	
#print moveHlt(2,"A","B","C")
def greet(a=0):
	if(a):
		print '''Hello,''',a,'.'
	else:
		print '''Hello, world.'''

def greet1(a='world'):
	print 'Hello,',a,'.'
#greet1()

#计算平均数
def average(*args):
	#args 是一个tuple
	if(len(args)==0):
		return 0.0
	else:
		return sum(args)/(len(args)+0.0)

#print average()
L = range(1, 101)
# 当有2个冒号的时候 第一个数字代表第几个 第二个代表索引 第三个代表步长
#print L[:11]
#print L[2::3]
#print L[4:50:5]

L = range(1, 101)
#print L[-10:]#最后10个数；
#print L[-46::5]#最后10个5的倍数。这是一个笨办法,思路而且不清晰	
#大神的做法，分成2个步骤，先找到所有的5个倍数，再取最后10个
#print L[4::5][-10:]

#字符串首字母大写
def firstCharUpper(s,n=1):
	#获取第一个字符
	fc = s[:n].upper()
	#
	fl = s[n:]
	return str(fc)+str(fl)
#print firstCharUpper('hello')

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

aum = 0.0
for value in d.itervalues():
    aum+=value
#print aum/len(d)
#print 1.0*sum(d.itervalues())/len(d)

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for k, v in d.iteritems():
    sum = sum + v
    #print k,':',v
#print 'average', ':', sum/len(d.items())

#print range(1,100,2)

#print [x*(x+1) for x in range(1,100,2)]

d = { 'Adam': 95, 'Lisa': 55, 'Bart': 59 }
def generate_tr(name, score):
	if(score<60):
		return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
	return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name, score) for name, score in d.iteritems()]
#print '<table border="1">'
#print '<tr><th>Name</th><th>Score</th><tr>'
#print '\n'.join(tds)
#print '</table>'


def toUppers(L):
    return [x[:1].upper()+x[1:] for x in L if isinstance(x, str)]

#print toUppers(['ello', 'world', 101])

print [str(x) + str(y) + str(z) for x in range(1,10) for y in range(1,10) for z in range(1,10) if x == z]


