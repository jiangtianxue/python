
# b = 10
# print(id(b))


# def change(num):
# 	print(id(num))
# 	num = num + 1
# 	print(id(num))

# 	num = num + 1
# 	print(id(num))
# 	print(num)

# change(b)

# print(b)

b = [1,2,3]
print(id(b))

# 通过观察变量的id来验证是值传递还是地址传递
# 如果变量的id没有变化，则表明是地址传递
def change(num):
	print(id(num))
	num.append(4)
	print(id(num))
	print(num)

	num.append(5)
	print(id(num))
	print(num)

change(b)

print(b)


print('-------------分割线----------')

def change2(num):
	print('num 在函数中的地址：', id(num))

	num = 5+num
	print('在没有修改之后，地址相同，说明是地址传递')
	print('不可变num改变之后的地址：',id(num))
	print('改变后的num的数值:', num)

c = 4
print('原始的c的地址：', id(c))
change2(c) 
