
# 装饰器的关键
# 1.原始函数体不改变；2.调用代码不发生改变
# 3.实现额外的功能

def check(func):
	def inner():
		print('登录验证')
		func()
	return inner

@check
def fashuoshuo():
	print('发说说')


# fashuoshuo函数体没有改变；调用fashuoshuo函数代码没有改变；实现了登录验证的功能
fashuoshuo()




# 使用类实现装饰器
class Check:
	# 注意两个要点 1.在初始化方法保存传递过来的方法本身
	def __init__(self, func):
		self.f = func

	# 2.在call方法中执行之前保存的函数，并且添加额外的功能
	# 因为call方法可以让实例像函数一样执行
	def __call__(self):
		print('登录验证')
		self.f()

@Check
def fashuoshuo():
	print('发说说')

# 或者使用下面形式
# fashuoshuo = Check(fashuoshuo)

# 实现的目标
# fashuoshuo函数体没有改变；调用fashuoshuo函数代码没有改变；实现了登录验证的功能
fashuoshuo()