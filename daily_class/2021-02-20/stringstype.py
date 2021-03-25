# string -> character array
s = "test 1"
s2 = 'test 2'
s3 = str(10) # type casting -> using constructor function

print(s)
print(s2)
print(type(s3))

for x in s:  # using for loop to iterate through each characcter of string
	print(x) 

print(len(s))


print("es" in s)
print("  " not in s)