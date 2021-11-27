class Person:
	__age = 18

	def __run(self):
		print('pao')

p = Person()
print(Person.__dict__)
print(p.__dict__)
# p.__run()
