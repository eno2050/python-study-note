#-*- coding:utf-8 -*-
__author__ = 'luotianshuai'
'''
alex 超级用户
wusir 管理用户
laoyao 普通用户
'''

name = input('Please input you name:')

if name == 'alex':
    print('超级用户')
elif name == 'wusir':
    print('管理用户')
elif name == 'laoyao':
    print('普通用户')
else:
    print('无效用户')