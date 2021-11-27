class Person:

	def __init__(self):
		self.result = 1

	def __iter__(self):
		# 加了下面这一句，就可以实现迭代器重用
		# for in的访问首先会到iter函数中，返回到实例本身
		# 再到next函数中访问数据，则在第二次for in的时候重置了self.result变量
		# 这样就不会引起next函数中异常，可以重用
		self.result = 1
		return self

	def __next__(self):
		self.result += 1
		if self.result >= 8:
			raise StopIteration('停止遍历')
		return self.result


p = Person()

import collections
print(isinstance(p, collections.Iterator))

for i in p:
	print(i)

print('--------------分割线-------------')

for i in p:
	print(i)


