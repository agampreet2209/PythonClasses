class Honda():
	def subfourmeter(self):  #can act as object
		print("WRV comes under this category ")  #it is a method to print 

	def sedans(self):
		print("honda city comes under this category")

	def suv(self):
		print("CRV comes under this category")

class Toyota():
	def	subfourmeter(self):
		print("liva comes under this category")

	def	sedans(self):
		print("yaris comes under this category")

	def suv(self):
		print("fortuner comes under this category")

obj_hon = Honda()
obj_toy = Toyota()
for cars in (obj_hon, obj_toy):
	cars.subfourmeter()
	cars.sedans()
	cars.suv()		



#polymorphism example

num1 = 1
num2 = 2
print(num1+num2) # 1 and 2 gives an output 3 


#inheritence example

class person:
	def __init__(self,fname,lname):
	  self.firstname = fname
	  self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)

x = person("agampreet", "singh")
x.printname()








