# boolean -> True or False

flag = True
print(flag)
flag = False
print(flag)

c = 10 + 50  # return int
flag = 10 < 50  # return boolean
print(flag)
print(10>50)
print(10==50)
print(10<50)
print(10<=50)
print(10>=50)

print(10<10)
print(10>10)
print(10<=10)
print(10>=10)
print(10==10)  # == is equality operator

print(type(flag))

flag = bool("")  #if we put a value in it then it is true else it will be false
print(flag)

flag = bool(0)
print(flag)

flag = bool(["apple","banana","waterm","",""])
print(flag)
