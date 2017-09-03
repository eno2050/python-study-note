# _*_ coding:utf-8 _*_

def make_list():
    L =[]
    for i in range(10):
        def inner(arg,a=i):
            return a + arg
        L.append(inner)
    return L

result = make_list()
#print result
print(result[3](10))