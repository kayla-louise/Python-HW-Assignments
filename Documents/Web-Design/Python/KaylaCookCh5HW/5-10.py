#Kayla Cook
#5-10 highest and lowest number

#global variables
number = 0
highestNum = 0
lowestNum = 0

#get the first number
print("Welcome to the high/low calculator")
print("To quit program type -99")
number = int(input("Please enter a number : "))
highestNum = number
lowestNum = number
while number != -99 :

#continue number comparisons as long as -99 isn't entered
    if number < lowestNum :
            lowestNum = number
    elif number > highestNum :
            highestNum = number
        
    number = int(input("Please enter another number : "))

        
#once -99 is entered
print("The lowest number entered was ", lowestNum )
print("The highest number entered was ", highestNum)
    
