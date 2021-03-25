s = "My Name Is Agam,i am 21 years old."
print(s.capitalize()) # only converts the first letter into capital by default
print(s.center(100)) # to align the text in the center 
print(s.count("a")) # total repitation 
print(s.expandtabs(2)) # it customizes tab size. It takes optional parameter as a int
print(s.find("name")) # it defines the postion 
print(s.isalnum()) # checks if there are only alphanumeric terms or not
print(s.isdigit()) # checks for digits 
print(s.isidentifier()) #to check wether it is an identifier 
print(s.islower()) #to check that all the characters are in lower cse
print(s.isnumeric()) # to check wether numeric value is used
print(s.isprintable())# weather value is printable
print(s.isspace()) # to check for all charectors are in whitespace
print(s.isupper()) # to check that all charecters are in upper case
print(s.lower()) # converts to lower case
print(s.rfind("Is")) # to find charecter
print(s.rindex("am")) # the charecter where is is found 
print(s.rjust(20)) #right justified version of the word #doubt 
print(s.rpartition("agam")) #doubt
print(s.rsplit(",")) #spliting the term 
print(s.rstrip())#doubt
print(s.splitlines()) #doubt
print(s.startswith("My")) #to check that the sentence starts with My
print(s.strip())#doubt
print(s.swapcase()) #swapping lower case with upper case
print(s.title()) #converts 1st letter of everycase into uppercase
print(s.zfill(20)) #doubt
