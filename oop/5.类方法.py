class Person:
	@classmethod
	def leifangfa(cls, a):
		print('这是一个类方法', cls, a)


# 1.直接使用类调用
Person.leifangfa(123)

# 2.使用实例调用，实例对应的类传入类方法，而不是实例
p = Person()
p.leifangfa(666)

# 3.间接使用
func = Person.leifangfa
func(111)

# 4. 子类调用类方法时传递的是子类，不是父类
class A(Person):
	pass
A.leifangfa(0)