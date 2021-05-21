import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A")) # %A code for getting the specific day

x = datetime.datetime(2020, 12, 10)
print (x)  # to create a date

print(x.strftime("%B")) # to get the name of the month
