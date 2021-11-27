class Person:
	'''
	这是一个关于类的描述
	'''
	age = 0
	def shilifangfa(self):
		print(self)
		print(self.age)
		print(self.num)

	@classmethod
	def leifangfa(cls):
		print(cls)
		print(cls.age)

	@staticmethod
	def jingtaifangfa():
		print(Person.age)

p = Person()
p.num = 10

# 类属性访问：1.类访问；2.实例访问
print(Person.age)
print(p.age)

print('**'*30)
# 实例属性访问：只能通过实例访问
print(p.num)


print('**'*30)
# 实例方法传入的是实例，可以访问实例属性和类属性
p.shilifangfa()


print('**'*30)
# 类方法传入的是实例，只可以访问类属性，不可以访问实例属性
p.leifangfa()

print('**'*30)
# 静态方法没有传入实例和类，不可以直接访问，如果想访问，需要在静态方法中有一个类或者实例
Person.jingtaifangfa()