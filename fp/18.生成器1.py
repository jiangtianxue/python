# 这是一个列表表达式
l = [i for i in range(100) if i % 2 ==0]
print(l)

# 1. 可以使用列表表达式生成

print('------------------分割线-----------------')
l = (i for i in range(10) if i % 2 ==0)
print(l)
print('打印出来的generator就代表这是一个生成器')


# # 也可以使用for in循环
# for i in l:
# 	print(i)


# 具备状态记录特性
print(next(l))
print(next(l))
print(next(l))
print(next(l))
# 下面的方式和上面的等效
print(l.__next__())

print('------------------分割线-----------------')
print('------------------分割线-----------------')
print('------------------分割线-----------------')


# 2. 使用生成器函数生成，函数中包含yield语句，这个函数的执行结果就是‘生成器’
# yield可以阻断当前的函数执行，相当于暂停，并且会把当前的状态值返回给外界
# 当使用next()函数或者__next__(),都会让函数继续
# 执行，当执行到下一个yield语句的时候，又会被暂停
# 所以在第一次yield之前会打印出xxx
def test():
	print('xxx')

	yield 1
	print('a')

	yield 2
	print('b')

	yield 3
	print('c')

	yield 4
	print('d')

	yield 5
	print('e')

# 调用这个函数不会执行里面任何的语句，只会产生生成器
g = test()

# 执行的结果就是一个生成器
print(g)

# 执行next函数的时候就是在状态的跳转，第一个状态是，即next(g)=1，所以prin(next(g))
# 会打印出1，同理下一个状态是2，应该打出2，但是1和2之间还有print('a')语句，所以会打印出
print(next(g))
print(next(g))
