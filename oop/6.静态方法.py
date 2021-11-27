class Person:
	@staticmethod
	def jingtai():
		print('this is a static method')


# 1.使用类调用
Person.jingtai()


# 2.使用实例调用
p = Person()
p.jingtai()