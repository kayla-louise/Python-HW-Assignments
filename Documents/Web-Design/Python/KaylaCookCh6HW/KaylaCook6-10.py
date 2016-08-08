#Kayla Cook
#Program 6-10 Prime List

#main module
def main():
    testNum()

#testNum module
def testNum():
    for n in range(1,101):
        if isPrime(n):
            if n==97:
                print (n)
            else:
                print (n,",")
    
            
#isPrime module   
def isPrime():
    z = input("please input a number :")
    if z < 2:
        status = False
    else:
         for x in range(2,z):
                if z % x == 0:
                    status = False
    return status

#call main
main()
