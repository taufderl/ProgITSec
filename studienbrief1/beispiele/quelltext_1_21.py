from operator import attrgetter

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __repr__(self):
		return repr((self.name, self.age))

person_objects = [
    Person('Otto', 22),
    Person('Eva', 20),
    Person('Tim', 23),]

print(sorted(person_objects, key=attrgetter('age')))