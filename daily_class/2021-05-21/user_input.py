# for user input from STDIN -> we have input() function
# input() returns a string
# input(param) -> we can pass a string message in input funciton for hint

name = input("Enter your name : ")
print(name)

age = int(input("Enter your age : ")) # type castring of str to int
if age<18:
	print("Children are not allowed")
else:
	print("Please Pay Fee")
	fee = float(input("Enter Entry fee : "))
	if fee == 99.99:
		print("Party")
	else:
		print("Sorry incorrect amount")


