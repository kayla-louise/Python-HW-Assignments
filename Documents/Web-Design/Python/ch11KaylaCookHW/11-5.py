#Kayla Cook
#11-5
#Golf Scores Modified


#print menu
def print_menu():
    print("Springfork Amateur Golf Club")
    print("=============================")
    print("1. Create new golf data")
    print("2. View golf data")
    print("3. Add onto existing golf data")
    print("4. Calculate best score")
    print("5. Calculate worst score")
    print("6. Exit Program")
    selection = int(input("Please choose a menu option"))
    while selection < 1 or selection > 6 :
        print("That is not a valid menu option")
        selection = int(input("Please choose a menu option"))
    if selection == 1:
        main1()
    elif selection == 2:
        main2()
    elif selection == 3:
        main3()
    elif selection == 4:
        main4()
    elif selection == 5:
        main5()
    elif selection == 6:
        main6()
    else:
        print("Sorry an unknown error has occurred, please try again")
        print_menu()
        
#program 1 writes each players name and score to golf.dat
def main1():
    #get number of golfers to enter
    numPlayers = int(input("How many player's records do you want to create? "))

    #open file to write to
    playersFile = open('golf.dat', 'w')

    #get player data to write
    for count in range(1, numPlayers + 1):
        #get player data
        print("Enter data for player # ", count)
        print
        name = input("Name: ")
        score = input("Golf Score: ")

        #write data as a record
        playersFile.write(name + '\n')
        playersFile.write(score + '\n')

    #close file
    playersFile.close()
    print("Player names and scores have been written to golf.dat ")
    print_menu()

#program 2 reads golf.dat and displays
def main2():
    #open golf.dat file
    playersFile = open('golf.dat', 'r')

    #read the first field of the first record
    name = playersFile.readline()

    #use while loop to go through file
    while name != '':
        #read score
        score = playersFile.readline()

        #strip the newlines
        name = name.rstrip('\n')
        score = score.rstrip('\n')

        #display record
        print("Name: ", name)
        print("Score: ", score)
        print

        #read next record
        name = playersFile.readline()

    #close the file
    playersFile.close()
    print_menu()

#program 3 appends to existing golf.dat
def main3():
    #get number of golfers to enter
    numPlayers = int(input("How many player's records do you want to add? "))

    #open file to write to
    playersFile = open('golf.dat', 'a')

    #get player data to write
    for count in range(1, numPlayers + 1):
        #get player data
        print("Enter data for player # ", count)
        print
        name = input("Name: ")
        score = input("Golf Score: ")

        #write data as a record
        playersFile.write(name + '\n')
        playersFile.write(score + '\n')

    #close file
    playersFile.close()
    print("Player names and scores have been written to golf.dat ")
    print_menu()

#program 4 calculates the best score (lowest score)
def main4():
    try:
        nameArray = []
        scoreArray = []
        #open golf.dat file
        playersFile = open('golf.dat', 'r')
        line = playersFile.readline()
        #use for loop to go through file
        for line in playersFile:
            #read name
            name = playersFile.readline()
            #strip the newlines
            name = name.rstrip('\n')
            nameArray.append(name)
            
            #read score
            score = playersFile.readline()
            #strip the newlines
            score = score.rstrip('\n')
            score = int(score)
            scoreArray.append(score)
            
        #close the file
        playersFile.close()
            
            
        #calculate lowest score
        minScore = min(scoreArray)
        item_index = scoreArray.index(minScore)
        print("The lowest score is : ", minScore)
        print("This score belongs to : ", nameArray[item_index])

    #handle errors
    except IOError:
        print("Error: An error occured while reading the file")
    except ValueError:
        print("Error: Non numeric data was found in the file")
    except:
        print("An unknown error has occured")
    print_menu()
#program 5 calculates the worst score (highest score)
def main5():
    try:
        nameArray = []
        scoreArray = []
        #open golf.dat file
        playersFile = open('golf.dat', 'r')
        line = playersFile.readline()
        #use for loop to go through file
        for line in playersFile:
            #read name
            name = playersFile.readline()
            #strip the newlines
            name = name.rstrip('\n')
            nameArray.append(name)
            
            #read score
            score = playersFile.readline()
            #strip the newlines
            score = score.rstrip('\n')
            score = int(score)
            scoreArray.append(score)
            
        #close the file
        playersFile.close()
            
            
        #calculate lowest score
        maxScore = max(scoreArray)
        item_index = scoreArray.index(maxScore)
        print("The highest score is : ", maxScore)
        print("This score belongs to : ", nameArray[item_index])

    #handle errors
    except IOError:
        print("Error: An error occured while reading the file")
    except ValueError:
        print("Error: Non numeric data was found in the file")
    except:
        print("An unknown error has occured")
    print_menu()
#program 6 exits the program
def main6():
    print("Good Bye")
#call start of program
print_menu()

