# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author:eno2050
# email:117908549@qq.com
# 2017-10-2

import re
str = "1apple2orange3banner4watermelon"
# 利用正则将匹配出符合正则表达式的子字符串，返回一个list
# title 可以将字符串的首字母大写
result = re.findall(r'\D+',str)
print result[0].title()
