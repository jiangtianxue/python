class Person:
	def eat(self, food):
		print('在吃饭, ', self, food)

	def eat2(xxx):
		print('这是一个实例方法')
		print(xxx)

p = Person()
print(p)
# 自动把实例p作为第一个参数传入 
# 这是一种标准调用方式
p.eat('饭')


p.eat2()

# 直接调用函数本身，方法在类中，直接找到这个函数本身，进行调用
# 这种调用方式，必须要传入一个实例对象才对
Person.eat(123, '饭')