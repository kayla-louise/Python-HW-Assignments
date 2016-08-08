#Kayla Cook
#10-7
#Best Golf Scores

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
#call first program
main1()

#program 2 reads golf.dat and displays
def main2():
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


#call second program
main2()
