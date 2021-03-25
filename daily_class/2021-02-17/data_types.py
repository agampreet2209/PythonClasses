# Data Type : it denots what  kind of data is stored in a varibale
# Types of DataTypes
# 1. Text -> str
# 2. Numeric -> int, float, complex
# 3. Squence -> list, tuple, range
# 4. Mapping -> dict
# 5. Set -> set, frozenset
# 6. Boolean -> bool (Treu, False)
# 7. Binary -> bytes, bytearray, memoryview

name = "CMPundhir"
print(type(name))

groc_list = ["Eggs", "Breads"]
groc_list.append("Butter") # we can modify a list
print(type(groc_list))

groc_tuple = ("Eggs", "Breads") # we can modify a tuple
print(type(groc_tuple))

flag = True
flag = False
print(type(flag))