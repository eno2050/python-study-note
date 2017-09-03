# _*_ coding:utf-8 _*_

# map 是 Python 内置的高阶函数，
#1.接收一个函数 f 和一个 list，
#2.通过把函数 f 依次作用在 list 的每个元素上，
#3.得到一个新的 list 并返回。

def f(x):
	return x*x
	

L = [1,2,3]

L2 = map(f,L)

print L2

# 作业
#假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，
#请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：

L3 = ['lilei','pHp','APache','HTML5']

def format_name(x):
	return x[:1].upper()+x[1:].lower()
	
L4 = map(format_name,L3)
print L4

# 这个对字符串来说有一个capitalize ,可以格式化字符串 capitalize() == x[:1].upper()+x[1:].lower()











