# number system
# decimal -> 0,1,2,3,4,5,6,7,8,9    
# eg 123 -> 100 * 1 + 10 * 2 + 3

'''
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14...


# binary -> 0,1
# es 101 -> 2^2 * 1 + 2^1 * 0 + 2^0 * 1
#			4 + 0 + 1
# 			5

0   ->0
1   ->1
10  ->2
11  ->3
100 ->4
101 ->5
110
111
1000

'''

x = 5
print(x)

print(bin(x))
x += 1
print(bin(x))


# or => one of them must be true
# and => all of them must be true

x = 5
x |= 3
print(x)
'''
5 =		101
3 = 	 11
OR = 	---
		111 => 7
'''

x = 15
x |= 3
print(x)

# 15 = 1111
# 3  =   11
#or    ____
#       1111 => 15
'''
15%2 = 1
7%2 =  1
3%2 =  1
1

1111

'''
x = 15
x &= 7
print(x)

101000
x = 10
x <<=2
print (x)

x = 10
x >>=2 
print (x)
