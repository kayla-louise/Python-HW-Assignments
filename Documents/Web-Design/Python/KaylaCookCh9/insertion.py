#Kayla Cook
#Insertion Sort
#This code will organize a list through the selection sort method
#------------------------------------------------------#
#variables
import random
global numComparisons
global numSwaps
numComparisons = 0
numSwaps = 0
#----------------------------------------------------------#
#insertion sort function
def insertionSort(array, n):
    index = 1
    #element 0 is already sorted so the first comparison begins at
    #element number one
    while index < len(array):
        unsortedNum = array[index]
        #first element gets scanned and is compared to the elements within
        #the sorted array. This unsorted element then gets placed into the
        #array into it's final position. This cycle repeats until all
        #unsorted elements have been sorted
        scanNum = index
        global numComparisons
        numComparisons = numComparisons + 1
        while scanNum > 0 and array[scanNum - 1] > unsortedNum:
            array[scanNum] = array[scanNum -1]
            scanNum = scanNum - 1
            global numSwaps
            numSwaps = numSwaps + 1
        array[scanNum] = unsortedNum
        index = index + 1
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
    insertionSort(array, n)
#-----------------------------------------------------------#
#call main module
main()
#--------------------------------------------------------#

