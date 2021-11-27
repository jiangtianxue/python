class Animal:
	x = 10
	def test(self):
		print(Animal.x)
		print(self.x)


class Dog(Animal):
	def test2(self):
		# 验证类
		print(Dog.x)
		# 验证实例
		print(self.x)


# 测试 类的内部可以访问到公有属性x
a = Animal()
a.test()


print('**'*30)
# 测试 子类内部可以访问到公有属性x
d = Dog()
d.test2()


print('**'*30)
# 测试 模块内部的其他位置可以通过类或者实例访问到公有类属性x
# 并且，跨模块也可以通过类或者实例访问公有类属性x
print(Animal.x)
print(Dog.x)
print(a.x)
print(d.x)