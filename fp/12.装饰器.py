# 定义两个功能函数

def fss():
	print('发说说')


def ftp():
	print('发图片')



# 逻辑代码，逻辑代码和功能函数分开
btnIndex = 2
if btnIndex ==1:
	fss()
else:
	ftp()

# 添加功能
# 发说说，发图片有个前提，就是用户必须登录，所以需要验证登录

# 1.直接在逻辑代码中修改，添加一个验证操作，缺点是可能要多次修改逻辑代码，很麻烦，代码冗余度大，复用性小，维护成本大
btnIndex = 2
if btnIndex ==1:
	print('登录验证...')
	fss()
else:
	print('登录验证...')
	ftp()


print('------------------分割线----------------------')
print('------------------分割线----------------------')
print('------------------分割线----------------------')

# 2.直接在功能函数中修改，方便代码的重用
# 把内部的闭包返回给了外界，这样fss和ftp才是函数
# 在后面的逻辑代码中才可以被调用，所以这里必须是闭包
def checklogin(func):
	def inner():
		print('登录验证...')
		# 传入的是一个函数
		# 有括号的是执行
		# 所以会打印 '登录验证...' 和执行 func()
		func()
	return inner


def fss():
	print('发说说')

def ftp():
	print('发图片')

# 下面一句等价于
# fss = def inner:
#			 print('登录验证...')
# 			 fss()
# 因为需要在后续代码中执行，所以必须将fss和ftp变成函数
# 这个时候就可以用到之前使用到的闭包的概念，接受一个函数
# 还可以返回一个函数
fss = checklogin(fss)

ftp = checklogin(ftp)

# 逻辑代码
btnIndex = 2
if btnIndex ==1:
	fss()
else:
	ftp()


print('------------------分割线------------------------')
print('------------------分割线------------------------')
print('------------------分割线------------------------')


# 3.语法糖写法,就是装饰器，使用checklogin函数装饰了fss函数
# @checklogin就等同于fss = checklogin(fss)，注意这里左边的fss是函数
# 因为checklogin里面的是闭包，返回的是一个函数
@checklogin
def fss():
	print('发说说')

# @checklogin就等同于ftp = checklogin(ftp)
@checklogin
def ftp():
	print('发图片')

btnIndex = 1
if btnIndex ==1:
	fss()
else:
	ftp()
