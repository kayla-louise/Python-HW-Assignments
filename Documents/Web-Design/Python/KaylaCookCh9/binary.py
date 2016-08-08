#Kayla Cook
#Binary Search
#This code will search for an item using the binary search method
#----------------------------------------------------------#
#binary search function
def binarySearch (list, value):
    comparisonNum = 0
    lowNum = 0
    upNum = len(list)
    while True:
        comparisonNum = comparisonNum + 1
        if upNum == lowNum:
            print("The number of comparisons done were: ", comparisonNum)
            return -1
        #find index number between the highest and lowest index
        middleI = (lowNum + upNum) // 2
        """grab number at that index, this becomes the number that the
        search value is compared to"""
        midElement = list[middleI]

        #value being searched for is compared to middle element
        if midElement == value:
            print("The number of comparisons done were: ", comparisonNum)
            return middleI
        #If the value being searched for is higher than the middle
        #element used in the last comparison, the computer will then search the
        #upper half of the array and discard the lower half. Since the middle
        #element has already been used for comparison, the next element is then
        #used as the new lower boundary and the process repeats
        if value > midElement:
            lowNum = middleI + 1
        #If the value being searched for is lower than the middle
        #element used in the last comparison, the computer will then search the
        #lower half of the array and discard the upper half. The middle element
        #now becomes the new higher boundary and the process repeats
        else:
            upNum = middleI
#----------------------------------------------------------#
#print results module
def results(isFound, value):
    if (isFound == -1):
        print("Sorry the number ", value,  " you were searching for was not in the array")
    else:
        print("The number ", value, " was found in the array at index # ", isFound)
#----------------------------------------------------------#
#main module
def main():
    #get n from user
    n = int(input("Please enter 'n', the maximum number of values"))
    array = []
    for x in range(0, n):
        array.append(x)
    print("Would you like to view the contents of the array?")
    viewArray = input("Type Y if yes. Type any other key for no : ")
    if (viewArray == 'Y' or viewArray == 'y'):
        print
        print("_________________________")
        print("Here are the contents of the array")
        print(array)
        print("_________________________")
        print
    #find number to search for
    value = int(input("What number do you want to search for? "))
    #run binary search function
    isFound = binarySearch(array, value)
    #run print results
    results(isFound, value)
#----------------------------------------------------------#              
#call main module
main()
