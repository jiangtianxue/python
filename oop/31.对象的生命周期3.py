


import sys
class Person:
	pass


p1 = Person()

p2 = p1
print(sys.getrefcount(p1))
p3 = p1
print(sys.getrefcount(p1))
del p2
print(sys.getrefcount(p1))



import objgraph
# objpraph.count()可以查看垃圾回收期，跟踪的对象个数,简单理解就是类创建的实例个数

class Person:
	pass

class Dog:
	pass

p = Person()
d = Dog()

print(object.count("Person"))
print(object.count("Dog"))

p.pet = d
d.master = p

# 删除p，d之后，对应的对象是否被释放掉
del p
del d

print('------------分割线--------------')
print(object.count("Person"))
print(object.count("Dog"))
