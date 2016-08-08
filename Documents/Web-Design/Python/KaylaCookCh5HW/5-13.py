#Kayla Cook
#5-13 ESP game

#global variables
colorList = ["red", "green", "blue", "orange", "yellow"]
correctCount = 0
import random

print("Welcome to the ESP game!")

#runs program 10 times
for x in range(10):
    randomItem = random.choice(colorList)
    userColor = input("Please enter red, green, blue, orange, or yellow : ")
    print("The correct answer was: ",randomItem)
    if userColor == randomItem:
            correctCount = correctCount + 1
    else:
            correctCount = correctCount + 0
            
#end of game
print("Thank you for playing!")
print("you got: ", correctCount, " correct")

#results message
if correctCount > 7 :
    print("you have ESP abilities!")
else:
    print("sorry you do not have ESP")
