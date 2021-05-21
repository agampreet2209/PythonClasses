checkOE = lambda n : "Even" if n%2==0 else "Odd"

print(checkOE(30))


# check prime number
# a number divisible by 1 or itself only is a prime number


'''
a function to return true if n is prime
else return false
1 - (2,22) - 23
'''
def isPrime(n):
	for x in  range(2, n):
		if n%x==0:
			return False
	return True


getType = lambda a : f'{a} is Prime' if isPrime(a) else f'{a} not Prime'

print(getType(25))

def checkPrimes(a, b):
	for x in range(a, b):
		if(isPrime(x)):
			print(x)


checkPrimes(1, 100)