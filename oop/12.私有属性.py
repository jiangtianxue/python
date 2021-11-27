class Animal:
	__x = 10
	def test(self):
		print(Animal.__x)
		print(self.__x)


class Dog(Animal):
	def test2(self):
		print(Dog._Animal__x)
		print(self._Animal__x)


# 测试 类的内部可以访问到私有属性__x
a = Animal()
a.test()


# print('**'*30)
# # 测试 子类内部不可以访问到私有属性__x
# d = Dog()
# d.test2()


# print('**'*30)
# 测试 模块内部的其他位置不可以通过类或者实例访问到私有类属性__x
# 并且，跨模块也不可以通过类或者实例访问私有类属性__x
# print(Animal.__x)
# print(Dog.__x)
# print(a.__x)
# print(d.__x)



# ---------------------------------------------------分割线--------------------------------
# 按照名字重整机制访问私有属性,通过__dict__方法可以查看Animal类的所有属性
# 发现有一个_Animal__x属性和私有属性值一致，所以可以通过_Animal__x访问私有属性
# 就可以在模块其他位置调用私有属性
print(Animal.__dict__)
print(Animal._Animal__x)
print(a._Animal__x)

# 同样的，子类也可以采用同样方法调用私有属性
d = Dog()
d.test2()
# 但是既然已经定义为私有属性，就是说不希望在外界调用，所以最好不要使用这种方法