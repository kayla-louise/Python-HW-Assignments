#Kayla Cook
#10-5
#Largest number

#variables
number=[]


#open file inputfile#5.dat
print("Let's find the largest number from the file!")
numFile = open('inputfile#5.dat', 'r')

#read file
line = numFile.readline()
#compare number
for line in numFile:
    strNum = numFile.readline()
    strNum = strNum.rstrip('\n')
    num = float(strNum)
    number.append(num)
    

#close file
numFile.close()
              
#print highest number
highestNum = max(number)
print("The highest number is : ", highestNum)               
