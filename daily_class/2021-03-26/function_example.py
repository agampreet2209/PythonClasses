# function - > code resuability, easy to read and understand code


def calculateSi(p, t, r=10):
	return p * r * t / 100


si = calculateSi(100, 2)
# si = 100 * 10 * 2 / 100
print(si)


si = calculateSi(1000, 5, 20)
print(si)



def printTable(n):
	for i in range(1,11):
		print(f'{n} x {i} = {i*n}')


table = printTable(12)
print(table)


# named argument -> we change positions of arguments
si = calculateSi(t = 3, p = 200, r = 2)
print(si)



