# _*_ coding:utf-8 _*_

#列表生成式

L = [x*x for x in range(1,10)]
print L


# 从一开始，美隔2个取一个
r = range(1,10,2)

#请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]

L2 = [x*(x+1) for x in range(1,100,2)]

print L2


# 复杂表达式 

print ''.join([str(x) for x in L2])


#条件过滤
def toUpperWord(L):
	return [x.upper() for x in L if isinstance(x,str)]
	
print toUpperWord(['Hello', 'world', 101])

#多层表达式
#利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。

L2 = [str(a)+str(b)+str(c) for a in range(1,10) for b in range(0,10) for c in range(1,10) if a==c]

print L2
# 这个很吊 也实现了上面的功能
L3 = [100*m+10*n+m for m in range(1,10) for n in range (0,10)]












