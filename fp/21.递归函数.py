

def jiecheng(n):
	if n == 1:
		return 1

	return n * jiecheng(n-1)


result = jiecheng(104)
print(result)