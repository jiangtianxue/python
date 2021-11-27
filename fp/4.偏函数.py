
# 直接方式，使用缺省函数
def test(a, b, c, d=1):
	print(a+b+c+d)
test(1,2,3)

# 偏函数, 大部分使用场景下d=2
def test2(a,b,c,d=2):
	test(a, b, c, d)
test2(1,2,3)

def test3(a,b,c=1,d=2):
	test(a,b, c, d)
test3(1,2)



print('-----------分割线-----------')

import functools
# 这样的写法相当于在上面的test3中的写法，把c变成5
# 只是这样的写法较为简单
newFunc = functools.partial(test, c=5)

# 使用functools模块也可以构造偏函数
# 由于d在test中已经有了缺省值，c在偏函数构造时候有了偏爱值，所以只需要传入两个参数

newFunc(1,2)