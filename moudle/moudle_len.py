#-*- coding:utf-8 -*-
# 任务
# 斐波那契数列是由 0, 1, 1, 2, 3, 5, 8...构成。
# 请编写一个Fib类，Fib(10)表示数列的前10个元素，print Fib(10) 可以打印出数列的前 10
# 个元素，len(Fib(10))可以正确返回数列的个数10。

class Fib(object):
    def __init__(self,num):
        self.num = num
        self.count = 2
        self.L = [0,1]
        while self.count < self.num:
            self.L.append(self.L[self.count-1]+self.L[self.count-2])
            self.count = self.count + 1

    def __str__(self):
        return str(self.L)

    def __len__(self):
        return len(self.L)

f = Fib(20)

print f
print len(f)
print f.count

#没想到和我写的竟然一样 感动啊
