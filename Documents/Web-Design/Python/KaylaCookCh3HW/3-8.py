#Kayla Cook
#Program 3-8
#Stadium Seating

#global varibales
numATix = 0
numBTix = 0
numCTix = 0
incomeA = 0
incomeB = 0
incomeC = 0


#main module
def main():
    global numATix
    global numBTix
    global numCTix
    numATix = int(input("How many Class A tickets were sold? "))
    numBTix = int(input("How many Class B tickets were sold? "))
    numCTix = int(input("How many Class C tickets were sold? "))
    calcIncomeA()
    calcIncomeB()
    calcIncomeC()
    calcTotalIncome()
    

#calculate income from Class A tickets
def calcIncomeA():
    global incomeA
    incomeA = int(numATix * 15)
    print("The income generated from Class A Tickets is $", incomeA)

#calculate income from Class B tickets
def calcIncomeB():
    global incomeB
    incomeB = int(numBTix * 12)
    print("The income generated from Class B Tickets is $", incomeB)

#calculate income from Class C tickets
def calcIncomeC():
    global incomeC
    incomeC = int(numCTix * 9)
    print("The income generated from Class C Tickets is $", incomeC)

#calculates total income
def calcTotalIncome():
    totalIncome = (incomeA + incomeB + incomeC)
    print("The total income from all tickets is $", totalIncome)

#call main function
main()
