# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author:eno2050
# email:117908549@qq.com
# 2017-10-2

import re
str = 'hello world! I am coming!'
# re.search 和 match 方法和属性相同;但是match只有在0位置匹配成功才有返回,search会在全局去匹配
result = re.match(r'(\w+) (\w+)(?P<other>.*)',str)
# 属性
print result.string
print result.re
print result.pos
print result.endpos
print result.lastindex
print result.lastgroup
# 方法
print result.group()
print result.groups()
print result.groupdict()
print result.start(2)
print result.end(2)
print result.span()
print result.expand(r'\3 \2 \1')
