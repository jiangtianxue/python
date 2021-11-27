
class Person:
    # 没有self或者在__init__之前的是类对象
    name = 'liurun'
    grade = '80'

    def __init__(self, age, gender, weight):
        self.age = age
        self.gender = gender
        self.weight = weight

        self.grade_int()

    def grade_one(self):
        self.kkk = 50
        self.grade = '60'
        print('分数是：' + self.grade)
    
    def grade_int(self):
        print('fenshushi ' + self.grade)
        print('kaodefenshushi ' + Person.grade)
        print('这是什么意思')


one = Person(12, 'male', 160)
print(one.__dict__)
one.grade_one()
print(one.__dict__)
print(Person.__dict__)
# two = Person(15, 'female', 148)

# one.grade_int()
# one.grade_one()
# one.grade_int()
# Person.grade = '70'
# one.grade_int()
# print(Person.__dict__)
# print(one.__dict__)
# print(two.__dict__)


# print(one.name, one.grade)
# print(two.name, two.grade)


# one.grade_one()
# one.grade_int()
# two.grade_int()
# two.grade_one()

# print(one.grade)
# print(two.grade)

# print(Person.__dict__)
# print(one.__dict__)
# print(two.__dict__)

# print(Person.grade)

