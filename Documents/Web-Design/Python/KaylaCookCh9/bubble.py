#Kayla Cook
#Bubble Sort
#This code will organzie a list through using the bubble sort method
#--------------------------------------------------------#
#variables
import random
global numComparisons
global numSwaps
numComparisons = 0
numSwaps = 0
#-----------------------------------------------------#
#bubble sort function
def bubbleSort(array, n):
    #the array can have an interget with a maximimum value
    #of n-1, as determined by y = random.randint(0, n-1)
    #found in the main module. This gets set as the maximum
    #element in which every element will get compared to
    maxValue = n-1
    while maxValue >= 0:
        index = 0
        while index <= maxValue -1:
            if array[index] > array[index + 1]:
                #elements are compared to its neighbor
                #if the element at the current index is greater
                #than its neighboring element, the two get switched
                global numSwaps
                #if the above condition is true, a swap is made
                #and the swap counter increases by one
                numSwaps = numSwaps + 1
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp
            #increase index
            #since a comparison was made, increase comparison
            #even if the inner loop isn't performed
            #a comparison was still made
            index = index + 1
            global numComparisons
            numComparisons = numComparisons + 1
        #since every element was compared to the max element, the
        #previous max element is in it's place
        #a new max element must be determined so the comparison
        #loop can start again to sort
        maxValue = maxValue - 1
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
#-----------------------------------------------------#
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
    bubbleSort(array, n)
#------------------------------------------------------#
#call main
main()
#-----------------------------------------------------#
