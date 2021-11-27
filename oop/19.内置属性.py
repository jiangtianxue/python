class Person:
	'''
	这是一个人
	'''
	age = 19

	def __init__(self):
		self.name = 'lr'

	def run(self):
		print('run')

# __dict__ 类的属性
print(Person.__dict__)

# __bases__ 类的父类构成原则
print(Person.__bases__)

# __doc__ 类的文档字符串
print(Person.__doc__)

# __name__ 类名
print(Person.__name__)

# __module__ 类定义所在的模块
print(Person.__module__)

# __dict__ 实例的属性

# __class__ 实例对应的类
p=Person()
print(p.__class__)