#!/bin/python3

def localVariable():
    spam = "eggs"
    print("Local variable: " + spam)
    return

def addNumbers(num1, num2):
    result = num1 + num2
    return result

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("{0} + {1} = {2}".format(num1, num2, addNumbers(num1, num2)))

