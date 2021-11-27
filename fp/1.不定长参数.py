def mySum(*t):
	print(t, type(t))
	result = 0
	# t是一个元组，对其操作的方式就是对元组的操作方式
	for v in t:
		print(v)
		result += v
	print(result)


mySum(4,5,6,7)

def mySum2(**kwargs):
	print(kwargs, type(kwargs))
	result = 0
	# kwargs是一个字典，对其操作方式就是对字典的操作方式
	for k, v in kwargs.items():
		print(v)


mySum2(name='sz', age=12)

'''
不定长参数*t形式，则传入的参数值即可，这些参数值会以元组形式传入函数，元组的每一个值就是传入的参数
不定长参数**kwargs形式，传入的参数是 参数名=参数值 的形式，这些参数会以字典的形式传入函数，参数名是字典的键，参数值是字典的值
'''