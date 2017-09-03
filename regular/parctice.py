# _*_ coding:utf-8 _*_
a = '_hello'
# 这个例子我看了老半天 原来是啊a【0】大于等于或者小于等于
#变量的第一 a首先要存在 第一个字母下滑杠 和 或者是字母
#print a and (a[0]=='_' or 'a' <= a[0] <= 'z')
#正则表达式 re 模块
import re
str = 'imooc python'
# find 查找字符串
#print str.find('11')
#使用正则
pa = re.compile('imooc')
#print dir(pa)
#'findall', 'finditer', 'flags', 'groupindex', 'groups', 'match', 'pattern',
# 'scanner', 'search', 'split', 'sub', 'subn
#print dir(re)
#'compile', 'copy_reg', 'error', 'escape', 'findall', 'finditer', 'match', 'purge',
# 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'sys', 'template
#print help(re.match)

result = re.match(pa,'imooc python')
print dir(result)

print result.re()
