# -*- coding:utf-8 -*-

import random,string
# 文件名起名的时候一定注意不要起系统已知模块的名字

field = string.letters + string.digits

#随机取出n个字符出来
def getString(n):
    return "".join(random.sample(field,n))

#生成一条验证码 格式比如XXXX-XXXX-XXXX-XXXX
def getOneCode(a=4,b=6):
    return '-'.join([getString(b) for i in range(a)])

# print getOneCode(4,6) lxWIOQ-mV1uAh-TIOezx-cXe8Fb
# print getOneCode() n5Rord-OEtWep-1ymtJa-iuMBzh

# 批量生成验证码
def getMoreCode(n):
    return ','.join([getOneCode() for i in range(n)])

print getMoreCode(10)
