# _*_ coding:utf-8 _*_

# sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，
#比较函数的定义是，传入两个待比较的元素 x, y，
#如果 x 应该排在 y 的前面，返回 -1，
#如果 x 应该排在 y 的后面，返回 1。
#如果 x 和 y 相等，返回 0。

L1 = [36, 5, 12, 9, 21]

L2 = sorted(L1)
print L2

def reversed_cmp(x,y):
	if x > y:
		return -1
	elif x < y:
		return 1
	else:
		return 0

L3 = sorted(L1,reversed_cmp)
print L3

#作业
#对字符串排序时，有时候忽略大小写排序更符合习惯。请利用sorted()高阶函数，实现忽略大小
#写排序的算法。
L4 = ['bob', 'about', 'Zoo', 'Credit']
#['about', 'bob', 'Credit', 'Zoo']

# 怎么实现
def cmp_ignore_case(t):
    return t.lower()

print sorted(['bob', 'about', 'Zoo', 'Credit'], key=cmp_ignore_case)


def cmp_ignore_case2(s1,s2):
	s1 = s1.upper()
	s2 = s2.upper()
	if s1 > s2:
		return 1
	if s1 < s2:
		return -1
	return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ignore_case2)


print 'Abbbb'<'Baaaaa'


# 这里是我想多了 字符串也能比较大小  而且比较函数里面的参数你即使加工了 但却不影响原来
#list里面的值

L5 = [x for x in L4 for y in L4 if x.upper()<y.upper]
print L5
