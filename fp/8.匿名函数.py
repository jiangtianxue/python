result = (lambda x, y : x + y)(1,2)
print(result)

newFunc = lambda x, y : x + y
print(newFunc(5, 5))

# lambda函数的具体应用例子
# 简化程序
l = [{'name':'lr1', 'age':16}, {'name':'lr2', 'age':14}, {'name':'lr3', 'age':19}]

# 这里的key就是一个函数
result = sorted(l, key=lambda x: x['age'])
print(result)