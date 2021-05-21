import classes_object_examples as m1


class Human(m1.Animal):
	def __init__(self, name):
		super(m1.Animal, self).__init__()
		self.name = name


human1 = Human("Agampreet")

human1.details()


mytuple = ("honda", "toyota", "maruti") # iterator
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

for x in mytuple: # for loop in mytuple
	print(x)

# pyhton scope 

x = 1000 # global value of x 

def myfunc():
	x = 550 # local value of x
	print(x)

myfunc()

print(x)




def myfunc():
	global x
	x = 1000
	x = 550   #updates with the latest value 

myfunc()

print(x)


x = 5000

def myfunc():
	global x 
	x = 200  # it is the latest updated value 

myfunc()

print(x)










