# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author:eno2050
# email:117908549@qq.com
# 2017-10-2
import re
pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
# 正则的方法完成替换
print re.sub(pattern,r'\2 \1', s)
# 函数的方法完成替换
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print re.sub(pattern,func, s)

### output ###
# say i, world hello!
# I Say, Hello World!
