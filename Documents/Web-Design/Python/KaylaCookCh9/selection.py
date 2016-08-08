#Kayla Cook
#Selection Sort
#This code will organize a list through the selection sort method
#------------------------------------------------------#
#variables
import random
global numComparisons
global numSwaps
numComparisons = 0
numSwaps = 0
#----------------------------------------------------------#
#selection sort function
def selectionSort(array, n):
    startNum = 0
    #the startNum is the position in the array in which comparisons will
    #start. The while loop continues to iterate while this number is
    #less than the array size minus one. The minus one part is because
    #by the time it equals the length of the array, the last element
    #will already be in the correct position
    while startNum < len(array) - 1:
        #the first element is assumed to be the smallest number
        #so that all other elements can be compared to it
        minNum = array[startNum]
        index = startNum + 1
        global numComparisons
        numComparisons = numComparisons + 1
        #the list will be scanned for the smallest element
        #if a number is found to be the smallest, it will be
        #swapped with the first element within the area being searched
        while index < len(array):
            if array[index] < minNum:
                minNum = array[index]
                minIndex = index
                global numSwaps
                numSwaps = numSwaps + 1
            index = index + 1
        array[minIndex] = array[startNum]
        array[startNum] = minNum
        #area being scanned is now smaller by one element now that the
        #smallest number in the previous scan was established
        #increase startNum so scan size is smaller in next scan
        startNum = startNum + 1
    printModule(numComparisons, numSwaps, array)
        
#----------------------------------------------------#
#print results module
def printModule(numComparisons, numSwaps, array):
    print("The number of comparisons done were", numComparisons)
    print("The number of swaps done were", numSwaps)
    print("Would you like to view the contents of the array?")
    viewArray = input("Type Y if yes. Type any other key for no : ")
    if (viewArray == 'Y' or viewArray == 'y'):
        print
        print("_________________________")
        print("Here are the contents of the array")
        print(array)
        print("_________________________")
        print
    
#---------------------------------------------------------#
#main module
def main():
    array = []
    #get n from user
    n = int(input("Please enter the size of the array : "))
    for x in range(0, n):
        y = random.randint(0, n-1)
        array.append(y)
    print("Would you like to view the contents of the array?")
    viewArray = input("Type Y if yes. Type any other key for no : ")
    if (viewArray == 'Y' or viewArray == 'y'):
        print
        print("_________________________")
        print("Here are the contents of the array")
        print(array)
        print("_________________________")
        print
    selectionSort(array, n)
#-----------------------------------------------------------#
#call main module
main()
#--------------------------------------------------------#
