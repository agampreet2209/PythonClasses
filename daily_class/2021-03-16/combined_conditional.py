 #we also have 'and' and 'or' operator
a = -20
b = -100
c = -150


max = 0

# nested if
if a>b:
	# a is greater then b
	# now compare a with c
	if a>c:
		max = a
	else:
		max = c
else:
	# b is greater then a
	# now compare b with c
	if b>c:
		max = b
	else:
		max = c


# and and or operator
if a>b and a>c:
	max = a
elif b>a and b>c:
	max = b
else:
	max = c

print(max)

print(max)




# check wheter a is smallest or not
if a>b or a>c:
	print('a is not a smallest number among a,b and c')
else:
	print('a is a smallest number')