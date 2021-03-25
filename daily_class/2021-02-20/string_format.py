name = "Agampreet"
age = 21
message = "I am "+name+" and i am "+str(age)+" years old" 
print (message)


message2 = "I am {} and i am {} years old" 
message22 = "I am {1} and i am {0} years old" 
print(message2.format(name, age))
print(message22.format(age, name))


message3 = f"I am {name} and i am {age} years old" 
print(message3)