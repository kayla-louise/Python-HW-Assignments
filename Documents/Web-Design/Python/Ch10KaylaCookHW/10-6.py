#Kayla Cook
#10-6
#Golf Scores

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

#call second program
main2()
