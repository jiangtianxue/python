
class Person:
	# def __new__(cls, *args, **kwargs):
	# 	print('新建一个对象，但是被我拦截了')


	def __init__(self):
		print('初始化方法')
		self.name = 'lr'

	def __del__(self):
		print('这个对象被释放了')

p = Person()
print(p)
print(p.name)