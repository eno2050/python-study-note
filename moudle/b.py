#-*- coding:utf-8 -*-
# 看完了函数 现在我们来攻破模块这个堡垒吧

#import a
#from a import showName
from a import showName as show
def showAge(age):
	print 'my age is '+ age
	
show('lilei')
showAge('26')


import os
print os.path.isdir(r'C:\Windows')
print os.path.isfile(r'C:\Windows\notepad.exe')