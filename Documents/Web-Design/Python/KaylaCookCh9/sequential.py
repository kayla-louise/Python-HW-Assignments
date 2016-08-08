#Kayla Cook
#Sequential Search
#This code will search for an item using the sequential search method
#----------------------------------------------------------#
#sequential search function
def sequentialSearch (array, value):
    comparisonNum = 0
    index = 0
    while (index < len(array)):
        comparisonNum = comparisonNum + 1
        if(array[index] == value):
            print("The number of comparisons done were: ", comparisonNum)
            return index
        index = index + 1
    print("The number of comparisons done were: ", comparisonNum)
    return -1
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
    #Find number to search for
    value = int(input("What number do you want to search for? "))
    #Run squential search function
    isFound = sequentialSearch (array, value)
    #Run print results
    results(isFound, value)
#----------------------------------------------------------#
#call main module
main()
