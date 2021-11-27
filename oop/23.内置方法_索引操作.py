class Person:
	def __init__(self):
		self.cache = {}

	# 新增
	def __setitem__(self, key, value):
		# 手动增加
		self.cache[key] = value
		print("setitem", key, value)

	# 查找
	def __getitem__(self, item):
		# 手动获取
		print('getitem', item)
		return self.cache[item]
	# 删除
	def __delitem__(self, key):
		# 手动删除
		print('delitem', key)
		del self.cache[key]

p = Person()
# 触发方式和字典很像，使用方括号键值对赋值，使用方括号键值对查找，
# 同样的使用方括号进行键值对删除
# __setitem__触发方式
p['name'] = "se"

# __getitem__触发方式
print(p['name'])

# __delitem__触发方式
del p['name']
print(p.cache)