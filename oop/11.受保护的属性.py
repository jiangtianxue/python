class Animal:
	_x = 10
	def test(self):
		print(Animal._x)
		print(self._x)


class Dog(Animal):
	def test2(self):
		print(Dog._x)
		print(self._x)


# 测试 类的内部可以访问到受保护的属性_x
a = Animal()
a.test()


print('**'*30)
# 测试 子类内部可以访问到受保护的属性_x
d = Dog()
d.test2()


print('**'*30)
# 测试 模块内部的其他位置可以通过类或者实例访问到受保护的类属性_x，但是会出现警告，不建议这种访问 
# 并且，跨模块也可以通过类或者实例访问受保护的类属性_x，但是会出现警告，不建议这种访问
print(Animal._x)
print(Dog._x)
print(a._x)
print(d._x)