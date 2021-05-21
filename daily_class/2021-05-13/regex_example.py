import re

txt = "my name is agampreet and i have completed my graduation"
x = re.search("^my.*graduation$", txt)
print(x)    # "^" it specifies the starting   , ".*" this specifies that more than  0 items in between,  "$" - last word


x = re.findall("am", txt)
print(x)

x = re.search("\s", txt)
print(x) 
print("x.string=>", x.string)
print(x.span())
x = re.split("\s", txt)
print(x)

x = re.split("a", txt)
print(x)

ids="iovfvfvrvrvr,rvrvrvyhvyh7j57,67hc67h67h65h6h6,6cch6h6h67vhc6"
print(re.split(",", ids))

x = re.sub("i", "-", txt) # to substitute
print(x)

