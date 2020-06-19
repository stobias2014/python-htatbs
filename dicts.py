#!/bin/python3


print("Dictionaries and Structuring Data\n")


employees = {1:"Saul", 2:"Brenda", 3:"Kareli"}

print("employees: {0}".format(employees))
print("Type: {0}".format(type(employees)))

print("\nKeys")
for k in employees.keys():
    print("Keys: {0}".format(k))

print("\nValues")
for v in employees.values():
    print("Value: {0}".format(v))


print("\nItems")
for i in employees.items():
    print("Item: {0}".format(i))


print("\nKey and Value")
for k, v in employees.items():
    print("Key: {0} ---- Value: {1}".format(k, v))

print("\nDoes key exist?")
if 1 in employees.keys():
    print("Key exists")
else:
    print("Key does not exist")

print("\nDoes value exist?")
if "Saul" in employees.values():
    print("Value exists")
else:
    print("Value does not exist")

print("\nGetting an item")
employee = employees.get(1, "Default")
print("Employee: {0}".format(employee))





