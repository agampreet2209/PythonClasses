class Animal():
	name = "Sheru"  # class variable 
	"""docstring for Animal"""
	def __init__(self, arg):  
		super(Animal, self).__init__()
		self.arg = arg  # object variable

	def details(self):
		print(self.__dict__)
		

lion = Animal("agam")

print(lion.arg)

lion.details()


class Vehicle():
	name = "Audi"


truck = Vehicle()
print(truck.name)

truck.driver = "raj"
print(truck.driver)
del lion.arg

lion.name = "Ramu"
print(lion.name)
del lion.name
print(lion.name)