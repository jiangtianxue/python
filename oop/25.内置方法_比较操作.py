
class Person:

	def __init__(self, age, height):
		self.age = age
		self.height = height

	# 比较运算符 ==， ！= ，>, >=, <, <=
	# 这里的参数other也是一个实例对象，和self是一样的
	def __eq__(self, other):
		return self.age == other.age
	# 不等于
	def __ne__(self, other):
		print('xxx')
    # 大于
	# def __gt__(self, other):
		pass
	# 大于等于
	# def __ge__(self, other):
	# 	pass
	# 小于
	def __lt__(self, other):
		print('lt')
		print('xxxxxxxxxxx')
		print('实际上是大于的')
		return self.height < other.height
	# 小于等于
	def __le__(self, other):
		print('这是小于等于')
	pass

p1 = Person(18, 180)
p2 = Person(18, 190)

# 其触发方式就是使用比较的运算符，例如下面的==符号
# 需要注意的是p1,p2都是实例对象，实例对象直接比较的时候，就会调动这些特殊方法
print (p1 == p2)

# ！=符号触发的是__ne__内置函数，但是如果只有__eq__,没有__ne__，也是可以的
# 也就是对于反向操作，如果只定义了其相反的方法，也可以调用该想法的方法运行
# 其他的运算符使用和触发方式是一样的
print (p1!=p2)
# __lt__既可以推出小于，也可以推出大于，但不支持叠加，意思是如果分别有大于
# 和等于的方法，则不支持大于等于的操作
# print (p1>p2)

print(p1>=p2)


'''
import functools

# 通过装饰器就可以把小于等于分解为小于和等于，既可以计算小于，也可以计算等于，还可以计算小于等于
@functools.total_ordering
class A:
	def __init__(self, age, height):
		self.age = age
		self.height = height

	def __lt__(self, other):
		print('lt')

	def __eq__(self, other):
		print('eq')

a1 = A(18,180)
a2 = A(19,180)
print(a1 <= a2)
'''


class Person:
	def __bool__(self):
		return False

p = Person()

if p:
	print('xx')
else:
	print('yy')