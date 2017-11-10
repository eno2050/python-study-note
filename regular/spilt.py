# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author:eno2050
# email:117908549@qq.com
# 2017-10-2

import re
str = "1apple2orange3banner4watermelon"
# 基本用法就是用正则去分割字符串，返回一个list
result = re.split(r'a',str)
print result
