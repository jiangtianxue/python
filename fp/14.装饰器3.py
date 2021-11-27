# 装饰器叠加

def add_line(func):
	def inner():
		print('-' * 30)
		func()
	return inner


def add_star(func):
	def inner():
		print('*' * 30)
		func()
	return inner

@add_line  # 等同于 lr = add_line(lr)
           # 则lr()就是执行print('-'*30) print('*'*30) print('lr')
@add_star  # 等同于 lr = add_star(lr)
           # 则lr()就是执行print('*'*30) print('lr')
def lr():
	print('lr')

lr()