color = None
#color = "red"

try:
	if not color:
		raise Exception( "Incorrect color")  # raise is used to generate exception
	print(color)
except Exception as e:
	print("error=>",e)
	print("transparent")
finally:
	print("color set successfully")



	try:    # multiple except
		print(x)
	except NameError :
		print("Variable x is not defined") #case sensative 
	except :
		print("Something else went wrong")	


try:      # if no error comes the it will print the else statement
	print("hello")
except : 
	print("something went wrong")
else:
	print("nothing went wrong")	 	



x = 2    # even if there is no error it will return the finally statement 
try:
	print(x)
except :
	print("something went wrong")	
finally : 
	print("the 'try except' is finished ")


x = -1      # we can raise our own exception

if x < 0:
	raise Exception("Sorry,no numbers below zero") 









