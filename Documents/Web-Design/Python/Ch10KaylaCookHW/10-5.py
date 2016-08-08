#Kayla Cook
#10-5
#Largest number

#global variables
global number
number = 0.00
global highestNum
highestNum = 0.00

#open file inputfile#5.dat
print("Let's find the largest number from the file!")
numFile = open('inputfile#5.dat', 'r')

#read file
line = numFile.readline()
#compare number
for line in numFile:
    strNum = numFile.readline()
    strNum = strNum.rstrip('\n')
    global number
    number = float(strNum)
    if number > highestNum:
        global highestNum
        highestNum = number
    

#close file
numFile.close()
              
#print highest number
print("The highest number is : ", highestNum)               
