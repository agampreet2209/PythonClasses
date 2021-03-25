shopping_list = ["vegetable", "fruits", "bread" , "juices" ,"books" ,"pencil" , "petrol"]
print(shopping_list)
print(type(shopping_list))
print(shopping_list[-1])
print(shopping_list[-2])
print(shopping_list[1:3])
print(shopping_list[1:4])
print(shopping_list[2:])
print(len(shopping_list))#to find total number of itme in the list
shopping_list.append("namkeen") #to add item in the list
print(len(shopping_list))
print(shopping_list)
shopping_list.append("waterbottle")#adds one item at a time
shopping_list.append("bag")
print(shopping_list)
shopping_list[6] = "berry"#to change item in the list
print(shopping_list)

# interchange values using third variable
temp = shopping_list[1]
shopping_list[1] = shopping_list[2]
shopping_list[2] = temp
# alternate way for interchanging in python
shopping_list[1], shopping_list[2] = shopping_list[2], shopping_list[1]
print(shopping_list)

shopping_list.insert( 1, "shoes") #to insert items 
print(shopping_list)

fruit_list = ["apple", "oranges", "banana", "pineapple"]
shopping_list.extend(fruit_list)
print(shopping_list) #to extend list

