# _*_ coding:utf-8 _*_

# lambda 匿名函数 希腊字符 第十一个
# 关键字lambda代表匿名函数  匿名函数有个限制，就是只能有一个表达是 不写return 返回值就是改表达式的结果


# 跳到装饰器了不好意思 还是把例子写一下吧 演过2遍了，还是没记住

def fn(x):
	return x*x

def new_fn(fn):
	def fn2(x):#新函数要传递老函数的参数
		#定义装饰器函数要运行的动作
		print 'call '+fn.__name__+'() 函数'
		#调用fn函数
		return fn(x)
	return fn2 #把fn2返回回去
	
#装饰器函数的调用 
#第一种方法 重新定义一个变量接受新函数
g = new_fn(fn)
print g(5)
#第二种方法 fn重新定义
fn = new_fn(fn)
print fn(5)
#第三种方法
@new_fn
def fn2(x):
	return x*x*x

print fn2(5)

#打印日志 @log
#检测性能 @performance
#数据库事物 @transaction
#url路由 @post('/register')

#查看全局变量

#print (vars())




		
		
	
	
	











