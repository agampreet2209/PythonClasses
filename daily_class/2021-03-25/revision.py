print("Hey, its python ....")
print("Hey, \nits python ....")

a = 10
b = 20
c = a + b
print(c)

# hey i am a comment, and i am very useful but yeah i don't have any meaning for you computer program...

p = 1000
r = 10
t = 2

si = p * r * t / 100
print(si)

# string concatenations
fname = 'Agampreet'
lname = "Singh"
fullname = fname + lname;
print(fullname)


# operators
x = 17/3
print(x)
x = 17//3
print(x)
x = 17%3
print(x)


#program for checking a number is odd or even
num = 12
if num%2==0:
	print("even number")
else:
	print("odd number")


#datatype
# string, number, tuple, list, set, dictionary
print(type(num))

# in python everything is an object


# escape characters
print("hello\tagam")


#string format
intro = f'I am {fullname}.'
print(intro)

intro2 = 'i am {}'
print(intro2.format(fullname))

intro3  = 'i am {1} {0}'
print(intro3.format(fname, lname))



import random
# number
print(random.randrange(1,7))


# boolean
flag = True
print(not flag)


# binary number
print(bin(p))

# list
grocery_list = ['vegetables', "fruits" , "sugar" , "salt"]
print(grocery_list)

grocery_list.append('milk')
print(grocery_list)



# loop
for x in grocery_list:
	print(x)

while p>0:
	p -= 100
	print(p)

# tuple : cannot modify once created
marks = ('90', '80')
print(type(marks))


# set : no duplicacy
jwel_set = {'ring', 'necklace'}
print(jwel_set)


# dictionary : key-value pair
cost = {'vegetables': 120, "fruits": 200, "sugar": 80, "salt": 12}
print(cost)
totalCost = 0
for k in cost:
	totalCost += cost[k]
print(totalCost)


# shorthand if else
max = a if a>b else b
min = a if a<b else b
print('max: ', max)
print('min: ', min)


# and and or operator
# find smallest number from a, b, c
if a<b and a<c:
	print('a is smallest')
elif b<a and b<c:
	print('b id smallest')
else:
	print('c is smallest')


# hurry...github setup completed!!!



