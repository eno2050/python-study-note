# _*_ coding:utf-8 _*_

# list 切片是一个很重要的操作  切片其实就是在给定的list里面获取所需的元素

L = [1,2,3,4,5,6,7,8,9,0]

print L[:] #相当于复制一个新的list
print L[0:3] # 1,2,3
print L[1:3] # 2,3
print L[::2] # 1,3,5,7,9
print L[::1] # 1,2,3,4,5,6,7,8,9,0

print L[2::2] #3,5,7,9

print L[2:7:2] # 3,5,7

#range()函数可以创建一个数列
#1. 前10个数；
#2. 3的倍数；
#3. 不大于50的5的倍数。

L2 = range(1,101)

print L2[:10]
print L2[2::3]
print L2[4:50:5]

# 获取最后10个5的倍数 这个比较经典 有些时候一步到位的事情分两步反而比较简单

print L2[4::5][-10:]

# 同理 对字符串也可以应用切片操作

str = 'php,apache,python,html'

# 定义一个函数 实现首字母大写

def upperFirstWord(str):
	return  str[:1].upper()+str[1:]

print upperFirstWord('haha')

#扩展一下 这个函数可传递一个参数，将前n个字母大写

def upperMultipleWord(str,n=1):
	return  str[:n].upper()+str[n:]
	
print upperMultipleWord('haha')
print upperMultipleWord('haha',2)

#enumerate 可以循环出索引 enumetate

for index,i in enumerate(L):
	print index,':',i













