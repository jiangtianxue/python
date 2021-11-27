'''
# 方式1，使用property
class Person:

	def __init__(self):
		self.__age = 18

	@ property
	def age(self):
		return self.__age

	@ age.setter
	def age(self, value):
		if value < 0:
			value = 0
		self.__age = value

	@ age.deleter
	def age(self):
		del self.__age

p = Person()
# 此时就可以直接使用 对象.属性 的方法去访问这个属性
# 查属性值
print(p.age)

print('------------------分割线----------------')

# 同时在外界使用 对象.属性 = value 的方法直接赋值
# 该改属性值
p.age = 20
print(p.age)

print('------------------分割线----------------')

# 删除属性
# 由于删除了属性，再打印肯定会出错
del p.age
print(p.age)'''


# 方式2，将相关操作也封装成一个类

class Age:
	def __get__(self, instance, owner):

		print('get')
		return instance.v

	# p.age传入的15这个数值，可以成为self(Age)的属性，也可以成为instance(Person)
	# 的属性，但是描述器是被实例共享的，所以这个数据只能存在实例对象上，而不是描述器对象
	def __set__(self, instance, value):
		instance.v = value
		print('set', self, instance, value)

	def __delete__(self, instance):
		print('delete')
		del instance.v

class Person:
	age = Age()

p = Person()
p.age = 15

p1 = Person()
p1.age = 18
