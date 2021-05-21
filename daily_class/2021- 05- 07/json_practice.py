import json

x = '{"name":"Agam","age":21, "religion": "sikh"}'
y = json.loads(x)

print(y["age"])

