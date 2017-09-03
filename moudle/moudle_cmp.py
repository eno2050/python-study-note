#-*- coding:utf-8 -*-
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if False == isinstance(s, Student):
            return -1
        return -cmp(self.score, s.score) or cmp(self.name, s.name)

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99),'haha']
print sorted(L)

#有时候看似理解了 实际上并没有理解 就像下面的2个函数
# cmp(x,y) 函数用于比较2个对象，
#如果 x < y  返回 -1,
#如果 x == y 返回 0,
#如果 x > y  返回 1。

# sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，
#比较函数的定义是，传入两个待比较的元素 x, y，
#如果 x 应该排在 y 的前面，返回 -1， 也就是false 如果是从大到小排列 若果x>y 那么应该返
#回not x-y 如果从小到大排列，那就刚刚好

#如果 x 应该排在 y 的后面，返回 1。
#如果 x 和 y 相等，返回 0。
#分析函数第一次运行 cmp(99,88) 返回 1 前面有一个取反 所以结果是 -1 这个值是存在的
#所以就不往后走了，直接输出 -1 , 也就是说 99应该在88的前面
#第二次 Student('Bob', 88), Student('Alice', 99) 第一次计算后 是1 值也是存在的，
#所以 
