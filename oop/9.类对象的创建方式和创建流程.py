def run(self):
	print(self)


# 变量xxx指向类对象，类对象的名称是Dog
xxx = type("Dog",(),{'name':0, 'run':run})
print(xxx)
print(xxx.__dict__)

# 不可以访问类对象的名称，只可以访问变量的名称	
d = xxx()
print(d)
d.run()



# --------------------类的创建流程--------------------
'''
方式1
class Person(mateclass=xxx):
'''
class Person:
	# 通过__metaclass__指明元类
	__metaclass__ = 'int'
	pass
