# 第一种使用方式，调用property函数

class Person(object):
	def __init__(self):
		self.__age = 18

	def get_x(self):
		return self.__age

	def set_x(self, value):
		self.__age = value

    # 这里的age经过property就变成一个属性
    # property装饰过的属性，既可以读，也可以写，具体可以看property的源码
	age = property(get_x, set_x)


p = Person()
print(p.age)

p.age = 90
print(p.age)

print(p.__dict__)



# 第二种使用方式，使用@property的装饰器

class Person(object):
	def __init__(self):
		self.__age = 18

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, value):
		self.__age = value

p = Person()
print(p.age)

# 如果只有@property，则这样设置会报错，还需要加一个装饰器@age.setter才可以设置
# 也就是说可以分开绑定读取值与修改值
p.age = 10

print(p.age)