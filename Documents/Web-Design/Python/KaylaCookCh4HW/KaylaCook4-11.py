#Kayla Cook
#4-11

#global constants
secInMin = 60
secInHrs = 3600
secInDay = 86400
#global variables
numSec = 0

#main asks for number of seconds and determines correct module
def main():
    global numSec
    numSec = int(input("Please enter a number of seconds:"))
    if numSec < 60 :
        print("The number in seconds is equal to ",numSec," seconds")
    else:
        if numSec >= 60 and numSec < 3600 :
            calcMin()
        else:
            if numSec >= 3600 and numSec < 86400 :
                calcHrs()
            else:
                if numSec <= 86400 :
                    calcDays()
                else:
                    print("an error has occurred")
            
                
#calc minutes module
def calcMin():
    numMin = float(numSec/secInMin)
    print(numSec," seconds is equal to ",numMin," minutes")

#calc hrs module
def calcHrs():
    numHrs = float(numSec/secInHrs)
    print(numSec," seconds is equal to ",numHrs," hours")
#calc days module
def calcDays():
    numDays = float(numSec/secInDay)
    print(numSec," seconds is equal to ",numDays," days")

#call main
main()

