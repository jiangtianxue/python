
# 打印不同长度分割线


# 线的配置函数
def line_config(content, length):

	def line():
		print('-'*(length // 2) + content + '-'*(length // 2))

	return line

# 这里的line1和下面的line2变量名都指向了一个函数
# 因为line_config()返回的是一个函数，所以可以
# 把line1和line2当成函数来使用，下面的line1()的调用就是函数的调用
line1 = line_config('闭包', 20)

# 打印相同内容时候可以直接使用函数，不用重复调用line_config函数
line1()
line1()
line1()
line1()

# 打印不同内容可以重新调用即可
line2 = line_config('刘润', 40)
line2()