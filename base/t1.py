#-*- coding:utf-8 -*-
#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。程序源代码：
	
## 利用set里面的元素不重复实现上面需要的功能

list_num  = ['1','2','3','4']
list_result = []

for i in list_num:
	for j in list_num:
		for k in list_num:
			if(len(set(i+j+k))==3):
				#list_result.append(int(i+j+k))
				list_result += [int(i+j+k)]

##print list_result

#print ['1','2','3']+['3'] 这个可以有

#print set('x','y','z')+set('xx')	set一旦建立就固定了 所以不带修改的 除非里面的元素的list

from itertools import permutations

for i in permutations([1, 2, 3, 4], 3):
	# 把每一个元素转化成字符串 用字符串的方法的时候 list 里面的元素必须是字符串
	L = map(lambda x:str(x),list(i))
	print "".join(L)

	
