class Person:
	# 当我们通过 "实例.属性 = 值"，给一个实例增加一个属性，或者说，修改一下属性值的时候
	# 都会调用这个方法。在这个方法内部，才会真正把这个属性以及对应的数据给存储到
	# __dict__字典里面，所以通过这个方法可以让只读属性无法修改
	def __setattr__ (self, key, value):
		print(key, value)

		# 1. 判定，key是否是我们要设置的只读属性的名称,如果key已经在__dict__字典里面
		#    则p1.age是修改操作，我们要拦截修改操作，允许只读操作和添加操作
		# 2. 如果不是只读属性的名称，则可以添加到这个实例里面去
		if key == "age" and key in self.__dict__.keys():
			print('这是只读属性，不能设置数据')
		else:
			self.__dict__[key] = value


p1 = Person()
p1.age = 18

print(p1.age)
print(30*'---')
p1.age = 999
print(p1.age)
print(p1.__dict__)