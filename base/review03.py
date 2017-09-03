# _*_ coding:utf-8 _*_

# list ：python 内置的一种列表数据类型 特点：1.有序 2.可以随意删除和修改 3. 中括号表示（和js的数组类似）

La = ['Micheal','Bob','Tracy']

Lb = ['Adam', 95.5, 'Lisa', 85, 'Bart', 59]
print Lb

#list 元素的访问，利用索引 从0开始
print Lb[0]

#当然也可以倒序访问 默认最后一个元素的索引是-1, 利用len方法可以获取对象的长度 所以第一个元素就应该是 -len(L)
print Lb[-len(Lb)]

#添加新的元素 list
#
#第一种办法：append()，把要追加的元素放到list的末尾
#

Lb.append('Lisa')
print Lb
print Lb[-1]
 
#第二种办法：利用insert 方法  这个方法有2个参数：1.索引 2.值  注意：这个只将替换索引出的值 而且将替换的值后移

Lb.insert(-1,'Lilei')

print Lb

Lb.insert(1,'Huge')

print Lb

#删除元素 用pop 方法 特点：里面可以加参数 参数代表索引 返回值是删除的这个元素

print Lb.pop()
print Lb

print Lb.pop(-1)
print Lb

#元素替换 这个就很简单了 直接利用索引获取元素后 赋值即可

Lb[-1] = 'NewLilei'
print Lb



