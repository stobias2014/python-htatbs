#!/bin/python3

import pyinputplus as pyin

name = pyin.inputStr("Enter a name: ")

print(name)

number = pyin.inputNum("Enter a number: ")

print(number)

are_you_old = pyin.inputYesNo("Are you old? ")

print(are_you_old)

email = pyin.inputEmail("Enter an email address: ")

print(email)

password = pyin.inputPassword("Enter a password: ")

print(password)

membership = pyin.inputMenu(["Premium","Pro","Basic"])

print(membership)



