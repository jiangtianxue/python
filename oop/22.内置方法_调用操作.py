
# 使得对象可以被调用，类似于函数，通过一个类实例化一个对象
# 通过调用这个对象，就会自动找__call__特殊方法，如果类中有这个方法
# 就会执行这个方法，如果类中没有这个方法，就会报错，并且同方法一样，
# 可以在调用的时候传递参数，其使用场景类似于偏函数，偏爱于某几个参数
class Person:
	def __call__(self, *args, **kwargs):
		print('xxx', args, kwargs)
	pass

p = Person()
# 函数的调用形式是 函数名()
# p是一个实例，但是却可以像一个函数一样被调用
p(123, 456, name='se')




class PenFactory:
	def __init__(self, p_type):
		self.p_type = p_type

	def __call__(self, p_color):
		print('创建一个%s这个类型的画笔，他是%s颜色' % (self.p_type, p_color))

# 主要是简便了代码
ganbi = PenFactory('钢笔')
ganbi('红色')
ganbi('绿色')
ganbi('蓝色')


qianbi = PenFactory('铅笔')
qianbi('红色')
qianbi('绿色')
qianbi('蓝色')
