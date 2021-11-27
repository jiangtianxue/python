class Person:
	def __init__(self):
		# 因为下面对于列表的操作是元素替换，所以这里的列表不能为空
		self.items = [1,2,3,4,5,6,7,8,9]

	# 新增
	def __setitem__(self, key, value):
		# 手动增加,这里的可以直接传递，也可以进行分解
		# 为了确保传入的是列表，还可以进行一下判断
		if isinstance(key, slice):
			# self.items[key.start, key.stop, key.step] = value
			self.items[key] = value

p = Person()
# 触发方式和列表类似
# 这是一个赋值操作，意思是列表的第0和第三个元素变成'a'和'b'
p[0:4:2] = ['a','b']
print(p.items)