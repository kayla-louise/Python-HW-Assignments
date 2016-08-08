#Kayla Cook
#4-9 Shipping Charges

#global constants
#weight for 2 lbs and less
rate1 = 1.10
#weight for more than 2 lbs and less than or equal to 6
rate2 = 2.20
#weight for more than 6 lbs and less than or equal to 10
rate3 = 3.70
#weight for more than 10 lobs
rate4 = 3.80


#global variables
packageWeight = 0


#main program asks user for package weight
def main():
    global packageWeight
    packageWeight = float(input("Please enter the weight of your package in lbs :"))
    if packageWeight <= 2 :
        calc_rate1()
    else:
        if packageWeight > 2 and packageWeight <= 6 :
            calc_rate2()
        else:
            if packageWeight > 6 and packageWeight <= 10 :
                calc_rate3()
            else:
                calc_rate4()

#calculate rate 1
def calc_rate1():
    shipCost1 = float(rate1 * packageWeight)
    print("Your shipping charges will be $",shipCost1)

#calculate rate 1 and rate 2
def calc_rate2():
    remaininglbs1 = float(packageWeight - 2)
    shipCost2 = float((rate1 * 2) + (rate2 * remaininglbs1))
    print("Your shipping charges will be $",shipCost2)

#calculate rate 1 and rate 2 and rate 3
def calc_rate3():
    remaininglbs2 = float(packageWeight - 6)
    shipCost3 = float((rate1 * 2) + (rate2 * 4) + (rate3 * remaininglbs2))
    print("Your shipping charges will be $",shipCost3)

#calculate rate 1 and rate 2 and rate 3 and rate 4
def calc_rate4():
    remaininglbs3 = float(packageWeight - 10)
    shipCost4 = float((rate1 * 2) + (rate2 * 4) + (rate3 * 4) + (rate4 * remaininglbs3))
    print("Your shipping charges will be $",shipCost4)

#call main
main()
