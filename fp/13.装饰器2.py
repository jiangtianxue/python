

# 给函数增加一些额外功能并且同时
# 1.函数名称不可以改变
# 2.函数体内部代码不能改变
# 这就是装饰器的作用，也是要求
'''

def fss():
	print('发说说')
fss = check(fss)

以上三行程序等价于

@check
def fss():
	print('发说说')

需要执行函数的时候都是
fss()

以上是本质，理解这个是很重要的
'''

def check(func):
	def inner():
		print('登录验证...')
		func()
	return inner	

def fss():
	print('发说说') 

# 第一种方式，传入函数
# fss = check(fss)
# fss()

# 第二种方式，装饰器，其本质还是闭包的概念
# 只不过这种方式是特定的一种书写方式，对于闭包的简化
# 就是装饰器
@check
def fss():
	print('发说说')


@check
def ftp():
	print('发图片')

# 执行
fss()

print('*'*60)

# 执行
ftp()

