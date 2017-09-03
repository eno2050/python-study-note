# _*_ coding:utf-8 _*_
 
# dict 相当于js的对象 用大括号{}表示 键值对  字典序
d= {
	'lisa':98,
	'apache':86,
	'php':80,
	'html':70
}

L = ['php','apache','html','css3']


# set方法是一种特殊的方法 里面会传一个list 作为他的值 ，下面我们来测试一个

s = set(L)
print s
# 返回 set(['apache', 'css3', 'php', 'html'])

# set 有这个几个特点 1：无序 2.元素不重复(万一定义有重复的元素，会被自动剔除掉)3.不存放可变对象

# set 访问
# 注意：由于set是无序集合，所以不能通过索引才来访问 我们一般就是来判断一个元素是否存在.比如

print 'apache' in s
# 返回 True
# 虽然set 不能使用索引访问，但是和list 一样 ，依然是可以使用for来循环遍历的
for name in s:
	print name
	
# set 元素的 改 1.add 2.remove

s.add('python')
print s

#添加元素就是add的方法，如果要添加的元素存在，也不会报错，只不过元素不会添加进去

#remove 就不那么的友好了，如果删除的元素不存在，就会报错，所以在删之前，最好判断一下

if 'python' in s:
	s.remove('python')
	print s

#如果直接删不存在的元素.会报错
#s.remove('mayun') #KeyError: 'mayun'












