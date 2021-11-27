def caculate(num1, num2, caculateFunc):
	print(caculateFunc(num1, num2))



def sum1(a, b):
	return a+b


def subtract(a, b):
	return a-b

caculate(6,2,sum1)
caculate(6,2,subtract)
