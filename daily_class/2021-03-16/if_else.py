# we check for conditions in it
# lets we have 2 variables of int type a, b so we can apply below
# ==, !=, >, <, >=, <=

a = 10
b = 20
if a == b:
	print("both are equal")
else:
	print("not equal")

if a != b:
	print('both are not equal')
else:
	print('both are equal')

if a > b:
	print('a is greater')

if a < b:
	print('a is smaller')

if b > a:
	print('b is greater')


# one line if else -> other language have a ternery operator for this purpose

max = a if a>b else b

print(max)

# so to reduce numbe rof line of code use one line if else.
ans = f'{a} > {b}' if a>b else f'{a} < {b}'

print(ans)

# general way for setting a particula variable value according to conditions
if a>b:
	ans = f'{a} > {b}'
else:
	ans = f'{a} < {b}'

print(ans)



# we also have 'and' and 'or' operator
if 


