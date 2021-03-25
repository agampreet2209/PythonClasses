# slicing

s = "Hello,Agam. Hows you, what about abc, so lets do it"
print(s[6:10])
print(s[6:])
print(s[:5])
print(s[:])

# negative slicing
print(s[-6:])
print(s[-3:-1])


# modifying a string
print(s.upper())  # upper() function converts a string into uppercase
print(s.lower())  # lower() function converts a string into lowercase

# remove whitespace
print(s.strip())  # To remove space 

# replace
print(s.replace("Hello", "Party"))

# split
print(s.split(","))



