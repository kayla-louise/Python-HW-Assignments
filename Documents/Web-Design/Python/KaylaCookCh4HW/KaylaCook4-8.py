#Kayla Cook
#4-8 Change for a dollar game

#global constants
pennyValue = 0.01
nickelValue = 0.05
dimeValue = 0.10
quarterValue = 0.25
#global variables
numPennies = 0
numNickels = 0
numDimes = 0
numQuarters = 0
totalAmt = 0.00

#main program asks for the number of each coin
def main():
    global numPennies
    numPennies = int(input("How many pennies do you have?"))
    global numNickels
    numNickels = int(input("How many nickels do you have?"))
    global numDimes
    numDimes = int(input("How many dimes do you have?"))
    global numQuarters
    numQuarters = int(input("How many quarters do you have?"))
    global totalAmt
    totalAmt = float((numPennies * pennyValue) + (numNickels * nickelValue) + (numDimes * dimeValue) + (numQuarters * quarterValue))
#determine if win, if not is amt over or under
    if totalAmt == 1.00 :
        print("Congratulations, you won!")
    else:
        if totalAmt < 1.00 :
            print("Sorry you did not win, you were under $1")
        else:
            if totalAmt > 1.00 :
                print("sorry you did not win, you were over $1")
            else:
                print("an error occurred, try again")
    

#call main
main()
