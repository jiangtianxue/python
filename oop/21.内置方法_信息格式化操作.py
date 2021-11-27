

# 信息格式化操作 包括__str__和__repr__

# class Person:
# 	# 创建不同的实例
# 	def __init__(self, name, a):
# 		self.name = name
# 		self.age = a

# 	# def __str__(self):
# 	# 	return self.name

# 	def __repr__(self):
# 		return 'reprxxxx'

# p1 = Person('lr', 18)
# print(p1.name, p1.age)
# print(p1)

# s = str(p1)
# print(s)

# p2 = Person('se', 20)
# print(p2.name, p2.age)
# print(p2)

# print(repr(p1))


import datetime
t = datetime.datetime.now()
print(t)
print(repr(t))