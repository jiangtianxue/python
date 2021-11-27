class Money:
	pass

one = Money()


print('**'*60)

# 类增加属性, 类名.属性 = 属性值
Money.count = 1
print(Money.count)
print(Money.__dict__)



print('**'*60)
# 类添加属性方式2，类中直接写上某个属性

class Money:
	age = 18
	count = 1
	num = 666
print(Money.age)
print(Money.count)
print(Money.num)
print(Money.__dict__)



print('**'*60)
# 类查询属性，通过类访问和通过对象访问

one = Money()
print(one.age)
print(one.count)
print(one.num)



print('**'*60)
# 如果更改__class__,则改变类，说明对象所属的类是可以动态改变的
class Test:
	sex = 'male'

# one对象指向了Test类,此时one已经变成了Test类
one.__class__ = Test
print(one.sex)


print('**'*60)
# 如果对象有需要属性，就会使用自己的对象的属性
one.sex = 'female'
print(one.sex)



print('**'*60)
# 修改类属性,直接使用类名进行修改,无法使用类实例化的对象进行修改
class Money:
	age = 18
	count = 1
	num = 666
Money.age = 20
print(Money.age)



print('**'*60)
class Person:
	age = 10
	pass
p = Person()
# 给p对象新增一个属性,如果通过实例对象对类属性进行修改，实质上是实例对象增加了一个属性，类对象本身的属性没有被修改
# 这里有两步，第一步右边的p.age = 10,是查找；第二步是p.age = 10+5 是p实例对象新增属性age，值是15
# 可以明显看出类对象和实例对象的两个age属性的id都是不一样的
p.age += 5
print(id(Person.age))
print(id(p.age))
print(Person.age)
print(p.age)
print(Person.__dict__)
print(p.__dict__)


print('**'*60)
# 通过__slots__属性来限制对象可以添加的属性是什么，如下图所示，如若添加了不在__slots__里面的属性，就会报错
class Person1:
	__slots__ = ['age']

p1 = Person1()
p1.age = 10
p1.num = 15
print(p1.age)
print(p1.num)
