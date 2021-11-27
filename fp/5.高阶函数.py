
def test(a, b):
	print(a+b)

# test只是一个函数名，也就是是一个变量，有id，也可以将函数
# 传递给另一个变量，说明函数本身也可以作为数据，传给另外一个变量
print(id(test))
test2 = test
test2(1,2)











# 高阶函数，一个函数A的参数是另一个函数的时候，则将函数A称之为高阶函数
# sorted函数就是一个高阶函数，它的一个参数key可以接受另一个函数作为参数
# getKey()函数返回的是一个字典的age对应的值，而sorted函数则凭借这个值进行排序


l = [{"name":'lr', 'age':18},
	 {'name':'lr2', 'age':19},
	 {"name":'lr3', 'age':17}]

def getKey(x):
	return x['age']

def getName(x):
	return x['name']


result1 = sorted(l, key=getKey)
result2 = sorted(l, key=getName)
print(result1)
print(result2)


# 使用场景，动态改变计算方式

def caculate(num1,num2,caculateFunc):
	print(caculateFunc(num1, num2))


def jiafa(a,b):
	return a + b

def jianfa(a,b):
	return a-b

caculate(6,2,jiafa)
caculate(6,2,jianfa)