# 被装饰函数有参数

def zsq(func):
	# 注意这里的inner是有参数的，接受被装饰的函数的参数
	# 并且因为装饰器可以装饰多个函数，接受参数不一样，所以需要有不定长参数
	def inner(num, *args, **kwargs):
		print('*'*30)
		func(num)
	return inner


@zsq
def pnum(num):
	print(num)

pnum(123)