#Kayla Cook
#Program 6-8 Odd/Even Counter

#global variables
numEven = 0
numOdd = 0
number = 0

import random

#main module generates 100 random numbers
def main():
    for count in range (100):
        number = random.randint (1, 1999)
        if (number % 2) == 0:
            global numEven
            numEven = numEven + 1
        else:
            global numOdd
            numOdd = numOdd + 1
    

#call main
main()

#print results
print("Out of 100 randomly generated numbers...")
print(numEven, " numbers were even")
print(numOdd, " numbers were odd")
