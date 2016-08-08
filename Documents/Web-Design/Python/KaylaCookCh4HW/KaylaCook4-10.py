#Kayla Cook
#4-10 BMI program enhancement

#global variables
bodyMassIndex = 0.00
weight = 0.00
height = 0.00

#main program gets height and weight
def main():
    global weight
    weight = float(input("please enter your weight in pounds:"))
    global height
    height = float(input("please enter your height in inches:"))
    global bodyMassIndex
    bodyMassIndex = float((weight * 703)/(height ** 2))
    bmiResults()

#determine where bmi falls module
def bmiResults():
    if bodyMassIndex < 18.50 :
        print("you are underweight")
    else:
        if bodyMassIndex > 25.00 :
            print("you are overweight")
        else:
            if bodyMassIndex >= 18.50 and bodyMassIndex <= 25.00 :
                print("you have an optimal weight")
            else:
                print("an error has occured")

#call main
main()
