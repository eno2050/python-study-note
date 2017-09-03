# _*_ coding:utf-8 _*_

#enumerate 枚举 很重要

Lindex = range(1,4)
Lname  = ['php','apache','html5']

Lnew = zip(Lindex,Lname)

for index,name in Lnew:
	print index,'==>',name
	
for index,name in enumerate(Lname):
	print index+1,'==>',name
	
#intervalues

# dict 迭代key and values

D = {
	'php':100,
	'python':99,
	'html5':98,
	'css3':97	
}

for key,value in D.items():
	print key,'===>',value
	
#第二种方法,没有特殊需求建议采用第二种方法
for key,value in D.iteritems():
	print key,'===>',value













