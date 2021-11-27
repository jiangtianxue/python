def test():
	funcs = []
	for i in range(1,4):
		def test2():
			print(i)
		funcs.append(test2)
	return funcs

new = test()

new[0]()
new[1]()
new[2]()


print('--------------分割线---------------')

def test():
	funcs = []
	for i in range(1,4):
		def test2(num):
			def inner():
				print(num)
			return inner
		# 有了()之后就会执行test2，就会进入到test2的作用域
		# append的是test2的执行，所以就会使用这个时候的i
		# 关键是有没有括号代表执行还是不执行的问题
		# 这里的列表和之前不一样的是存的是函数的执行，而不是函数本身
		# 并且append的是返回函数inner
		funcs.append(test2(i))

	return funcs

funcs = test()

# 返回的是一个列表，列表里面是函数
print(funcs)

# 只有函数被调用，才会确定变量标识对应的值，所以如果没有inner函数则打印的全是3
# 也就是在这里的时候才会确认i的数值
funcs[0]()
funcs[1]()
funcs[2]()



def test():
	num = 10
	def test2():
		nonlocal num
		num = 666
		print(num)
	print(num)
	# 如果内层函数可以修改外层函数的变量，经过test2()之后num应该是666
	# 但是此处num任然等于10，说明内层函数无法修改外层函数的变量
	# 只要使用nonlocal关键词之后，才可以进行修改
	test2()
	print(num)

	return test2

result = test()