# 被装饰函数有返回值

def zsq(func):
	def inner(*args, **kwargs):
		print('*'*30)
		res=func(*args, **kwargs)
		return res
	return inner

@zsq
def pnum(num1, num2, num3):
	return(num3+num2+num1)


res = pnum(1,2,3)
print(res)