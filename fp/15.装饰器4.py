# 装饰器有参数

def getzsq(char):
	# 定义一个装饰器并且return一个装饰器
	# def zsq到return inner是一般装饰器的格式，
	# 而getzsq这个函数是为了根据char参数生成特定的装饰器
	# char参数也在装饰器内部使用到了
	def zsq(func):
		def inner():
			print(char * 30)
			func()
		return inner
	return zsq
# 不能在上面的getzsq函数列表中直接加入char的原因是
# 如果这样做zsq函数就有两个参数，必须要先传lr函数
# 但此时的lr函数还在下面，看不到，所以是不行的
@getzsq('-')
def lr():
	print('lr')

lr()

@getzsq('#')
def lr():
	print('lr')

lr()