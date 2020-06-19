#!/bin/python3

import random

names = ["Saul", "Brenda", "Kareli"]
print("Before shuffle: {0}".format(names))
random.shuffle(names)
print("After shuffle: {0}".format(names))

print("Random Name: {0}".format(random.choice(names)))

print("Looping through a list of names")

for i in range(len(names)):
    print("names[{0}] = {1}".format(i, names[i]))

list_with_list = [[0, 1, 2], [0, 1, 2]]

for x in range(len(list_with_list)):
    for y in range(len(list_with_list[x])):
        print("list_with_list[{0}][{1}] = {2}".format(x, y, list_with_list[x][y]))


numbers = [0,1,2,3,4,5,6]

print(numbers)
print("A slice of a list: {0} ".format(numbers[1:3]))

print("Names for dogs")

dog_names = []

for i in range(0, 4):
    dog_name = input("Enter dog name: ")
    dog_names = dog_names + [dog_name]

print(dog_names)

print("Check if 'pimpon' exists in list")

if "pimpon" in dog_names:
    print("pimpon exists in list")
else:
    print("pimpon does not exist in list")
print("Thank you")

hot_sauces = []

for i in range(0, 4):
    hot_sauce_name = input("\nEnter hot sauce name: ")
    hot_sauces.append(hot_sauce_name)

print("Before Sort")
print("Hot Sauces: {0}".format(hot_sauces))

print("\nAfter Sort")
hot_sauces.sort()
print("Hot Sauces: {0}".format(hot_sauces))




