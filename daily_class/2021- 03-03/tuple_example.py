stationary = ("pencil", "pen", "eraser", "sketchpen")
print(stationary)

print(len(stationary))

stationary = ("pencil",)
print(type(stationary))

fruits = tuple(("orange", "mango", "guava"))
print(fruits)

cars = ("suv", "sedan", "hatchback", "crossover")
print(cars[1])

print(cars[-1])
print(cars[1:3])#range of indexing
print(cars[:4])

cars = list(fruits) #to change tuple values
cars[1] = "apple"  #doubt
fruits = tuple(cars)
print(fruits)

(green, yellow, *red) = cars #using *
print(green)
print(yellow)
print(red)



