class Person:
	def __init__(self):
		self.__age = 18

	# 方式1
	def getAge(self):
		return self.__age

	# 方式1优化
	# property装饰器主要作用就是，可以以使用属性的方式，来使用这个方法
	@property
	def xxx(self):
		return self.__age


# 方式1
# 设置成私有化属性，则既不可以写，又不可以读
# 设置指定的方法getAge在类的内部读出私有化属性，实现可读不可写
p1 = Person()
print(p1.getAge())


# 方式1优化，使用property装饰器
# 可以在外界读出属性值，在修改属性值的时候报错
# 并且这种装饰器方法，可以简便书写，不用在后面加小括号，
# 也就是说用使用属性的方式来使用这个方法，这个方法当成属性来使用，下面的xxx没有小括号
# 同时，此种方法下，直接设置p1.xxx是会出错的，而不是添加一个新的属性，同时为了方便，这里的xxx可以变成age
print(p1.xxx)

p1.xxx = 666
