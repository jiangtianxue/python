


# 创建一个实例，计数加1；删除一个实例，计数减1

class Person:
	# 这是一个类属性
	__count = 0

	def __init__(self):
		# 类属性访问的时候要加上类
		Person.__count += 1
		print('计数加1')

	def __del__(self):
		self.__class__.__count -= 1
		print('计数减1')

	@classmethod
	def log(cls):
		# 同样的这里需要进行类属性访问，需要传入的是一个类，所以使用到类方法的装饰器
		print('当前实例的个数是', cls.__count)

p1 = Person()
p2 = Person()

del p1
del p2
Person.log()