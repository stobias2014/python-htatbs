#!/bin/python3

import sys
import random

def sips():
    
    sip_count = random.randint(1,10)
    
    print("Sip Count = {0}".format(sip_count))

    for sip in range(sip_count):
        print("Taking sip {0}.....".format(sip + 1))
    
    return


print("Flow Control\n")

while(True): 
    age = input("What is your age?")
    age = int(age)
    if (age < 21):
        print("You are not old enough to drink")
    elif (age > 21 and age < 100):
        print("You've been able to drink")
        sips()
    elif (age == 21):
        print("You are just at the age to drink")
        sips()
    else:
        print("You should not be drinking bones")
    
    should_continue = input("Continue program (y or n)")

    if should_continue == "n":
        print("Program is stopping....\n")
        break
    elif should_continue == "y":
        print("Program will keep going...\n")
    else:
        print("Invalid option\n")
        print("Exiting program......")
        sys.exit()
