def test():
	print('xxx')
	# 在执行这一步的时候，赋值语句先执行右边，当碰到yield的时候就会暂停挂起
	yield 1
	print('a')

	yield 2
	print('b')

	yield 3
	print('c')

g = test()

print(g.__next__())
print(g.__next__())

g.close()
print(g.__next__())
# print(g.__next__())
