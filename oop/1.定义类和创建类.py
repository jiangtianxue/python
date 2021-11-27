#定义一个类
class Money:
	pass


# 根据这个类，实例化一个对象
one = Money()
print(Money.__name__)
print(id(Money))
print(one.__class__)


print('**'*30)

# 对象添加属性
class Person:
	pass

p = Person()
p.age = 15
p.hight = 150
print(p.age)
# 当前对象的所有属性
print(Person.__dict__)
print(p.__dict__)

print('**'*30)

# 访问对象属性
p.age = 123
print(p.age)


print('**'*30)
# 属性是可变对象
p.pets = ['小花', '小黑']
print(p.pets)
print(id(p.pets))
p.pets.append('小黄')
print(p.pets)
print(id(p.pets))



print('**'*30)
# 删除属性
print(p.__dict__)
del p.hight
print(p.__dict__)