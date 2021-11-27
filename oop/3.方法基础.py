
# 方法分为实例方法，类方法，静态方法
class Person:
	def eat(self):
		print('这是一个实例方法', self)

	@classmethod
	def leifangfa(cls):
		print('这是一个类方法', cls)

	@staticmethod
	def jingtaifangfa():
		print('这是一个静态方法')

p = Person()
print(p)
p.eat()

print('**'*60)
Person.leifangfa()
Person.jingtaifangfa()

print('**'*60)
print(Person.__dict__)