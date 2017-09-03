#-*- coding:utf-8 -*-
#匿名函数 lambda
print filter(lambda s: s and len(s.strip())>0, ['test', None, '', 'str', '  ', 'END'])