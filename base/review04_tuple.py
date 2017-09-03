# _*_ coding:utf-8 _*_
 
#tuple 翻译中文是元组的意思 特点：1：有序 2：创建完毕后不可修改（除非里面的元素是list） 3.用圆括号表示
# 可以定义一些不变的变量 比如星期 和 月份 这些都是固定不变的
# 

t = ('monday','tuesday','wedday')

print t

# 读取的话就利用索引 

print t[-1]

# 不可修改 所以 没有append insert pop 等方法 当然也不能利用索引进行赋值

print (range(1,10))


#创建tuple的时候要注意 单元素的 tuple

print (1)
# 这样子就会输出1 而不是 (1)  因为在这里 括号作为运算符，提高了里面的运算等级 所以就输出了1，因此在创建单元素的tupled
#的时候 就要这样子创建 (1,)

print (1,)









