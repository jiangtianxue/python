def getFunc(flag):
	#再次定义几个函数
	def sum1(a, b, c):
		return  a+b+c

	def subtract(a, b, c):
		return a-b-c

	# 根据不同的flag返回不同的操作函数
	if flag == '+':
		# 返回函数变量名而不是调用函数，所以不用()
		return sum1 

	elif flag == '-':
		return subtract


# 此时的result已经是一个函数了
result = getFunc('+')
print(result, type(result))

res =  result(1,3,5)
print(res)

result = getFunc('-')
print(result, type(result))

res =  result(1,3,5)
print(res)