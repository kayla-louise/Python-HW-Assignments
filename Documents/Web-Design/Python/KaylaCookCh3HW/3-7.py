# Kayla Cook
#Program 3-7
#Calories From Fat and Carbs

#global variables
fatGrams = 0
carbGrams = 0

# main module
def main():
    global fatGrams
    global carbGrams
    fatGrams = float(input("Please enter the number of fat grams: "))
    carbGrams = float(input("Please enter the number of carbohydrate grams: "))
    calcFatCal()
    calcCarbCal()
    

# calculate calores from fat
def calcFatCal():
    fatCals = fatGrams * 9
    print("The number of calories from fat is ", fatCals)

#calculate calories from carbs
def calcCarbCal():
    carbCals = carbGrams * 4
    print("The number of calories from carbohydrates is ", carbCals)

#call main function
main()
