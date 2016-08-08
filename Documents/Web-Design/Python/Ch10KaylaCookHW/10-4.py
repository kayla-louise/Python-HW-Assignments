#Kayla Cook
#10-4
#Average of numbers


#main module
def main():
    #declare blank array
    nums = []
    
    #open file numbers.dat for reading
    numFile = open('numbers.dat', 'r')
    line = numFile.readline()
    
    #read numbers from file and put them into array
    for line in numFile:
        #convert line to a float
        x = float(line)
        nums.append(x)
        
    #close file
    numFile.close()
    
    #find array length
    totalNums = len(nums)
    
    #calculate average
    total = 0.00
    count = 0
    for n in range(0, totalNums):
        number = nums[count]
        total = total + number
        count + 1
    average = total/(totalNums + 1)
    print("The average is : ", average)
        
#call main
main()
