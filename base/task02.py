#-*- coding:utf-8 -*-
# python 进阶 list 元素字符串格式化 将首字母大写
def format_name(s):
	return s[:1].upper()+s[1:].lower()

print map(format_name, ['adam', 'LISA', 'barT'])