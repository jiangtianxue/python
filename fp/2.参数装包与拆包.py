
# 装包
def test1(*args):

	print(args, '传入的是整体')
	# 拆包
	print(*args, '拆包之后是一个个元素')
test1(1,2,3,4)


print('--------------分割线---------------')


def sum(a,b,c,d):
	print(a+b+c+d)

def test(*args):
	print(args)
	# 拆包，把元组元素1,2,3,4一个个传入到函数中去
	# 分别对应a,b,c,d则程序不会报错
	sum(*args)
# 装包
test(1,2,3,4)



def sum1(a, b):
	print(a+b)

def test1(**kwargs):
	print(kwargs)

	# 拆包
	# 因为sum1函数有两个参数，所以需要拆包
	sum1(**kwargs)
# 装包
test1(a=1,b=2)