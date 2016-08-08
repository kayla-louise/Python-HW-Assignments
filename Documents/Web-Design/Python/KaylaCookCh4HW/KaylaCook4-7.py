#Kayla Cook
#4-7 Software Sales

#global constants
originalPrice = 99
#global variables
numberPurchased = 0
discountAmt = 0
discountPrice = 00
totalPurchase = 00

#main program asks for number purchased, calculates discount and total price
def main():
    global numberPurchased
    numberPurchased = int(input("Please enter the number of packages purchased: "))
    discountCalc()
    global discountPrice
    discountPrice = int(originalPrice * (discountAmt/100))
    print("Your discount is $", discountPrice)
    global totalPurchase
    totalPurchase = int((numberPurchased * originalPrice) - discountPrice)
    print("Your total with discount for ", numberPurchased, "packages, is $", totalPurchase)
    print("Thank you for your purchase!")
    
            
#calculates discount
def discountCalc():
    global discountAmt
    if numberPurchased >= 10 and numberPurchased <= 19 :
        discountAmt = 20
    else:
        if numberPurchased >= 20 and numberPurchased <= 49 :
            discountAmt = 30
        else:
            if numberPurchased >= 50 and numberPurchased <= 99 :
                discountAmt = 40
            else:
                if numberPurchased > 100:
                    discountAmt = 50
                else:
                    discountAmt = 0          

#call main
main()                
