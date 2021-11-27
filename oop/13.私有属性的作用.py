class Person:
	__weight = 100
	# 在__init__内部定义的是实例属性，因为第一个参数是self
	# __init__作用是，当创建一个实例对象的时候，会自动调用这个方法，执行这个函数内的语句，初始化这个实例
	# 如果有两个下划线就是私有属性，实例的私有属性只可以在类的内部定义
	def __init__(self):
		self.__age = 18

	# 而私有属性只可以在类的内部访问，如果要修改，可以通过一个方法来进行修改
	# 此处的age是可以是数字，不可以是字符串或者其他，通过私有属性的不可直接修改性
	# 通过setAge函数进行修改，可以在setAge函数里面进行一下数据的拦截和过滤
	# 例如下面的代码就是对输入的age的数据类型和大小进行了一个判断
	def setAge(self, value):
		if isinstance(value, int) and  0<value<200:

			self.__age = value
		else:
			print("您输入的数据有问题。")

	def getAge(self):
		return self.__weight

p1 = Person()
print(Person.__dict__)
Person.__weight = 19
p2 = Person()

print(p1.getAge())
print(p2.getAge())
print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)
