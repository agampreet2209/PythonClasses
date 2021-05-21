import random

# non parameterized
def sayHello():
	print("Hello ji")


# parameterized function
def sayHello2(name):
	print("hello ", name)


# function call
sayHello()
sayHello2("Agam")

# non parameterized with return
def turnDice():
	print("dice turned")
	return random.randrange(1,7)

value = turnDice() # turnDice() will return a value so we store this value in a varibale 'value', after it we can use it as per need
print(value)


# default parameter function
def default_hi(name = "not found"):
	print("hi", name)

default_hi()  # defaul param is optional now
default_hi("Agam")


def just_hello(fname, lname):
	print("welcome" , fname, lname)

just_hello("agampreet","singh" )
just_hello("singh", "agampreet")
just_hello(lname = "singh", fname = "agampreet")

def hello_to_all(*args):  #doubt error 
for a in args:
print("hello" ,a)	
hello_to_all("hello")



