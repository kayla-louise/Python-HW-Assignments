#Kayla Cook
#Program 6-9 Prime Calculator

#global
number = 0
maxLimit = 0

#main module asks for a number and calculates if prime
def main():
    global number
    number = int(input("Please input a number to check if it is prime : "))
    global maxLimit
    maxLimit = number
    isPrime(number, maxLimit)

#isPrime module
def isPrime(number, maxLimit):
    for x in range (3,maxLimit, 2):
        if (number % x) == 0:
            status = True
            print(number, " is a prime number")
        else:
            status = False
            print(number, " is not a prime number")
        return status


#call main
main()


