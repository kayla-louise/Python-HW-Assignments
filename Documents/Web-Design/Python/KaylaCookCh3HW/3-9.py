#Kayla Cook
#HW 3-9
#Paint Job Estimate

#global variables
sqFeet = 0
costPerGallon = 0
gallonsNeeded = 0
hrsNeeded = 0

#main module
def main():
    global sqFeet
    global costPerGallon
    sqFeet = float(input("How many square feet of wall do you need painted? "))
    costPerGallon = float(input("What is the cost per gallon for paint? $"))
    calcGallons()
    calcHrsLabor()
    
#gallons needed
def calcGallons():
    global gallonsNeeded
    gallonsNeeded = float(sqFeet/115.00)
    print("The number of gallons needed are ", gallonsNeeded)
#number of hours of labor
def calcHrsLabor():
    global hrsNeeded
    hrsNeeded = float(sqFeet * 8)
    print("The number of hours of labor are ", hrsNeeded)

#cost of everything

#call main
main()
