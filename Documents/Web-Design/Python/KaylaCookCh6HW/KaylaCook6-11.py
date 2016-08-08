#Kayla Cook
#Program 6-11 Rock Paper Scissors Game
#1 = rock  2=paper  3=scissors

#global variables
playerName = " "
playersChoice = 0

import random

#Program intro
print("Welcome to the rock paper scissors game!")
global playerName
playerName = input("What is your name? ")

#computer picks rock paper scissors

computerChoice = ((random.randint(1,4))

#user picks rock paper scissors

playersChoice = input("Please choose rock, paper, or scissors : ")
playersChoice = playersChoice.lower()
if playersChoice == "rock":
    global playersChoice
    playersChoice = int(1)
else:
    if playersChoice == "paper":
           global playersChoice
           playersChoice = int(2)
    else:
        if playersChoice == "scissors":
             global playersChoice     
             playersChoice = int(3)
        else:
            print("An error occurred, please try again")

#display computer choice
print("The computer chose: ", computerChoice)

#calculate winner
if playersChoice == computerChoice :
    print("Both the computer and ", playerName, "chose ", playerschoice, " ... draw")
else:
    if playersChoice == 1 and computerChoice == 3 :
        print(playerName, " is the winner! ")
    else:
        if computerChoice == 1 and playersChoice == 3 :
            print("The computer is the winner!")
        else:
            if playersChoice == 1 and computerChoice == 2 :
                print("The computer is the winner!")
            else:
                if computerChoice == 1 and playersChoice == 2 :
                    print(playerName, " is the winner! ")
                else:
                    if playersChoice == 2 and computerChoice == 3 :
                        print("The computer is the winner!")
                    else:
                        if computerChoice == 2 and playersChoice == 3 :
                            print(playerName, " is the winner! ")
                        else:
                            print ("sorry an error occurred")
                    
