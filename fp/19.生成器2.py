def test():
	print('xxx')
	# 在执行这一步的时候，赋值语句先执行右边，当碰到yield的时候就会暂停挂起
	res1 = yield 1
	print(res1)

	res2 = yield 2
	print(res2)

	res1 = yield 3
	print(res3)


# g就是一个生成器
g = test()

# 只有在调用这个生成器的时候才会进入函数体内部执行
# 调用的方式有三种，例如 生成器.__next__()
print(g.__next__())

# 此处会打印出None，因为yield语句暂停的作用，使得res1无法赋值，也就是什么都没有，就是None
print(g.__next__())
# send和next一样，可以重启程序的执行，跳转到下一个状态，但是多了一个功能，可以给上一次被
# 挂起的yield语句的返回值传值，上一次挂起的是res1=yield 1，也就是给res1传值sss，所以可以打印出sss
# 但是因为是为上一次挂起返回值传值，所以在整个函数执行的开始传值，因为没有上一次挂起
print(g.send('sss'))


# 如果要在第一次启动函数的时候就用send，可以传None
# print(g.send(None))
